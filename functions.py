import requests


def get_repos_stats(username):
    """ Собирает статистику по репозиториям заданного пользователя на GitHub. """
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()
