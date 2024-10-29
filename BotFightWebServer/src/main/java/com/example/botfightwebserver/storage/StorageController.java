package com.example.botfightwebserver.storage;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController()
@RequestMapping("/api/v1/storage")
@RequiredArgsConstructor
public class StorageController {

    @Qualifier("gcpStorageServiceImpl")
    private final StorageService storageService;

    @GetMapping("/verify")
    public ResponseEntity<String> verifyStorage() {
        storageService.verifyAccess();
        return ResponseEntity.ok("Can Access bucket");
    }
}