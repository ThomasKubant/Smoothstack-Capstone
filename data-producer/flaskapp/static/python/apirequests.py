import requests
import json

########################
###  POST  Functions ###
########################

applications_url = "http://localhost:8071/applications"
registration_url = "http://localhost:8070/users/registration"
login_url = "http://localhost:8070/login"

# Requires bearer token
bank_url = "http://localhost:8083/banks"
branch_url = "http://localhost:8083/branches"
transaction_url = "http://localhost:8073/transactions"

### Unprotected routes ###
def application_post(application, header):
    response = requests.post(applications_url, json=application, headers=header)
    return json.loads(response.text)

def user_post(user, header):
    response = requests.post(registration_url, json=user, headers=header)
    return json.loads(response.text)

def user_login(user, header):
    response = requests.post(login_url, json={"username": user["username"], "password": user["password"]}, headers=header)
    return response.headers

### Protected routes ###
def bank_post(bank, authenticated_header):
    response = requests.post(bank_url, json=bank, headers=authenticated_header)
    return json.loads(response.text)

def branch_post(branch, authenticated_header):
    response = requests.post(branch_url, json=branch, headers=authenticated_header)
    return json.loads(response.text)

def transaction_post(transaction, authenticated_header):
    response = requests.post(transaction_url, json=transaction, headers=authenticated_header)
    return json.loads(response.text)

