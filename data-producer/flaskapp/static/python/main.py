import producers
import apirequests

header = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

auth_header = {
    'Content-type':'application/json',
    'Accept':'application/json',
    'Authorization': ''
}
def create_admin():
    admin = producers.generate_admin()
    apirequests.user_post(admin, header)
    admin_response = apirequests.user_login(admin, header)
    auth_header['Authorization'] = admin_response['Authorization']
    print(admin_response)

def create_banks():
    bank_count = int(input("How many banks would you like to generate?\n"))
    for _ in range(bank_count):
        bank = producers.generate_bank()
        bank_response = apirequests.bank_post(bank, auth_header)
        print("Bank = " + str(bank))
        print("Bank Response = " + str(bank_response))
        branch = producers.generate_branch(bank_response['id'])
        branch_response = apirequests.branch_post(branch, auth_header)
        print("branch = " + str(branch))
    print("branch Response = " + str(branch_response))


def create_branches(count):
    for _ in range(count):
        branch = producers.generate_branch()

def create_applications():
    application_count = int(input("How many applicants would you like to create?\n"))
    for _ in range(application_count):
        application = producers.generate_application()
        application_response = apirequests.application_post(application, header)
        create_transactions(application_response)
        member = producers.generate_member(application_response)
        apirequests.user_post(member, header)
        print("application = " + str(application))
        print("application Response = " + str(application_response))

def create_transactions(application_response):
    if "createdAccounts" in application_response:
        account_number = application_response["createdAccounts"][0]["accountNumber"]
        deposit = producers.generate_transaction(account_number, 5000000)
        transaction = producers.generate_transaction(account_number)
        deposit_response = apirequests.transaction_post(deposit, auth_header)
        transaction_response = apirequests.transaction_post(transaction, auth_header)
        print("Deposit: " + str(deposit_response))
        print("Transaction: " + str(transaction_response))
create_admin()
create_applications()
create_banks()
create_transactions()