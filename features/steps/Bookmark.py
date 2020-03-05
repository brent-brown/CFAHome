from behave import *


import features.pages.CFAHomePageObjects
import features
import applitools.common.match
from features.environment import *

#from features.environment import eyes

features.pages.CFAHomePageObjects.use_step_matcher("re")
use_step_matcher("re")


@when('I click on the "Bookmark" icon')
def step_impl(context):
    # bookMarkIcon = context.browser.find_element_by_css_selector("a.person.bookmark-nav-icon.bookmark-select-nav")
    if features.pages.CFAHomePageObjects.Locators.BOOKMARK_ICON:
        print()
        #context.browser.find_element(*Locators.BOOKMARK_ICON).click()
       # context.browser.implicitly_wait(2000)
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
        #eyes.branch_name = "Books"
        #eyes.open(context.browser, "CFAHome", "Bookmark Page (Desktop)")

        # eyes.force_full_page_screenshot = True
        # eyes.check_region_by_element()

        features.environment.eyes.match_level = features.environment.eyes.MatchLevel.LAYOUT


        # eyes.check_region_in_frame('#bookmark-page > ul')
        #eyes.check(context.browser.current_url, Target.window())
        print(context.browser.current_url)

        # End the test.
        #eyes.close()
    else:
        print("Not on bookmark page")
