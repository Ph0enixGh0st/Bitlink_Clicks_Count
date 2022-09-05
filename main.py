
import json
import os
from urllib.parse import urlparse

import argparse
import requests
from dotenv import load_dotenv


def is_bitlink(link, token):

    headers = {"Authorization": "Bearer {}".format(token)}
    bitlink = urlparse(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}"
    response = requests.get(url, headers=headers)

    return response.ok


def count_clicks(bitlink, token):

    bitlink = urlparse(bitlink)
    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {"unit": "month", "units": "-1"}
    clicks_summary = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary",
        params=payload,
        headers=headers)
    stats = clicks_summary.json()
    return stats["total_clicks"]


def make_bitlink(link, token):

    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {
        "long_url": link,
    }
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(url, json=payload, headers=headers)
    created_bitlink = response.json()

    return created_bitlink["link"]


def main():

    load_dotenv()
    
    token = os.environ['BITLINK_TOKEN']

    parser = argparse.ArgumentParser(
    description='The program shortens user provided link and shows bitlink clicks statistics'
    )
    parser.add_argument("link", help='Your link or bitlink here')
    args = parser.parse_args()
    
    link = args.link

    if not is_bitlink(link, token):
        full_bitlink = make_bitlink(link, token)#, output_clicks# 
        print(f"Битлинк ", full_bitlink)
        
    else:
        output_clicks = count_clicks(link, token)
        print(f"Количество кликов по битлинку:", output_clicks)


if __name__ == '__main__':
    main()