package com.example.botfightwebserver.player;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PlayerService {

    @Autowired
    private PlayerRepository playerRepository;

    public List<Player> getPlayers() {
        return playerRepository.findAll();
    }

    public Player getPlayerReferenceById(Long id) {
        return playerRepository.getReferenceById(id);
    }

    public Player createPlayer(String name, String email) {
        if (playerRepository.existsByEmail(email)) {
            throw new IllegalArgumentException("Player with email " + email + " already exists");
        }
        Player player = new Player();
        player.setName(name);
        player.setEmail(email);
        return playerRepository.save(player);
    }

    public void validatePlayers(Long player1Id, Long player2Id) {
        if (!playerRepository.existsById(player1Id) || !playerRepository.existsById(player2Id)) {
            throw new IllegalArgumentException("One or both players do not exist");
        }
        if (player1Id.equals(player2Id)) {
            throw new IllegalArgumentException("Players must be different");
        }
    }
}


