from utils.openai_utils import generate_text

def analyze_steps(file_path):
    """
    Check Behave steps and suggest code for missing ones.

    """
    try:
        with open(file_path,"r") as f:
            steps = f.read()
    except FileNotFoundError:
        print(f"Error: file {file_path} not found")
        return
    
    environment_context = """

    The automation framework is already set up to initialize Playwright in environment.py.
    This includes setting up the browser, creating a new page, and managing teardown processes.
    Avoid reinitializing Playwright in step definitions as it is redundant.
    You can access the current page using 'context.page'.
    
    """

    # Create a promt combining the environment context and the behave steps

    prompt = f"""
    {environment_context}

    Analyze the following Behave step definitions. 
    For each unimplemented step, 
    provide example Python code to implement it, using Playwright for browser automation.
    Ensure you add assertions to steps which perform validation i.e steps which contains 'Then I should see'
    Behave steps:
    {steps}

    """

    # Generate AI suggestions
    suggestions = generate_text(prompt)
    print("AI suggestions:\n")
    print(suggestions)

if __name__ == "__main__":
    analyze_steps("features/steps/contact_us_forms_steps.py")