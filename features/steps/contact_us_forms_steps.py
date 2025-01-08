from behave import given, when, then
from utils.types import CustomContext
import logging
from playwright.sync_api import TimeoutError


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('verify_logger')

@given("I am on the Contact Us form")
def navigate_to_contact_us_form(context:CustomContext):
    context.page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")


@when('I fill in the "{field}" field with "{value}"')
def fill_in_field(context:CustomContext, field, value):
    field_selector = f'[name="{field}"]'
    if value=="\\n":
        logger.info(f"Skipping fiels {field} as indicated by '\\n'.")
        return
    context.page.wait_for_selector(field_selector)
    context.page.fill(field_selector,value)
    logger.info(f"Filled field {field} with data {value}")



    


@when('I click on the "{button}" button')
@given('I click on the "{button}" button')
@then('I click on the "{button}" button')
def click_button(context:CustomContext, button):
    context.page.wait_for_timeout(2000)
    button_selector = f'[value="{button}"]'
    context.page.wait_for_selector(button_selector)
    context.page.click(button_selector)
   


@then(' should see the success message "{message}"')
def verify_success_message(context:CustomContext, message):
    success_message = f'//*[contains(text(),"{message}")]'
    try:
        logger.info(f"Waiting for success message:{message}")
        context.page.wait_for_selector(success_message,timeout=2000)
        assert  context.page.is_visible(success_message)
        logger.info(f"Success message:{message} is visable!")
    except TimeoutError:
        logger.error(f"{message} : is not found")

        assert False,f"Sucess message '{message}' not found on the page"

@then('I should see an error message saying "{message}"')
def verify_error_message(context:CustomContext, message):
    error_message = f'//body[contains(.,"{message}")]'
    try:
        logger.info(f"Waiting for error message: {message}")
        context.page.wait_for_selector(error_message, timeout=2000)
        assert context.page.is_visible(error_message)
        logger.info(f"Error message: {message} is visible!")
    except TimeoutError:
        logger.error(f"{message} : is not found")
        assert False, f"Error message '{message}' not found on the page"
    
@then("all fields should be cleared of any entered information")
def verify_fields_cleared(context:CustomContext):
    field_names = ["first_name", "last_name", "email", "message"]
    for field in field_names:
        field_selector = f'[name="{field}"]'
        entered_text = context.page.locator(field_selector).input_value()
        assert entered_text == "", f"Field '{field}' still has text: {entered_text}"

@then('I should see the message "{expected_message}"')
def verify_message(context:CustomContext, expected_message):
    message_selector = f'//*[contains(text(),"{expected_message}")] | //body[contains(.,"{expected_message}")]'
    try:
        logger.info(f"Waiting for message:{expected_message}")
        context.page.wait_for_selector(message_selector,timeout=2000)
        assert  context.page.is_visible(message_selector)
        logger.info(f"Message:{expected_message} is visable!")
    except TimeoutError:
        logger.error(f"{expected_message} : is not found")
        assert False,f"Message '{expected_message}' not found on the page"