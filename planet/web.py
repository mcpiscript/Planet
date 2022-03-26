from urllib.request import urlopen
import requests


def get_versions() -> str:
    return str(
        urlopen(
            "https://gist.github.com/leha-code/3e8fea40346536b451e45fc1728ed250/raw/versions.json"
        ).read(),
        "UTF-8",
    )


def check_internet() -> bool:
    try:
        requests.head("http://www.google.com/")
        return True
    except requests.ConnectionError:
        return False
