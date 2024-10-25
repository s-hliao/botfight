package com.example.botfightwebserver.gameMatch;

import com.example.botfightwebserver.player.Player;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

enum MATCH_STATUS {
    WAITING,
    IN_PROGRESS,
    PLAYER_ONE_WIN,
    PLAYER_TWO_WIN
}

@Entity
@Table
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class GameMatch {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @ManyToOne
    @JoinColumn(name = "player_one_id")
    private Player playerOne;

    @ManyToOne
    @JoinColumn(name = "player_two_id")
    private Player playerTwo;

    @Enumerated(EnumType.STRING)
    private MATCH_STATUS status;

}

