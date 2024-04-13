Feature: Login

  Scenario: Presence of expected elements
    Given the user is on the login page
    Then the following login page elements should be visible:
      | Page title        |
      | Username form     |
      | Password form     |
      | Login button      |
      | Login credentials |
      | Passwords         |

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    And the user clicks the login button
    Then the user should be redirected to the products page

  Scenario Outline: Testing login
    Given the user is on the login page
    When the user enters the credentials Username <username> and Password <password>
    And the user clicks the login button
    Then the following error message should be present <error_message>
    And the user should remain on the login page

    Examples: 
      | username      | password     | error_message                                                             |
      | standard_user | empty        | Epic sadface: Password is required                                        |
      | standard_user | zzzzzzzzzzz  | Epic sadface: Username and password do not match any user in this service |
      | empty         | secret_sauce | Epic sadface: Username is required                                        |
      | empty         | empty        | Epic sadface: Username is required                                        |

