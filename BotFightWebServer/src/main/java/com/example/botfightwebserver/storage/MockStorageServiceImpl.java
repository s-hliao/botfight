package com.example.botfightwebserver.storage;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

@Service
public class MockStorageServiceImpl implements  StorageService {
    public String uploadFile(Long playerId, MultipartFile file) {
        if (file == null || file.isEmpty()) {
            throw new IllegalArgumentException("File is null or empty");
        }
        String fileName = file.getOriginalFilename() != null ?
            file.getOriginalFilename() : "unknown";
        String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"));
        return String.format("PLAYER_%s/%s_%s",playerId, fileName, timestamp);
    }
}
