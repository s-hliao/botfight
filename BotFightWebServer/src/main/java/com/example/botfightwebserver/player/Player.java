package com.example.botfightwebserver.player;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.PrePersist;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.CreationTimestamp;
import org.springframework.data.annotation.LastModifiedBy;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Builder
public class Player {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    @CreationTimestamp
    private LocalDateTime creationDateTime;
    @LastModifiedBy
    private LocalDateTime lastModifiedDate;
    @Builder.Default
    private Double elo=1200.0;
    @Builder.Default
    private Integer matchesPlayed=0;
    @Builder.Default
    private Integer numberWins=0;
    @Builder.Default
    private Integer numberLosses=0;
    private Long currentSubmissionId;

    @PrePersist
    private void onCreate() {
        creationDateTime = LocalDateTime.now();
        lastModifiedDate = LocalDateTime.now();
    }
}
