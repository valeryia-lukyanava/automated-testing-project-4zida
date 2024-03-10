import requests

from utils.logger import logger


def send_get_request(url: str):
    response = None
    try:
        response = requests.get(url=url,
                                headers={"IC-Bypass-Throttling": "8f190c31363e1d3a08ec0ccd0eed4be4"},
                                timeout=30)
        logger.info(f"GET '{url}'. Response status code: {response.status_code}")
        if int(response.status_code) == 429:
            send_get_request(url)
    except ConnectionError:
        logger.info(f"GET '{url}': ConnectionError")
        send_get_request(url)
    except TimeoutError:
        logger.info(f"GET '{url}': TimeoutError")
        send_get_request(url)
    return response


def send_delete_request(url: str, x_api_key: str):
    response = None
    try:
        response = requests.delete(url=url,
                                   headers={"X-API-Key": x_api_key},
                                   timeout=30)
        logger.info(f"DELETE '{url}'. Response status code: {response.status_code}")
    except ConnectionError:
        logger.info(f"DELETE '{url}': ConnectionError")
        send_delete_request(url, x_api_key)
    except TimeoutError:
        logger.info(f"DELETE '{url}': TimeoutError")
        send_delete_request(url, x_api_key)
    return response
