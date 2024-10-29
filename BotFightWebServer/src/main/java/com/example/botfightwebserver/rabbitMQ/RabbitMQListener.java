package com.example.botfightwebserver.rabbitMQ;

import com.example.botfightwebserver.gameMatch.GameMatchResult;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class RabbitMQListener {

    @RabbitListener(queues = RabbitMQConfiguration.GAME_MATCH_RESULTS)
    public void receiveGameMatchResults(GameMatchResult gameMatchResult) {
        //logic after receiving the result.
    }
}
