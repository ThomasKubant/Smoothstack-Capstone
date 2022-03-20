from faker import Faker
import random
import string
from datetime import datetime
import helpers

faker = Faker(['en-US'])


# # APPLICATIONS PRODUCER

def generate_application():
    types = ["CHECKING", "SAVINGS", "CHECKING_AND_SAVINGS", "CREDIT_CARD", "LOAN"]
    profile = faker.profile()
    address = faker.street_address()
    city = faker.city()
    state = faker.state_abbr()
    zipcode = faker.zipcode()
        
        
    if (profile['sex'] == 'F'):
        gender = "FEMALE"
    else:
        gender = "MALE"
    names = helpers.generate_name(gender)
    return {
        "applicationType": random.choice(["CHECKING", "SAVINGS", 
                    "CHECKING_AND_SAVINGS", "CREDIT_CARD", "LOAN"]),
        "noApplicants": False,
        "applicants": [{
            "firstName": names[0],
            "middleName": names[1],
            "lastName": names[2],
            "dateOfBirth": faker.date_of_birth(minimum_age=18).strftime(f'%Y-%m-%d'),
            "gender": gender,
            "email": profile['mail'],
            "phone": f'{random.randrange(100, 1000, 3)}-{random.randrange(100, 1000, 3)}-{random.randrange(1000, 10000, 4)}',
            "socialSecurity": profile['ssn'],
            "driversLicense": ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)),
            "income": round(random.randrange(1500000,12000000)),
            "address": address,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "mailingAddress": address,
            "mailingCity": city,
            "mailingState": state,
            "mailingZipcode": zipcode
        }]
    }

# ADMIN PRODUCER

def generate_admin():
    name = helpers.generate_name("MALE")
    
    return {
        "role": "admin",
        "username": name[0] + name[2],
        "password": 'Myp@ssword1!',
        "firstName": name[0],
        "lastName": name[1],
        "email": faker.email(),
        "phone": helpers.generate_phone()
    }

# MEMBER PRODUCER

def generate_member(response):
    return {
        "role": "member",
        "username": faker.first_name() + faker.last_name(),
        "password": 'Myp@ssword1!',
        "firstName": response['applicants'][0]['firstName'],
        "lastName": response['applicants'][0]['lastName'],
        "email": response['applicants'][0]['email'],
        "phone": response['applicants'][0]['phone'],
        "lastFourOfSSN": response['applicants'][0]['socialSecurity'][7:11],
        "membershipId": response['createdMembers'][0]['membershipId']
    }

# BANK PRODUCER

def generate_bank():
    return {
        "routingNumber": helpers.generate_routing(),
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode()
    }

# BRANCH PRODUCER

def generate_branch(bankId):
    return {
        "bankID": bankId,
        "name": random.choice(faker.company()),
        "address": faker.street_address(),
        "phone": helpers.generate_phone(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zipcode": faker.zipcode()
    }

# TRANSACTION PRODUCER

def generate_transaction(account_number, value=0):
    type = random.choice([
            "DEPOSIT",
            "WITHDRAWAL",
            "TRANSFER_IN",
            "TRANSFER_OUT",
            "PURCHASE",
            "PAYMENT",
            "REFUND"])
    method = random.choice([
            "ACH",
            "ATM",
            "DEBIT_CARD",
            "APP"])
    if value == 0:
        value = round(random.randint(100,1200000))
    else:
        type = "DEPOSIT"
        method = "ATM"

    return {
        "type": type,
        "method": method,
        "amount": value,
        "merchantCode": "ALINE",
        "description": f"{type} transaction using method: {method}",
        "accountNumber": account_number
    }