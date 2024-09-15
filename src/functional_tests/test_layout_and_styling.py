from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class LayoutAndStyling(FunctionalTest):
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

