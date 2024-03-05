import requests

from utils.logger import logger


def send_get_request(url):
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
