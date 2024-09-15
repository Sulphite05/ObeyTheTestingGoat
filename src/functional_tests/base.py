# failing test if superlists are not configured
# django-admin startproject superlists .
# The superlists folder is intended for stuff that applies to the whole
# project-like settings.py, for example, which is used to store global
# configuration information for the site.
# But the main thing to notice is manage.py. That’s Django’s Swiss Army knife,
# and one of the things it can do is run a development server.
# python manage.py runserver
# test passed after this
import os
# Tests that use Selenium let us drive a real web browser, so they really
# let us see how the application functions from the user’s point of view.
# That’s why they’re called functional tests.
# Functional Test == Acceptance Test == End-to-End Test
# established LiveServer connection for test database

import time
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 5


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server: self.live_server_url = "http://" + test_server

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_todo_list(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                # WebDriverException for when the page hasn’t loaded and
                # Selenium can’t find the table element on the page, and AssertionError for when the table is there,
                # but it’s perhaps a table from before the page reloads, so it doesn’t have our row in yet.
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)



# if __name__ == "__main__":
#     # that’s how a Python script checks if it’s been executed from the command line,
#     # rather than just imported by another script
#
#     unittest.main()     # searches for all tests in main files then runs them

# git commit -a to automatically add any changes to tracked files(not any newly added file)

# User Story
# A description of how the application will work from the point of view of the user.
# Used to structure a functional test.

# Expected failure
# When a test fails in the way that we expected it to.

# python manage.py startapp lists
# to start building the app

# Functional tests test the application from the outside, from the user’s point of view(per test per feature)
# Unit tests test the application from the inside, from the programmer’s point of view(multiple tests per feature)
