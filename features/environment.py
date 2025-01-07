from playwright.sync_api import sync_playwright
from utils.types import CustomContext
import json
import logging
import allure
from allure_commons.types import AttachmentType


# Setup up logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def before_all(context: CustomContext):
    # This Function is called before all the test start
    logger.info("Starting Automation Test Suite....")

    # Load envionment variables from env.json
    with open("config/env.json", "r") as file:
        env_vars = json.load(file)

        # Accessing variables from env.json
    context.browser_type = env_vars.get("browser", "chromium")
    context.headless_mode = env_vars.get("headless", False)

    context.playwright = sync_playwright().start()
    context.is_api_test = False


def before_scenario(context: CustomContext, scenario):
    # This function is called before each scenario
    logger.info(f"Starting Scenario: {scenario.name}")

    if "api" in scenario.tags:
        context.is_api_test = True
        logger.info("Skipping browser setup for API Scenario...")
    else:
        context.is_api_test = False
        context.browser = context.playwright[context.browser_type].launch(headless=context.headless_mode, args=["--start-maximized"])    
        context.page = context.browser.new_page(no_viewport=True) # Create a new page for the scenario



def after_scenario(context: CustomContext, scenario):
    # Capture screenshot on failure
    if scenario.status == "failed" and not context.is_api_status:
        screenshot_path = f"screenshots/{scenario.name.replace(' ','_')}.png"
        context.page.screenshot(path=screenshot_path)
        logger.info(f"Captured screenshots for failed Scenario: {screenshot_path}")

        # Attach screen to allure report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=scenario.name,
                attachment_type=AttachmentType.PNG,
            )
    if not context.is_api_test and hasattr(context, 'page'):
        context.page.close()

    # This function is called after each scenario
    logger.info(f"Ending Scenario : {scenario.name}")


def after_all(context: CustomContext):
    # This Function is called after all test have finished
    logger.info("Stopping Automation Test Suite.......")

    if hasattr(context, 'browser') and not context.is_api_test:
        context.browser.close() # Close the browser
        context.playwright.stop() # Stop the Playwright instance
