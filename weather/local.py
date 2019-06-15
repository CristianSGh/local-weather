#!usr/bin/env python

import os
import sys
import json

import requests

# URLs
# Base: http://api.apixu.com/v1
# Current weather: http://api.apixu.com/v1/current.json?key=...&q=...


def get_urls():
    with open('vars.json') as f:
        urls = json.load(f)
        return urls


def get_key() -> str:
    with open('keys.json') as f:
        data = json.load(f)
        api_key = data['apixu']
        return api_key


def get_weather(url: str, key: str, query: str):
    payload = {'key': key, 'q': query}
    r = requests.get(url, params=payload)
    data = r.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    api_key = get_key()
    # print(api_key)
    urls = get_urls()
    # print(urls)
    get_weather(urls['apixu_current'], api_key, 'Bucharest')
