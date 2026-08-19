package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OrderSummaryTest {

    private final OrderSummary orderSummary = new OrderSummary();

    @Test
    void shouldUseLowerHalfForScoresBelowPassMark() {
        int[] scores = {10, 25, 40};

        int result = orderSummary.calculateFinalScore(scores, 30);

        assertEquals(5 + 12 + 40, result);
    }

    @Test
    void shouldUseFullScoreForScoresAtOrAbovePassMark() {
        int[] scores = {30, 50, 20};

        int result = orderSummary.calculateFinalScore(scores, 30);

        assertEquals(30 + 50 + 10, result);
    }

    @Test
    void shouldAddBonusWhenTotalReachesThreshold() {
        int[] scores = {50, 30, 40};

        int result = orderSummary.calculateFinalScore(scores, 30);

        assertEquals(120 + 10, result);
    }

    @Test
    void shouldReturnTotalWithoutBonusWhenBelowThreshold() {
        int[] scores = {10, 20, 25};

        int result = orderSummary.calculateFinalScore(scores, 30);

        assertEquals(5 + 10 + 12, result);
    }
}
