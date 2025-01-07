from utils.openai_utils import generate_text

def generate_api_test(api_name):
    prompt = f"""
    Generate a Gherkin scenario for testing the {api_name} API. The scenarios should:
    - Be concise and focus only on the API status
    - Include minimal steps.
    - Base URL is: https://goal-tracker-api.onrender.com/
    - The end point is /status

    Example cases to consider:
    - Successful request; reponse will contain 'OPERATIONAL'
    """
    return generate_text(prompt)

if __name__ == "__main__":
    api_name="goal-tracker-api"
    scenarios = generate_api_test(api_name)
    print(f"Genrated scenarios for {api_name} API:\n")
    print(scenarios)