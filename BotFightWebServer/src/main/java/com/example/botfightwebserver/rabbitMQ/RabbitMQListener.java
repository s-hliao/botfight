package com.example.botfightwebserver.rabbitMQ;

import com.example.botfightwebserver.gameMatch.GameMatchResult;
import com.example.botfightwebserver.gameMatch.GameMatchService;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RabbitMQListener {

    private final GameMatchService gameMatchService;

    @RabbitListener(queues = RabbitMQConfiguration.GAME_MATCH_RESULTS)
    public void receiveGameMatchResults(GameMatchResult gameMatchResult) {
        gameMatchService.handleGameMatchResult(gameMatchResult);
    }
}