package com.example.botfightwebserver.player;

import com.example.botfightwebserver.submission.Submission;
import com.example.botfightwebserver.submission.SubmissionDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class PlayerDTO {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime creationDateTime;
    private LocalDateTime lastModifiedDate;
    private Double elo;
    private Integer matchesPlayed;
    private Integer numberWins;
    private Integer numberLosses;
    private Integer numberDraws;
    private SubmissionDTO currentSubmissionDTO;

    public static PlayerDTO fromEntity(Player player) {
        return PlayerDTO.builder()
            .id(player.getId())
            .name(player.getName())
            .email(player.getEmail())
            .creationDateTime(player.getCreationDateTime())
            .lastModifiedDate(player.getLastModifiedDate())
            .elo(player.getElo())
            .matchesPlayed(player.getMatchesPlayed())
            .numberWins(player.getNumberWins())
            .numberLosses(player.getNumberLosses())
            .numberDraws(player.getNumberDraws())
            .currentSubmissionDTO(SubmissionDTO.fromEntity(player.getCurrentSubmission()))
            .build();
    }
}
