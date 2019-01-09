Feature: Deposit cash
    As an account holder
    In order to keep my money nice and safe
    I want to deposit it into my account

    Scenario: Successful deposit
        Given there is a new account for customer "12345"
        When I deposit 50 the account"
        Then then balance of the account should be 50