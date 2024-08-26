# failing test if superlists are not configured
# django-admin startproject superlists .
# The superlists folder is intended for stuff that applies to the whole
# project- like settings.py, for example, which is used to store global
# configuration information for the site.
# But the main thing to notice is manage.py. That’s Django’s Swiss Army knife,
# and one of the things it can do is run a development server.
# python manage.py runserver
# test passed after this

# Tests that use Selenium let us drive a real web browser, so they really
# let us see how the application functions from the user’s point of view.
# That’s why they’re called functional tests.
# Functional Test == Acceptance Test == End-to-End Test

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_todo_list(self):

        # Aqiba has heard about a new To Do list App
        # She checks its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to do lists
        self.assertIn("To-Do", self.browser.title)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")
        [...]
        # She types "Knead Dough" in  a text-box

        # When she hits enter, the page updates and shows "1. Knead Dough" on the page

        # There is still a text-box inviting her to add a new item to the list

        # She enters "Roll the rotis" as she is very methodical and presses enter

        # The page updates again and shows both items on the page

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



