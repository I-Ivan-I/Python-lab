#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for city_1 in sites:
    distances[city_1] = {}
    for city_2 in sites:
        x1, y1 = sites[city_1]
        x2, y2 = sites[city_2]
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances[city_1][city_2] = distance

print(distances)




