package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OrderSummaryPathsTest {

    private final OrderSummary orderSummary = new OrderSummary();

    @Test
    void singleElementBelowAndAbove() {
        int[] below = {10};
        assertEquals(5, orderSummary.calculateFinalScore(below, 30));

        int[] at = {30};
        assertEquals(30, orderSummary.calculateFinalScore(at, 30));
    }

    @Test
    void multiElementMixedPaths_andExactThreshold() {
        // mixed branches that produce exactly 100 total before bonus
        int[] scores = {50, 30, 20};
        // calculation: 50 (>=30) + 30 (>=30) + 10 (20/2) = 90 -> no bonus
        assertEquals(50 + 30 + 10, orderSummary.calculateFinalScore(scores, 30));

        // create combination that leads to exactly 100
        int[] scores2 = {50, 50};
        // 50 + 50 = 100 -> bonus applied -> 110
        assertEquals(110, orderSummary.calculateFinalScore(scores2, 30));
    }
}
