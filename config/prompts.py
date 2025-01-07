import json
prompts = {
    "contact_us_form": """
    Feature: Contact Us form functionality
    
    Write Gherkin scenarios for testing a Contact Us form with the following details:
    - The form contains input fields: 'First Name', 'Last Name', 'Email Address', and 'Comments'.
    - All fields are mandatory.
    - The 'SUBMIT' button submits the form.
    - The 'RESET' button clears all fields.
    - The email address must be valid and contain an '@' symbol.
    - A success message is displayed for valid submissions: 'Thank You for your Message'.
    - Error messages:
      - 'Error: Invalid email address'
      - 'Error: All fields are required'.
    
    For each scenario:
    1. Start with 'Given I am on the Contact Us form.'
    2. Include explicit steps for filling fields, clicking buttons, and validating messages.
    
    Generate scenarios for:
    1. Valid form submission.
    2. Missing fields.
    3. Invalid email address.
    4. Using the 'RESET' button.

    Do not use code formatting tags like ```gherkin or ```. Output plain Gherkin syntax only.
    """
}

# Pretty-print the json data with indentation for readability
print(json.dumps(prompts,indent=2))