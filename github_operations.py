# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:32:30 2022

@author: 91798
"""
import json
import requests
import os
import sys


BASE_URL = "https://api.github.com/"

token = os.environ['GH_TOKEN']

owner = "udit-ceq"
repo = "test_repo"


tool = sys.argv[1]
team_name = sys.argv[2]
env = sys.argv[3]
aws_account = sys.argv[4]


def list_commits(owner, repo):
    uri = BASE_URL + "repos/" + owner + "/" + repo + "/commits"
    req = requests.get(uri, auth=(token, ''))
    return req.json()


print(list_commits(owner,repo))


def create_repo_project(owner, repo_name, project_name):
    uri = BASE_URL + "repos/" + owner + "/" + repo_name + "/projects"
    data = {"name": project_name}
    body = json.dumps(data)
    req = requests.post(uri, data=body, auth=(token, ''))
    return req.json()


print(create_repo_project(owner,repo, "project_three"))


