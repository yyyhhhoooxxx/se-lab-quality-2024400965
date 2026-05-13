package com.example;

public class Calculator {
    // 加法
    public int add(int a, int b) {
        return a + b;
    }

    // 减法
    public int subtract(int a, int b) {
        return a - b;
    }

    // 乘法
    public int multiply(int a, int b) {
        return a * b;
    }

    // 除法
    public double divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为0");
        }
        return (double) a / b;
    }
}
