from behave import given, when, then
import requests

@given('the base URL is "{base_url}"')
def step_impl(context,base_url):
    context.base_url = base_url


@when('I send a GET request to "{end_point}"')
def step_impl(context,end_point):
    endpoint = f"{context.base_url}{end_point}"
    response = requests.get(endpoint)
    context.response =response


@then('the response status should be {statuscode}')
def step_impl(context,statuscode):
    statuscode = statuscode.strip('"')
    assert context.response.status_code == int(statuscode),f"Expected status code {statuscode} but got {context.response.status_code}"



@then('the response body should contain "{expected_text}"')
def step_impl(context,expected_text):
    assert expected_text in context.response.text,f"Response text does not contain {expected_text} : {context.response.text}"

