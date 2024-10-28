package com.example.botfightwebserver.gameMatch;

import com.example.botfightwebserver.player.Player;
import com.example.botfightwebserver.player.PlayerRepository;
import com.example.botfightwebserver.player.PlayerService;
import com.example.botfightwebserver.submission.Submission;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Transactional
@RequiredArgsConstructor
public class GameMatchService {

    private final GameMatchRepository gameMatchRepository;
    private final PlayerService playerService;

    public List<GameMatch> getGameMatches() {
        return gameMatchRepository.findAll();
    }

    public GameMatch createMatch(Long player1Id, Long player2Id) {
        playerService.validatePlayers(player1Id, player2Id);
        GameMatch gameMatch = new GameMatch();
        gameMatch.setPlayerOne(playerService.getPlayerReferenceById(player1Id));
        gameMatch.setPlayerTwo(playerService.getPlayerReferenceById(player2Id));
        gameMatch.setStatus(MATCH_STATUS.WAITING);
        return gameMatchRepository.save(gameMatch);
    }
}


