import json
import sys
import requests
import os
from base64 import b64encode
from nacl import encoding, public
from requests.auth import HTTPBasicAuth




base_url = "https://api3.prismacloud.io/"

team_name = sys.argv[1]
orgs = sys.argv[2]

def prismaLogin():
    username = os.environ['PRISMA_ACCESS_KEY']
    password = os.environ['PRISMA_SECRET_KEY']
    prismaId = os.environ['PRISMA_ID']


    payload = {
        "username": username,
        "password": password,
        "prismaId": prismaId,
    }
    headers = {"content-type": "application/json; charset=UTF-8"}
    url = base_url+"login"
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    #print(response.json())
    return response.json()["token"]




JWT_token = prismaLogin()
#print(JWT_token)


def addPrismaUserRole():
    role_names = ["{}-Prisma_Admin", 
                  "{}-Prisma_ComputeAccess", 
                  "{}-Prisma_ComputeCI", 
                  "{}-Prisma_DefenderManager", 
                  "{}-Prisma_Developer", 
                  "{}-Prisma_Readonly"]


    role_type = ["Account Group Admin", 
                 "Account and Cloud Provisioning Admin", 
                 "Build and Deploy Security", 
                 "Cloud Provisioning Admin", 
                 "Developer", 
                 "Account Group Read Only"]


    role_description = ["Account Group Admin", 
                        "ACCOUNT AND CLOUD PROVISIONING ADMIN, AUDITOR", 
                        "CI,BUILD AND DEPLOY SECURITY",
                        " ", 
                        "Allow to scan IAC code in IDE or CI/CD pipeline", 
                        "ACCOUNT GROUP READ ONLY DEVSECOPS"]



    restrictDismissalAccess = [False, False, True, True, True, True]
    
    url = base_url+"user/role"
    for i in range(len(role_names)):
        payload = {
            "accountGroupIds": [],
            "resourceListIds": [],
            "description": role_description[i],
            "name": role_names[i].format(team_name),
            "roleType": role_type[i],
            "additionalAttributes": {
                "hasDefenderPermissions": False,
                "onlyAllowCIAccess": False,
                "onlyAllowComputeAccess": False
       },
            "restrictDismissalAccess": restrictDismissalAccess[i]
        }
        headers = {
            "content-type": "application/json",
            "x-redlock-auth": JWT_token
        }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        
        print(response)
    return response.text



def getListOfRoles():
    
    url = base_url+"user/role/name"
    headers = {"x-redlock-auth": JWT_token}

    response = requests.request("GET", url, headers=headers)

    return response.json()


def getRoleIds():
    role_ids = []
    svc_user_role_names = ["{}-Prisma_ComputeCI", "{}-Prisma_DefenderManager", "{}-Prisma_Developer"]
    all_roles = getListOfRoles()
    for svc_user_role in svc_user_role_names:
        for role in all_roles:
            if(svc_user_role.format(team_name) == role["name"]):
                role_ids.append(role["id"])
                
    print(role_ids)
    return role_ids
        


def addAccessKey(accessKeyName,serviceAccountName):
    
    url = base_url + "access_keys"
    
        
    payload = {
        "expiresOn": 0,
        "name": accessKeyName,
        "serviceAccountName": serviceAccountName
    }
    headers = {
        "content-type": "application/json",
        "x-redlock-auth": JWT_token
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print(response)
    




def addPrismaSvcUser():
    list_accees_secret_keys=[]
    url = base_url+"v3/user"
    all_svc_user_role_ids = getRoleIds()
    svc_user_role_names = ["{}-Prisma_ComputeCI", "{}-Prisma_DefenderManager", "{}-Prisma_Developer"]
    Username = ["{}-Prisma-ComputeCI-Svc", "{}-Prisma-DefenderManager-Svc", "{}-Prisma-Developer-Svc"]
    accessKeyName = ["{}-prisma-computeci-access-keys", "{}-prisma-defendermanager-access-keys", "{}-prisma-developer-access-keys"]
    
    
    for i in range(len(svc_user_role_names)):
        
        payload = {
            "accessKeyName": accessKeyName[i].format(team_name.lower()),
            "accessKeysAllowed": True,
            "defaultRoleId": all_svc_user_role_ids[i],
            "timeZone": "Asia/Calcutta",
            "type": "SERVICE_ACCOUNT",
            "username": Username[i].format(team_name)
        }
        
        headers = {
            "content-type": "application/json",
            "x-redlock-auth": JWT_token
        }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.json())
        list_accees_secret_keys.append(response.json())
    return list_accees_secret_keys

addPrismaUserRole()

list_accees_secret_keys = addPrismaSvcUser()
print(list_accees_secret_keys)





secrets={"{}_PRISMA_COMPUTECI_ACCESS_KEY".format(team_name): list_accees_secret_keys[0]["id"], 
         "{}_PRISMA_COMPUTECI_SECRET_KEY".format(team_name):list_accees_secret_keys[0]["secretKey"], 
         "{}_PRISMA_DEFENDERMANAGER_ACCESS_KEY".format(team_name): list_accees_secret_keys[1]["id"], 
         "{}_PRISMA_DEFENDERMANAGER_SECRET_KEY".format(team_name): list_accees_secret_keys[1]["secretKey"],
         "{}_PRISMA_IACSCAN_KEYS".format(team_name):"{}::{}".format(list_accees_secret_keys[2]["id"],list_accees_secret_keys[2]["secretKey"])
         }

print(secrets)

token = os.environ['GH_TOKEN']#"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"







def add_token_to_github_secret(secret_name, secret_value):
  #url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/public-key"
  url = f"https://api.github.com/orgs/{orgs}/actions/secrets/public-key"
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
    url = "https://api.github.com/orgs/{}/actions/secrets/{}".format(orgs, secret_name)
    print(url)
    resp = requests.put(url, headers={
				"Content-Type": "application/json",
				"Authorization": "token " + token
			},
        data=json.dumps({
                "org": orgs,
				"secret_name": secret_name,
				"visibility": "selected",
                'encrypted_value': encoded_value,
                "key_id" : data['key_id']
			}))
    print(resp.json())
    
    
    
def encryptSecret(public_key, secret_value):
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")





for secret_name,secret_value in secrets.items():
    add_token_to_github_secret(secret_name.format(team_name), secret_value)







