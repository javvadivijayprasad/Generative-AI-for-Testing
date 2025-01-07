Feature: Contact Us form functionality

    Background: Pre-condition
        Given I am on the Contact Us form

    @smoke
    Scenario Outline: Form Submission scenario
        When I fill in the "first_name" field with "<first_name>"
        And  I fill in the "last_name" field with "<last_name>"
        And  I fill in the "email" field with "<email>"
        And  I fill in the "message" field with "<message>"
        And  I click on the "<button>" button
        Then I should see the message "<expected_message>"

        Examples:
            | first_name | last_name | email                     | message    | button | expected_message               |
            | vijay      | javvadi   | vijay.javvadi@example.com | contact me | SUBMIT | Thank You for your Message!    |
            | Prasad     | vijay     | prasad.vijayexamplecom    | contact me | SUBMIT | Error: Invalid email address   |
            | \n         | \n        | \n                        | \n         | SUBMIT | Error: all fields are required |

    @smoke
    Scenario: Missing fields
        And   I click on the "SUBMIT" button
        Then  I should see an error message saying "Error: all fields are required"

    @smoke
    Scenario: Using the 'RESET' button
        When  I fill in the "first_name" field with "vijay"
        And   I fill in the "last_name" field with "javvadi"
        And   I fill in the "email" field with "vijay.javvadiexamplecom"
        And   I fill in the "message" field with "contact me"
        And   I click on the "RESET" button
        Then  all fields should be cleared of any entered information