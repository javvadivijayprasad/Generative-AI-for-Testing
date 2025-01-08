from behave import given, when, then
from utils.types import CustomContext
import logging
from playwright.sync_api import TimeoutError


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('verify_logger')


@given('I am on the Register Account page')
def step_impl(context:CustomContext):
    context.page.goto("https://demo.opencart.com/en-gb?route=account/register")


