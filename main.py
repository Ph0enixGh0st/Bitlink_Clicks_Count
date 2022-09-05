
import json
import os
from urllib.parse import urlparse

import argparse
import requests
from dotenv import load_dotenv


def check_bitlink(link, token):

    headers = {"Authorization": "Bearer {}".format(token)}
    bitlink = urlparse(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}"
    response = requests.get(url, headers=headers)

    return response.ok


def get_clicks_stats(bitlink, token):

    bitlink = urlparse(bitlink)
    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {"unit": "month", "units": "-1"}
    clicks_count = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary",
        params=payload,
        headers=headers)
    #return (f"{bitlink.netloc}{bitlink.path}", clicks_count.text)
    #print(bitlink)
    #print(clicks_count.text)
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


def main():

    load_dotenv()
    
    token = os.environ['BITLINK_TOKEN']

    parser = argparse.ArgumentParser(
    description='The program shortens user provided link and shows bitlink clicks statistics'
    )
    parser.add_argument("link", help='Your link or bitlink here')
    args = parser.parse_args()
    
    link = args.link

    if not check_bitlink(link, token):
        full_bitlink = print_bitlink(link, token)#, output_clicks# 
        print(f"Битлинк ", full_bitlink)
        
    else:
        output_clicks = get_clicks_stats(link, token)
        print(output_clicks)


if __name__ == '__main__':
    main()
