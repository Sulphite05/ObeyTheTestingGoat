# from unittest import skip
from .base import FunctionalTest




class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Aqiba goes to he home page and accidently submits an empty list item
        # She hits enter on the empty input box

        # The home page refreshes with an error saying the list item cannot be blank
        # SHe tries again with some text in the input and it works

        # Perversely, she tries entering another blank item
        # She receives a similar warning
        # And then she corrects it by sending a non-empty list item
        self.fail("write me!")


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
