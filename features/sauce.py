# import pytest
# from selenium import webdriver
# import os
# from _pytest.runner import runtestprotocol
#
#
#
# def driver(context):
#     sauce_username = os.environ["SAUCE_USERNAME"]
#     sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
#     remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
#
#     desired_cap = {
#         'platform': 'Mac OS X 10.13',
#         'browserName': 'safari',
#         'version': '11.1',
#         'build': 'Onboarding Sample App - Python + Pytest',
#         'name': '2-user-site',
#         'username': sauce_username,
#         'accessKey': sauce_access_key
#     }
#
#     context.browser = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)
#     yield context.browser
#     context.browser.quit()
#
#
# # Here is our actual test code. In this test we open the saucedemo app in chrome and assert that the title is correct.
# def test_should_open_chrome(context):
#     # Substitute 'http://www.saucedemo.com' for your own application URL
#     context.browser.get("https://www.saucedemo.com")
#     actual_title = context.browser.title
#     expected_title = "Swag Labs"
#     assert expected_title == actual_title