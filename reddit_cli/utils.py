from typing import Dict
import requests


def get_api_response_post(url: str, headers: Dict) -> Dict:
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response_headers = response.headers
        if "retry-after" in response_headers.keys():
            print(f"Retry after {response_headers['retry-after']}")
        raise Exception(e)

    return response.json()
