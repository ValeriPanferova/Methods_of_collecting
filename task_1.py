import requests
import sys
import json

_USERNAME = 'ValeriPanferova'


def _main():
    api_path = f'https://api.github.com/users/{_USERNAME}/repos'
    req = requests.get(api_path)
    with open('json_request.json', 'w', encoding='UTF-8') as f_obj:
        json.dump(req.json(), f_obj)


if __name__ == '__main__':
    sys.exit(_main())
