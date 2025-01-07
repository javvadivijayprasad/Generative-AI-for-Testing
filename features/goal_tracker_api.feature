Feature: Check API Status

    @api
    Scenario: Check API status
        Given the base URL is "https://goal-tracker-api.onrender.com/api/v1/"
        When I send a GET request to "status"
        Then the response status should be "200"
        And  the response body should contain "OPERATIONAL"