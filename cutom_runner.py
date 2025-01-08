from behave.__main__ import main as behave_main
import os
import shutil
import argparse


def clean_and_create_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


if __name__ == "__main__":

    allure_results_folder = "reports"
    screenshot_folder = "screenshots"

    clean_and_create_folder(allure_results_folder)
    clean_and_create_folder(screenshot_folder)

    # Set-up command-line arguments for running behave tests with specific tags
    parser = argparse.ArgumentParser(description="Run behave tests with specific tags.")
    parser.add_argument("--tags",help="Behave tags to filter scenario",default="")
    args = parser.parse_args()

    #check if behave_tag is set by jenkins
    tags = args.tags or os.getenv("BEHAVE_TAGS","")


    behave_main(
        [
            "--tags",tags,
            "--format",
            "allure_behave.formatter:AllureFormatter",
            "--outfile",
            "reports/allure-results",
        ]
    )

# allure generate reports/allure-results -o reports/allure-reports --clean
# allure open reports/allure-reports
