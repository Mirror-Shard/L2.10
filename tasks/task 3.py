#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Печатает введённое название компании и персонал
"""


# Вывод информации о компании
def list(company, **staff):

    print(f"\nНазвание компании: {company}")

    for post, workers in staff.items():
        print(f"{post} : {workers}")


if __name__ == '__main__':
    name = input("Введите название компании: ")
    list(name, Антошка="Директор", Василевс="Программист", Святополк="Уборщик")

