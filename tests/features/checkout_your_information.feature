Feature: Checkout - Your Information

  Background: 
    Given the user is logged in with valid credentials
    And the user has added a random number of items to the cart
    And the user has navigated to the cart
    And the user begins the checkout process

  Scenario: User verifies expected elements on the checkout: Your Information page
    Given the user is on the checkout: Your Information page
    Then the following elements should be visible:
      | Elements         |
      | first name field |
      | last name field  |
      | zip code field   |
      | continue button  |
      | cancel button    |

  Scenario: User fills in the checkout form with valid information
    Given the user is on the checkout: Your Information page
    When the user fills in the form with the following input:
      | First Name | Last Name | Zip/Postal Code |
      | Antonio    | Santos    |        4567-123 |
    And the user clicks the Continue button
    Then the user should be redirected to the checkout: Overview page

  Scenario Outline: User fills in the checkout form partially and validates error messages
    Given the user is on the checkout: Your Information page
    When the user fills in the form with the partial information first name: <first_name>, last name: <last_name>, zip code: <postal_code>, and submits it
    Then the error message "<error_message>" should be displayed

    Examples: 
      | first_name | last_name | postal_code | error_message                  |
      | Antonio    | Santos    | empty       | Error: Postal Code is required |
      | empty      | Santos    |    4567-123 | Error: First Name is required  |
      | Antonio    | empty     |    4567-123 | Error: Last Name is required   |
      | Antonio    | empty     | empty       | Error: Last Name is required   |

  Scenario: User clicks the Cancel button
    Given the user is on the checkout: Your Information page
    When the user clicks the Cancel button
    Then the user should be redirected to Your Cart page
    And the user sees his previously chosen items

  Scenario: User retuns to Shopping Cart
    Given the user is on the checkout: Your Information page
    When the user clicks the Cart icon
    Then the user should be redirected to Your Cart page
    And the user sees his previously chosen items
