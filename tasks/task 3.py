#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создающёт компанию, которая состоит из названия и персонала,
где персонал это словарь – состоящий из постов и сотрудников
"""


# Создаёт компанию с названием и персоналом
def new():

    # Персонал компании
    staff = {}

    # Название компании
    name = str(input("\nНазвание компании: "))

    # Организовать бесконечный цикл запроса команд.
    while True:

        # Запросить команду из терминала.
        print("Введите add чтобы добавить должность и работников")
        print("Или введите done если компания готова")
        command = input(">>> ").lower()

        # Добавляет должность, и сотрудников в эту должность
        if command == "add":

            post = str(input("Введите название должности: "))
            workers = input("Введите имена сотрудников через пробел: ").split()
            staff[post] = workers

        # Или заканчивает создание компании
        elif command == "done":
            return name, staff

        else:
            print("! Команда не опознана !")


# Вывод информации о компании
def list(company, **staff):

    print(f"\nНазвание компании: {company}")

    for post, workers in staff.items():
        print(f"{post} : {workers}")


if __name__ == '__main__':

    # Организовать бесконечный цикл запроса команд.
    while True:

        print("\nnew - создать компанию, list - вывести информацию о компании")

        # Запросить команду из терминала.
        command = input(">>> ").lower()

        if command == "new":
            name, staff = new()

        elif command == "list":
            list(name, **staff)

        else:
            print("! Команда не опознана !")
