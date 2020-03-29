from applitools.common import MatchLevel
from behave import *
from features.pages.CFAHomePageObjects import *
from applitools.selenium import Eyes, Target
import features.environment


use_step_matcher("re")


@when('I click on the "Bookmark" icon')
def step_impl(context):
    context.browser.find_element_by_css_selector("a.person.bookmark-nav-icon.bookmark-select-nav").click()
    # if Locators.BOOKMARK_ICON:
    #     print()
    #     #context.browser.find_element(*Locators.BOOKMARK_ICON).click()
    #    # context.browser.implicitly_wait(2000)
    # else:
    #     return Exception

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
        # eyes.branch_name = "Books"
        eyes.open(context.browser, "CFAHome", "Bookmark Page (Desktop)")

        eyes.match_level = MatchLevel.LAYOUT
        eyes.check(context.browser.current_url + title + " Bookmark Page Check", Target.window())
        eyes.close()

    else:
        print("Not on bookmark page")
