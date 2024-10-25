package com.example.botfightwebserver.player;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/v1/player")
public class PlayerController {

    @Autowired
    private PlayerService playerServiceService;

    public List<Player> getPlayers() {
        return playerServiceService.getPlayers();
    }
}
