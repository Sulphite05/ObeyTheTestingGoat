# failing test if superlists are not configured
# django-admin startproject superlists .
# The superlists folder is intended for stuff that applies to the whole
# project-like settings.py, for example, which is used to store global
# configuration information for the site.
# But the main thing to notice is manage.py. That’s Django’s Swiss Army knife,
# and one of the things it can do is run a development server.
# python manage.py runserver
# test passed after this

# Tests that use Selenium let us drive a real web browser, so they really
# let us see how the application functions from the user’s point of view.
# That’s why they’re called functional tests.
# Functional Test == Acceptance Test == End-to-End Test
# established LiveServer connection for test database

import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 5


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()


    def test_layout_and_styling(self):

        # Aqiba goes to the homepage
        self.browser.get(self.live_server_url)

        # Her browser window is set to a very specific size
        self.browser.set_window_size(1024, 768)

        # She notices the input box isnicely centered
        inputbox =self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10,
        )

        # She starts a new list and sees the input is nicely centered there too
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_todo_list("1. testing")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] /2,
            512,
            delta=10,
        )




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

    def test_can_start_a_todo_list(self):

        # Aqiba has heard about a new To Do list App
        # She checks its homepage
        # self.browser.get("http://localhost:8000")
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Knead Dough" in  a text-box
        inputbox.send_keys("Knead Dough")  # selenium's way of typing into input elements

        # When she hits enter, the page updates and shows "1. Knead Dough" on the page
        inputbox.send_keys(Keys.ENTER)

        # self.assertTrue(any(row.text == "1. Knead Dough" for row in rows),
        #                 "New To-Do item did not appear in the table. "
        #                 f"Contents were \n{table.text}") # generator not list comprehension

        self.wait_for_row_in_todo_list("1. Knead Dough")

        # There is still a text-box inviting her to add a new item to the list
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She enters "Roll the rotis" as she is very methodical and presses enter
        inputbox.send_keys("Roll the rotis")  # selenium's way of typing into input elements
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and shows both items on the page
        self.wait_for_row_in_todo_list("1. Knead Dough")
        self.wait_for_row_in_todo_list("2. Roll the rotis")
        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Iqra starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Knead Dough")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_todo_list("1. Knead Dough")

        # she notices that her list has a unique url
        iqra_list_url = self.browser.current_url
        self.assertRegex(iqra_list_url, '/lists/.+')

        ##  We delete all browser cookies(meta comments are written in ##)
        ##  As a way of simulating a brand new user session
        self.browser.delete_all_cookies()

        # Aqsa visits the home page. There is no sign of Iqra's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Knead Dough", page_text)
        self.assertNotIn("Roll the rotis", page_text)

        # Aqsa starts a new list entering a new item. She is a little less interesting than Iqra :')
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Do homework")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_todo_list("1. Do homework")

        # Aqsa gets her own unique url
        aqsa_list_url = self.browser.current_url
        self.assertRegex(aqsa_list_url, "/lists/.+")
        self.assertNotEqual(iqra_list_url, aqsa_list_url)

        # Again there is no trace of Iqra's list
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Knead Dough", page_text)
        self.assertNotIn("Roll the rotis", page_text)

        # Satisfied, they both go back to sleep


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
