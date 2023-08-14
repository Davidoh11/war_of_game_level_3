import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_scores_service(url):
    # Initialize the browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run the browser in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the score element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))

        # Get the text content of the score element
        score_text = driver.find_element(By.ID, 'score').text

        # Convert the score to an integer and check if it's within the range 1-1000
        score = int(score_text)
        is_valid = 1 <= score <= 1000
    except (TimeoutException, ValueError):
        is_valid = False
    finally:
        driver.quit()  # Close the browser

    return is_valid


def main_function(url):
    if test_scores_service(url):
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1


if __name__ == "__main__":
    application_url = "http://localhost:8777"
    exit_code = main_function(application_url)
    exit(exit_code)