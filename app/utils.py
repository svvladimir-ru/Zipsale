import os
import requests
from dotenv import load_dotenv
load_dotenv()
import pprint


pp = pprint.PrettyPrinter(indent=4)
params = {
    "Authorization": f"Bearer {os.environ.get('Authorization')}",
    'Accept': 'application/vnd.github.v3.star+json',
}


def get_json(url):
    r = requests.get(url=url, headers=params)
    return r


def parser(username):
    """Парсер данный по api github. На вход принимает username,
    получает все репозитории, далее проходит циклом по репозиториям,
    собирает их имя, количество звезд, и ссылку, в первом цикле получаем данные
    api pull request и передает их во второй цикл. Во втором цикле собирает pull requests репозитория
    и количество коментариев к каждому pull requests. """
    url_repos = f'https://api.github.com/users/{username}/repos'
    repos = get_json(url_repos).json()
    e = []
    for i in repos:
        url_pulls = f'https://api.github.com/repos/{username}/{i["name"]}/pulls?state=all'
        pulls = get_json(url_pulls).json()
        url_pull = []
        for pulls_number in pulls:
            url_pulls_number = f'https://api.github.com/repos/{username}/{i["name"]}/pulls/{pulls_number["number"]}'
            comment = get_json(url_pulls_number).json()
            url_pull.append({
                'url': pulls_number['html_url'],
                'comments_count': comment['comments'],
            })
        if len(url_pull) > 0:
            e.append(
                {
                    'description': i['name'],
                    'html_url': i['html_url'],
                    'stargazers_count': i['stargazers_count'],
                    'url_pulls': url_pull,
                }
            )

    return e
