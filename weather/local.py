#!usr/bin/env python

import os
import sys
import json

import requests
from dotenv import load_dotenv


def get_key() -> str:
    api_key = os.getenv("APIXU_KEY")
    return api_key


def get_weather(url: str, key: str, query: str):
    payload = {'key': key, 'q': query}
    r = requests.get(url, params=payload)
    data = r.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    dotenv_path = os.path.join('..', '.env')
    print(dotenv_path)
    load_dotenv(dotenv_path=dotenv_path)
