# failing test if superlists are not configured
# django-admin startproject superlists .
# The superlists folder is intended for stuff that applies to the whole
# project- like settings.py, for example, which is used to store global
# configuration information for the site.
# But the main thing to notice is manage.py. That’s Django’s Swiss Army knife,
# and one of the things it can do is run a development server.
# python manage.py runserver
# test passed after this
import time
# Tests that use Selenium let us drive a real web browser, so they really
# let us see how the application functions from the user’s point of view.
# That’s why they’re called functional tests.
# Functional Test == Acceptance Test == End-to-End Test

import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_todo_list(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_todo_list(self):

        # Aqiba has heard about a new To Do list App
        # She checks its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Knead Dough" in  a text-box
        inputbox.send_keys("Knead Dough")   # selenium's way of typing into input elements

        # When she hits enter, the page updates and shows "1. Knead Dough" on the page
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # self.assertTrue(any(row.text == "1. Knead Dough" for row in rows),
        #                 "New To-Do item did not appear in the table. "
        #                 f"Contents were \n{table.text}") # generator not list comprehension

        self.check_for_row_in_todo_list("1. Knead Dough")

        # There is still a text-box inviting her to add a new item to the list
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She enters "Roll the rotis" as she is very methodical and presses enter
        inputbox.send_keys("Roll the rotis")  # selenium's way of typing into input elements
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and shows both items on the page
        self.check_for_row_in_todo_list("2. Roll the rotis")
        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    # that’s how a Python script checks if it’s been executed from the command line,
    # rather than just imported by another script

    unittest.main()     # searches for all tests in main files then runs them

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



