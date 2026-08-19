package com.example;

import java.util.Arrays;

public class OrderSummary {
    public int calculateFinalScore(int[] scores, int passMark) {
        int total = 0;

        for (int index = 0; index < scores.length; index++) {
            if (scores[index] >= passMark) {
                total += scores[index];
            } else {
                total += scores[index] / 2;
            }
        }

        if (total >= 100) {
            return total + 10;
        }

        return total;
    }

    public static void main(String[] args) {
        OrderSummary summary = new OrderSummary();
        int[] scores = {12, 20, 30, 85, 50};
        int result = summary.calculateFinalScore(scores, 30);

        System.out.println("Scores=" + Arrays.toString(scores));
        System.out.println("Final score=" + result);
    }
}
