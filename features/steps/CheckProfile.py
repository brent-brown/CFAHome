
from environment import *
from behave import *
import os

from selenium import webdriver
from applitools.selenium import Eyes
import environment
from features.environment import *

use_step_matcher("re")



# @given("I am on the CFAHome Page")
# def step_impl(context):
#
#     context.browser.get("https://int.portal.cfahome.com")
#     context.browser.implicitly_wait(500)
#
#
#     theUser = context.browser.find_element_by_xpath('//*[@id="okta-signin-username"]')
#     theUser.clear()
#
#     enterUN = os.environ['CFAUSER_ADMIN']
#     theUser.send_keys(enterUN)
#
#     passsword = context.browser.find_element_by_css_selector("#okta-signin-password")
#     passsword.clear()
#     enterPW = os.environ['CFAPW_ADMIN']
#     passsword.send_keys(enterPW)
#
#     context.browser.find_element_by_css_selector("#okta-signin-submit").click()
#     context.browser.implicitly_wait(200)
#
#     popUpMessage = context.browser.find_element_by_css_selector("#wm-shoutout-170936")
#     context.browser.implicitly_wait(500)
#     if popUpMessage.is_displayed():
#         context.browser.find_element_by_css_selector('#wm-shoutout-170936 > div.wm-content > div.buttons-wrapper > span').click()
#     else:
#         return
#
#
#     welcome = context.browser.find_element_by_css_selector('body > div.chik-header > div > a.logo-container > img')
#     #content = context.browser.find_element_by_css_selector('div.prefName')
#     if welcome.is_displayed():
#         print('STEP: I am on the CFAHome Page')
#     else:
#         print('STEP: I am NOT on the CFAHome Page')
#




@when("I click on the user Icon")
def step_impl(context):

    userIcon = context.browser.find_element_by_css_selector("body > div.chik-header > div > a.person.person-img")
    userIcon.click()
    context.browser.implicitly_wait(10000)



    print('STEP: When I click on the user Icon')


@then("I should be on the User Profile page")
def step_impl(context):
    title = context.browser.title
    print(title)
    assert "Accounts" in title
    #eyes.open(context.browser, "User Profile", "HomePage", {'width': 800, 'height': 600})
    eyes.check("Check Profile Test", Target.window())

    # End the test.
    eyes.close()

    print('STEP: Then I should be on the User Profile page')
