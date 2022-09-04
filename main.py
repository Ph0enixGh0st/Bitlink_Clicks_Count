
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


def get_clicks_stats(bitlink, token):

    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {"unit": "month", "units": "-1"}
    clicks_count = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        params=payload,
        headers=headers)
    return clicks_count.text


def make_bitlink(link, token):

    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {
        "long_url": link,
    }
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(url, json=payload, headers=headers)
    created_bitlink = response.json()

    return created_bitlink["link"]


def print_bitlink_stats(link, token):

    bitlink = make_bitlink(link, token)
    full_bitlink = bitlink
    bitlink = urlparse(bitlink)

    return full_bitlink, get_clicks_stats(f"{bitlink.netloc}{bitlink.path}", token)


def given_bitlink_stats(link, token):

    link = urlparse(link)

    return get_clicks_stats(f"{link.netloc}{link.path}", token)


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
        full_bitlink, output_clicks = print_bitlink_stats(link, token)
        print(f"Битлинк ", full_bitlink)
        
    else:
        output_clicks = given_bitlink_stats(link, token)
        print(output_clicks)


if __name__ == '__main__':
    main()