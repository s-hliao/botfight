package com.example.botfightwebserver.gameMatch;

import com.example.botfightwebserver.player.Player;
import com.example.botfightwebserver.player.PlayerRepository;
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
    private final PlayerRepository playerRepository;

    public List<GameMatch> getGameMatches() {
        return gameMatchRepository.findAll();
    }

    public GameMatch createMatch(Long player1Id, Long player2Id) {
        if (!playerRepository.existsById(player1Id) || !playerRepository.existsById(player2Id)) {
            throw new IllegalArgumentException("One or both players do not exist");
        }
        GameMatch gameMatch = new GameMatch();
        gameMatch.setPlayerOneId(player1Id);
        gameMatch.setPlayerTwoId(player2Id);
        gameMatch.setStatus(MATCH_STATUS.WAITING);
        return gameMatchRepository.save(gameMatch);

        //rabbit logic here with New rabbit service
    }

}
