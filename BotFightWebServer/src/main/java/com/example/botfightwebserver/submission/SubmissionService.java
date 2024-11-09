package com.example.botfightwebserver.submission;

import com.example.botfightwebserver.player.Player;
import com.example.botfightwebserver.player.PlayerRepository;
import com.example.botfightwebserver.storage.MockStorageServiceImpl;
import com.example.botfightwebserver.storage.StorageService;
import jakarta.transaction.Transactional;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
@Transactional
public class SubmissionService {

    private final SubmissionRepository submissionRepository;
    private final StorageService storageService;
    private final PlayerRepository playerRepository;

    public SubmissionService(SubmissionRepository submissionRepository, @Qualifier("gcpStorageServiceImpl") StorageService storageService,
                             PlayerRepository playerRepository) {
        this.submissionRepository = submissionRepository;
        this.storageService = storageService;
        this.playerRepository = playerRepository;
    }

    private static final long MAX_FILE_SIZE = 50 * 1024 * 1024;

    public SubmissionDTO createSubmission(Long playerId, MultipartFile file) {
        validateFile(file);

        Player player = playerRepository.getReferenceById(playerId);
        String filePathString = storageService.uploadFile(playerId, file);

        Submission submission = new Submission();
        submission.setPlayer(player);
        submission.setStoragePath(filePathString);
        submission.setSubmissionValidity(SUBMISSION_VALIDITY.NOT_EVALUATED);

        // Can be optimized if we create the DTO just using the playerID
        return SubmissionDTO.fromEntity(submissionRepository.save(submission));
    }

    public Submission getSubmissionReferenceById(Long id) {
        return submissionRepository.getReferenceById(id);
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

    public void validateSubmissions(Long submission1Id, Long submission2Id) {
        if(!submissionRepository.existsById(submission1Id) || !submissionRepository.existsById(submission2Id)) {
            throw new IllegalArgumentException("Submission 1 or 2 does not exist");
        }
        if (submission1Id == submission2Id) {
            throw new IllegalArgumentException("Submission 1 is the same as submission 2");
        }
    }

    public void validateSubmissionAfterMatch(long submissionId) {
        Submission submission = submissionRepository.findById(submissionId).get();
        submission.setSubmissionValidity(SUBMISSION_VALIDITY.VALID);
        submissionRepository.save(submission);
    }
}
