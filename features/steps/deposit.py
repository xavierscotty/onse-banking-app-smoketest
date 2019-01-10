import os
import time

import requests
from behave import *

URL = os.getenv('URL', 'http://localhost')


@given('there is a new account for customer "{customer_id}"')
def create_account(context, customer_id):
    create_account_request = dict(customerId=customer_id)

    response = requests.post(f'{URL}/accounts/accounts', json=create_account_request)

    assert response.status_code == 201, \
        f'Expected 201 when creating account, got {response.status_code}'
    body = response.json()
    context.account_number = body['accountNumber']


@when('I deposit {amount:d} the account"')
def deposit(context, amount):
    deposit_request = {'accountNumber': context.account_number,
                       'amount': amount,
                       'operation': 'deposit'}

    response = requests.post(f'{URL}/cashier/create', json=deposit_request)

    assert response.status_code == 202, \
        f'Expected 202 when creating deposit, got {response.status_code}'


@then('then balance of the account should be {amount:d}')
def assert_balance_increased(context, amount):
    balance = None
    retries = 5

    while balance != amount and retries > 0:
        response = requests.get(f'{URL}/balance/{context.account_number}')
        assert response.status_code == 200, \
            f'Expected 200 when checking balance, got {response.status_code}'
        body = response.json()
        balance = body['balance']
        retries = retries - 1
        time.sleep(1)

    assert balance == amount, f'{balance} != {amount}'
