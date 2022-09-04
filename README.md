# Bitlink Clicks Count

The script shortens user provided links or displays the shortened link clicks statistics.

## Environment

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables

- BITLINK_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
BITLINK_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
#### How to get
* Register an application [API Bitly]
(https://app.bitly.com/settings/api/) and get the `Bitlink Token`:
![token screen](https://user-images.githubusercontent.com/108229516/187847564-ce5cadd6-e2ad-4018-80a9-8e85d3c8dd3f.jpg)


## Run

Launch on Linux(Python 3) or Windows:

```bash

$ python main.py http://dvmn.org

```

You will see:
```
Битлинк  https://bit.ly/3B6xNAE
```

Launch on Linux(Python 3) or Windows:

```bash

$ python main.py https://bit.ly/3B6xNAE

```

You will see:
```
{"unit_reference":"2022-08-29T08:01:36+0000","total_clicks":0,"units":1,"unit":"month"}
```
