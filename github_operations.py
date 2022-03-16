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

owner = sys.argv[1]
repo = sys.argv[2]


def list_commits(owner, repo):
    uri = BASE_URL + "repos/" + owner + "/" + repo + "/commits"
    req = requests.get(uri, auth=(token, ''))
    return req.json()


print(list_commits("pinkesh-ceq", "First-repo"))


def create_repo_project(owner, repo_name, project_name):
    uri = BASE_URL + "repos/" + owner + "/" + repo_name + "/projects"
    data = {"name": project_name}
    body = json.dumps(data)
    req = requests.post(uri, data=body, auth=(token, ''))
    return req.json()


print(create_repo_project("pinkesh-ceq", "First-repo", "project_three"))

