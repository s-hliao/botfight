package com.example.botfightwebserver.storage;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public interface StorageService {
    public String uploadFile(Long playerId, MultipartFile file);

    public void verifyAccess();
}
