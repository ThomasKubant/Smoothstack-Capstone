import string
import random
from faker import Faker

fake = Faker()


def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_routing(size=9):
    return int(''.join(random.choices(string.digits, k=size)))

def generate_password(minSize=14):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(minSize))

def generate_phone():
    return f'{random.randrange(100, 1000, 3)}-{random.randrange(100, 1000, 3)}-{random.randrange(1000, 10000, 4)}'

def gender():
    return random.choice(["MALE", "FEMALE"])

def generate_name(gender):
    if gender == 'MALE' or gender == 'M':
        first_name = fake.first_name_male()
        middle_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.first_name_female()
        last_name = fake.last_name_male()

    return (first_name, middle_name, last_name)

def generate_username(size=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))