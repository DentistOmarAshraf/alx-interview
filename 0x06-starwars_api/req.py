#!/usr/bin/env python3
"""
The Task in python3
"""

from sys import argv
import requests


if len(argv) != 2:
    print("Usage:")
    print("./req <actor_id>")
    exit(1)

actor_id = argv[1]
res = requests.get(f"https://swapi-api.alx-tools.com/api/films/{actor_id}/")

data = res.json()["characters"]

for url in data:
    res = requests.get(url)
    print(res.json()["name"])
