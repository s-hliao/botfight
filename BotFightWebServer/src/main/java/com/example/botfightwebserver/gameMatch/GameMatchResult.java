package com.example.botfightwebserver.gameMatch;

import java.io.Serializable;

public record GameMatchResult(Long matchId, int winner) implements Serializable {
}
