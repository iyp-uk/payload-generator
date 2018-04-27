import datetime
import logging
import socket
from time import sleep
import os
import requests
from requests import RequestException


def create_payload():
    """
    Just creates a dict.
    :return: Dictionary representing a payload with some variables.
    """
    return dict(
        hostname=socket.gethostname(),
        ip=socket.gethostbyname(socket.gethostname()),
        time=str(datetime.datetime.now())
    )


def post_payload(endpoint):
    try:
        r = requests.post(endpoint, json=payload)
        r.raise_for_status()
    except RequestException as e:
        logging.error(e)


if __name__ == "__main__":
    endpoint = os.environ.get('POST_ENDPOINT', 'http://127.0.0.1:8080')
    while True:
        payload = create_payload()
        print(payload)
        post_payload(endpoint)
        sleep(1)
