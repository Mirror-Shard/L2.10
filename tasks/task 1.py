#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее геометрическое
своих аргументов a1, a2, ... an

Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


# Вычисляет среднее геометрическое
def mean(*n):

    if n:
        g = 1.0
        k = 1

        for i in n:
            g *= i * k
        g = g ** (1/len(n))

        return g
    else:
        return None


if __name__ == '__main__':

    print("Введите числа в массив через пробел: ")
    mas = list(map(float, input().split()))
    print(mean(*mas))
