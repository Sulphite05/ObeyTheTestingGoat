# from unittest import skip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Aqiba goes to he home page and accidently submits an empty list item
        # She hits enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)

        # The home page refreshes with an error saying the list item cannot be blank
        self.wait_for(lambda: self.assertEqual(self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                                               "You can't have an empty list item")
                      )

        # She tries again with some text in the input and it works
        self.browser.find_element(By.ID, "id_new_item").send_keys("Purchase meat")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_todo_list("1. Purchase meat")

        return  # TODO: Remove early return

        # Perversely, she tries entering another blank item
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)

        # She receives a similar warning
        self.wait_for(lambda: self.assertEqual(self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                                               "You can't have an empty list item")
                      )

        # And then she corrects it by sending a non-empty list item
        self.browser.find_element(By.ID, "id_new_item").send_keys("Make tea")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_todo_list("1. Purchase meat")
        self.wait_for_row_in_todo_list("2. Make tea")


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
