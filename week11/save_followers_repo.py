import requests
import json

# token
token = '$已注释'
username = "Zhouxzj"


# get followers
def get_followers(username):
    url = f"https://api.github.com/users/{username}/following"
    response = requests.get(url, auth=(username, token))
    followers = response.json()
    return followers


# get followers' repos
def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, auth=(username, token))
    repos = response.json()
    return repos


# save data
def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


followers = get_followers(username)

# get every follower`s repo
all_repos = []
for follower in followers:
    repos = get_repos(follower['login'])
    all_repos.extend(repos)

save_to_json_file(all_repos, 'followers_repos.json')