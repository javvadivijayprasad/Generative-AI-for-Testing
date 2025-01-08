Feature: Register Account form functionality
    Background: Pre-cond
        Given I am on the Register Account page

    Scenario Outline: Valid page submission
        When I fill in the "firstname" field with "<First_Name>"
        And  I fill in the "lastname" field with "<Last_Name>"
        And  I fill in the "email" field with "<Email_Address>"
        And  I fill in the "password" field with "<Message>"
        # And   I check the Privacy Policy as "Privacy_Policy"
        # And   I check the Subscribe as "Subscribe"
        # And   I click on the "submit" button
        # Then  I should see the message "Message"
        Examples:
            | First_Name | Last_Name | Email_Address        | Password | Privacy_Policy | Subscribe | Message                        |
            | vijay      | javvadi   | example1@example.com | 1qazxsw2 | Yes            | Yes       | Your Account Has Been Created! |

# Scenario: Missing fields
#     Given I am on the Register Account page
#     When  I click the 'Continue' button
#     Then  I should see the error message for each missing field

# Scenario: Invalid email address
#     Given I am on the Register Account page
#     When  I fill in the 'Email Address' with "invalidemail"
#     And   I click the 'Continue' button
#     Then  I should see the error message "'E-Mail Address does not appear to be valid!'"

# Scenario: Missing only First Name
#     Given I am on the Register Account page
#     When  I fill in the 'Last Name' with "Doe", 'Email Address' with "johndoe@example.com", 'Password' with "password123"
#     And   I click the 'Continue' button
#     Then  I should see the error message "'First Name must be between 1 and 32 characters!'"

# Scenario: Missing only Last Name
#     Given I am on the Register Account page
#     When  I fill in the 'First Name' with "John", 'Email Address' with "johndoe@example.com", 'Password' with "password123"
#     And   I click the 'Continue' button
#     Then  I should see the error message "'Last Name must be between 1 and 32 characters!'"

# Scenario: Missing only Password
#     Given I am on the Register Account page
#     When  I fill in the 'First Name' with "John", 'Last Name' with "Doe", 'Email Address' with "johndoe@example.com"
#     And   I click the 'Continue' button
#     Then  I should see the error message "'Password must be between 4 and 20 characters!'"

# Scenario: Missing to agree Privacy Policy
#     Given I am on the Register Account page
#     When  I fill in the 'First Name' with "John", 'Last Name' with "Doe", 'Email Address' with "johndoe@example.com", 'Password' with "password123"