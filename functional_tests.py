from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://localhost:8000")

assert "Congratulations" in browser.title   # should type congratulations to map

print("Okay!")  # failing test if superlists are not configured
# django-admin startproject superlists .
# The superlists folder is intended for stuff that applies to the whole
# project- like settings.py, for example, which is used to store global
# configuration information for the site.
# But the main thing to notice is manage.py. That’s Django’s Swiss Army knife,
# and one of the things it can do is run a development server.
# python manage.py runserver
# test passed after this



