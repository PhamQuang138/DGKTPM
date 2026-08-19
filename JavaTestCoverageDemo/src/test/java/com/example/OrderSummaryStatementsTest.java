package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class OrderSummaryStatementsTest {

    private final OrderSummary orderSummary = new OrderSummary();

    @Test
    void coversLoopBranchesAndBonus_andEmpty() {
        // case: some below, some above, final total < 100
        int[] scores1 = {10, 25, 40};
        assertEquals(5 + 12 + 40, orderSummary.calculateFinalScore(scores1, 30));

        // case: some at or above, some below, final total < 100
        int[] scores2 = {30, 50, 20};
        assertEquals(30 + 50 + 10, orderSummary.calculateFinalScore(scores2, 30));

        // case: empty array -> total 0
        int[] empty = {};
        assertEquals(0, orderSummary.calculateFinalScore(empty, 30));
    }
}
