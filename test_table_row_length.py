import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="module")
def driver():
    """
    Fixture to initialize the WebDriver and ensure proper cleanup.
    """
    geckodriver_path = r"C:\Users\91735\Downloads\geckodriver-v0.35.0-win64\geckodriver.exe"  # Replace with your path
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)  # Set implicit wait
    yield driver
    driver.quit()


def test_verify_table_row_length(driver):
    """
    Test to verify the number of table rows after searching for 'New York'.
    """
    # Open the target page
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    # Locate the search box and enter 'New York'
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.send_keys("New York")

    # Get all rows in the table
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    # Assertion to verify the number of rows
    assert len(rows) == 5, f"Expected 5 rows, but found {len(rows)}."

