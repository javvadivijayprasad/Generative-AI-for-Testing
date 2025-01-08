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
    """,
    "Registor Account Page":"""
    Feature: Register Account form functionality

    Write Gherkin scenarios for testing a Register Account page with the following details:
    - The form contains input fields: 'First Name', 'Last Name', 'Email Address', and 'Passoed'.
    - 'First Name' must be between 1 and 32 characters.
    - 'Last Name'  must be between 1 and 32 characters.
    - 'Password' must be between minimum 4 and maximum 20
    - All fields are mandatory.
    - The 'Continue' button submits the form.
    - The 'I have read and agree to the Privacy Policy' and Subscribe toggle button .
    - The email address must be valid and contain an '@' symbol.
    - A success message is displayed for valid submissions: 'Your Account Has Been Created!'.
    - Error messages:
      - 'First Name must be between 1 and 32 characters!'
      - 'Last Name must be between 1 and 32 characters!'.
      - 'E-Mail Address does not appear to be valid!'.
      - 'Password must be between 4 and 20 characters!'.
      - 'Warning: You must agree to the Privacy Policy!'.
    
    For each scenario:
    1. Start with 'Given I am on the Register Account page.'
    2. Include explicit steps for filling fields, clicking buttons, and validating messages.
    
    Generate scenarios for:
    1. Valid page submission.
    2. Missing fields.
    3. Invalid email address.
    4. Missing only Firt Name.
    5. Missing only Flast Name.
    6. Missing only Password.
    7. Missing to agree Privacy Policy.
    8. Submition without subscribe

    Do not use code formatting tags like ```gherkin or ```. Output plain Gherkin syntax only.
    """
}

# Pretty-print the json data with indentation for readability
print(json.dumps(prompts,indent=2))