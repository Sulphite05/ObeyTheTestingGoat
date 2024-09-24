import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
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
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
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
