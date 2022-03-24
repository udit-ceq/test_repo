import json
import sys
import requests
import os
from base64 import b64encode
from nacl import encoding, public
from requests.auth import HTTPBasicAuth





token = os.environ['GH_TOKEN']
owner = "udit-ceq"
repo = "test_repo"

tool = sys.argv[1]
org = sys.argv[2]
team_name = sys.argv[3]
env = sys.argv[4]
aws_account = sys.argv[5]



SONAR_TEAM_NAME = os.environ['SONAR_TEAM_NAME']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
PRISMA_TOKEN = os.environ['PRISMA_TOKEN']



#secret_name= "GH_TOKEN"
#secret_value = "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"

def add_token_to_github_secret(secret_name, secret_value):
  url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/public-key"
  response = requests.get(url, headers={
    "Content-Type": "application/json",
    "Authorization": "token " + token
  })
  print(url)
  print(response.json())
  if(response.status_code == 200):
    data = response.json()
    encoded_value = encryptSecret(data['key'], secret_value)
    print(encoded_value)
    url = "https://api.github.com/repos/{}/{}/actions/secrets/{}".format(owner,repo, secret_name)
    print(url)
    resp = requests.put(url, headers={
				"Content-Type": "application/json",
				"Authorization": "token " + token
			},
        data=json.dumps({
                'encrypted_value': encoded_value,
                "key_id" : data['key_id']
			}))
    print(resp)
    
    
    
def encryptSecret(public_key, secret_value):
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")



if (tool =="sonarqube"):
    secrets={"{}_SONARQUBE_HOST": "https://sonarqube.mcd.com", "{}_SONARQUBE_TOKEN":SONAR_TEAM_NAME}
    for secret_name,secret_value in secrets.items():
        add_token_to_github_secret(secret_name.format(team_name), secret_value)

elif (tool =="aws"):
    secrets={"{}_AWS_GITHUB_{}_{}_ACCESS_KEY_ID": AWS_ACCESS_KEY, "{}_AWS_GITHUB_{}_{}_SECRET_KEY":AWS_SECRET_KEY}
    for secret_name,secret_value in secrets.items():
        add_token_to_github_secret(secret_name.format(team_name,aws_account,env), secret_value)
