package com.example.botfightwebserver.gameMatch;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.PrePersist;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;
import java.time.LocalDateTime;

enum MATCH_STATUS {
    WAITING,
    IN_PROGRESS,
    FAILED,
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
    private Long id;

    @Column(name = "player_one_id")
    private Long playerOneId;

    @Column(name = "player_two_id")
    private Long playerTwoId;

    @Enumerated(EnumType.STRING)
    private MATCH_STATUS status;

    private LocalDateTime createdAt;
    private LocalDateTime processedAt;
    private String queueMessageId;

    @PrePersist
    public void onCreate() {
        createdAt = LocalDateTime.now();
        if (status == null) {
            status = MATCH_STATUS.WAITING;
        }
    }
}

