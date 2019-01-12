Feature: Deposit cash
  As an account holder
  In order to keep my money nice and safe
  I want to deposit it into my account

  Scenario: Successful deposit
    Given there is a customer "Jez Humble"
    And "Jez Humble" has a new account
    When I deposit 50 the account
    Then then balance of the account should be 50
