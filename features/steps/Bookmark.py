from behave import *
from features.environment import *
from selenium.common.exceptions import *
from features.pages.CFAHomePageObjects import *
from applitools.common import *
from applitools.core import *

from applitools.selenium import *
from selenium import webdriver

use_step_matcher("re")


@when('I click on the "Bookmark" icon')
def step_impl(context):
    # bookMarkIcon = context.browser.find_element_by_css_selector("a.person.bookmark-nav-icon.bookmark-select-nav")
    if Locators.BOOKMARK_ICON:
        context.browser.find_element(*Locators.BOOKMARK_ICON).click()
        context.browser.implicitly_wait(2000)
    else:
        return Exception

    print('STEP: I click on the "Bookmark" icon')


@step("I am on the bookmark page")
def step_impl(context):
    context.browser.implicitly_wait(1000)
    title = context.browser.title
    print(title)
    assert "Bookmarks" in title

    print('STEP: I am on the bookmark page')


@then("The user should be able to view their bookmarks")
def step_impl(context):
    title = context.browser.title

    # #bookList = context.browser.find_element_by_css_selector("#bookmark-page > ul")
    if "Bookmarks" in title:
        eyes.branch_name = "Books"
        eyes.open(context.browser, "CFAHome", "Bookmark Page (Desktop)")

        # eyes.force_full_page_screenshot = True
        # eyes.check_region_by_element()

        eyes.match_level = MatchLevel.LAYOUT


        # eyes.check_region_in_frame('#bookmark-page > ul')
        eyes.check(context.browser.current_url, Target.window())
        print(context.browser.current_url)

        # End the test.
        eyes.close()
    else:
        print("Not on bookmark page")
