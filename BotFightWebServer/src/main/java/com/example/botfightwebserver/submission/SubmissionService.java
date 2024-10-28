package com.example.botfightwebserver.submission;

import com.example.botfightwebserver.player.Player;
import com.example.botfightwebserver.player.PlayerRepository;
import com.example.botfightwebserver.storage.StorageService;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
@RequiredArgsConstructor
@Transactional
public class SubmissionService {

    private final SubmissionRepository submissionRepository;
    private final StorageService storageService;

    private static final long MAX_FILE_SIZE = 50 * 1024 * 1024;
    private final PlayerRepository playerRepository;

    public SubmissionDTO createSubmission(Long playerId, MultipartFile file) {
        validateFile(file);

        Player player = playerRepository.getReferenceById(playerId);
        String fileIdentifierString = storageService.uploadFile(file);

        Submission submission = new Submission();
        submission.setPlayer(player);
        submission.setStorageHash(fileIdentifierString);
        submission.setSubmissionValidity(SUBMISSION_VALIDITY.NOT_EVALUATED);

        // Can be optimized if we create the DTO just using the playerID
        return SubmissionDTO.fromEntity(submissionRepository.save(submission));
    }
    public void validateFile(MultipartFile file) {
        if (file.isEmpty()) {
            throw new IllegalArgumentException("File is empty");
        }

        if (file.getSize()  > MAX_FILE_SIZE) {
            throw new IllegalArgumentException("File is too large");
        }

        String contentType = file.getContentType();
        if (contentType == null || !contentType.equals("application/zip")) {
            throw new IllegalArgumentException("Unsupported content type: only zip files allowed");
        }
    }

    // before overwriting the whatever the current submission is for a player, check theri current submission created time and make sure the new submisson
    // has a created time that is after.

}
