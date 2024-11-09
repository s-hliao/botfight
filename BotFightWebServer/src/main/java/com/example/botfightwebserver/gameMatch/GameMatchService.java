package com.example.botfightwebserver.gameMatch;

import com.example.botfightwebserver.Elo.EloCalculator;
import com.example.botfightwebserver.Elo.EloChanges;
import com.example.botfightwebserver.player.PlayerDTO;
import com.example.botfightwebserver.player.PlayerService;
import com.example.botfightwebserver.rabbitMQ.RabbitMQService;
import com.example.botfightwebserver.submission.Submission;
import com.example.botfightwebserver.submission.SubmissionDTO;
import com.example.botfightwebserver.submission.SubmissionService;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Transactional
@RequiredArgsConstructor
public class GameMatchService {

    private final GameMatchRepository gameMatchRepository;
    private final PlayerService playerService;
    private final SubmissionService submissionService;
    private final RabbitMQService rabbitMQService;
    private final EloCalculator eloCalculator;

    public List<GameMatch> getGameMatches() {
        return gameMatchRepository.findAll();
    }

    public GameMatch createMatch(Long player1Id, Long player2Id, Long submission1Id, Long submission2Id, MATCH_REASON reason) {
        playerService.validatePlayers(player1Id, player2Id);
        submissionService.validateSubmissions(submission1Id, submission2Id);
        GameMatch gameMatch = new GameMatch();
        gameMatch.setPlayerOne(playerService.getPlayerReferenceById(player1Id));
        gameMatch.setPlayerTwo(playerService.getPlayerReferenceById(player2Id));
        gameMatch.setSubmissionOne(submissionService.getSubmissionReferenceById(submission1Id));
        gameMatch.setSubmissionTwo(submissionService.getSubmissionReferenceById(submission2Id));
        gameMatch.setStatus(MATCH_STATUS.WAITING);
        gameMatch.setReason(reason);
        return gameMatchRepository.save(gameMatch);
    }

    public GameMatchJob submitGameMatch(Long player1Id, Long player2Id, Long submission1Id, Long submission2Id, MATCH_REASON reason) {
        GameMatch match = createMatch(player1Id, player2Id, submission1Id, submission2Id, reason);
        GameMatchJob job = GameMatchJob.fromEntity(match);
        rabbitMQService.enqueueGameMatchJob(job);
        return job;
    }

    public GameMatchDTO getDTOById(Long id) {
        return GameMatchDTO.fromEntity(gameMatchRepository.getReferenceById(id));
    }

    public GameMatch getReferenceById(Long id) {
        return gameMatchRepository.getReferenceById(id);
    }

    public void handleGameMatchResult(GameMatchResult result) {
        long gameMatchId = result.matchId();
        MATCH_STATUS status = result.status();
        GameMatchDTO gameMatchDTO = getDTOById(gameMatchId);
        PlayerDTO player1DTO = gameMatchDTO.getPlayerOne();
        PlayerDTO player2DTO = gameMatchDTO.getPlayerTwo();

        if (gameMatchDTO.getReason() == MATCH_REASON.LADDER) {
            handleLadderResult(player1DTO, player2DTO, status);
        } else if (gameMatchDTO.getReason() == MATCH_REASON.VALIDATION) {
            SubmissionDTO submission1DTO = gameMatchDTO.getSubmissionOne();
            handleValidationResult(player1DTO, submission1DTO);
        }
        setGameMatchStatus(gameMatchId, status);
    }

    public void setGameMatchStatus(Long gameMatchId, MATCH_STATUS status) {
        GameMatch gameMatch = gameMatchRepository.findById(gameMatchId).get();
        gameMatch.setStatus(status);
        gameMatchRepository.save(gameMatch);
    }

    private void handleLadderResult(PlayerDTO player1DTO, PlayerDTO player2DTO, MATCH_STATUS status) {
        // make this cleaner
        EloChanges eloChanges = eloCalculator.calculateElo(player1DTO, player2DTO, status);
        if (status == MATCH_STATUS.PLAYER_ONE_WIN) {
            playerService.updatePlayerAfterLadderMatch(player1DTO, eloChanges.getPlayer1Change(), true, false);
            playerService.updatePlayerAfterLadderMatch(player2DTO, eloChanges.getPlayer2Change(), false, false);
        } else if (status == MATCH_STATUS.PLAYER_TWO_WIN) {
            playerService.updatePlayerAfterLadderMatch(player1DTO, eloChanges.getPlayer1Change(), false, false);
            playerService.updatePlayerAfterLadderMatch(player2DTO, eloChanges.getPlayer2Change(), true, false);
        } else if (status == MATCH_STATUS.DRAW) {
            playerService.updatePlayerAfterLadderMatch(player1DTO, eloChanges.getPlayer1Change(), false, true);
            playerService.updatePlayerAfterLadderMatch(player2DTO, eloChanges.getPlayer2Change(), false, true);
        }
    }

    private  void handleValidationResult(PlayerDTO playerDTO, SubmissionDTO submissionDTO) {
        submissionService.validateSubmissionAfterMatch(submissionDTO.id());
        playerService.setCurrentSubmissionIfNone(playerDTO.getId(), submissionDTO.id());
    }


    }


