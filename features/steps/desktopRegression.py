from applitools.common import MatchLevel
from behave import *
from features.pages.CFAHomePageObjects import *
from applitools.selenium import Eyes, Target
import features.environment

use_step_matcher("re")


@when("I search for (?P<items>.+)")
def step_impl(context, items):
    if context.browser.find_element_by_css_selector('#txtSearch'):
        context.browser.find_element_by_css_selector('#txtSearch').send_keys(items)
        context.browser.find_element_by_css_selector('#searchSection > ul > li > a').click()
    #print(items)
    print(u'STEP: When I search for <items>')


@then("I should see (?P<items>.+) in the search results")
def step_impl(context, items):
    itemName = context.browser.find_element_by_xpath('(//div[@class="source-title"])').text
    context.browser.find_element_by_xpath('(//div[@class="source-title"])').click()
    if itemName == items:
         print(itemName)

    batch_info = BatchInfo('CFAHome - Search results check - Exact Match')
    eyes.batch = batch_info
    eyes.open(context.browser, "CFAHome", "Search Results Check - Exact Match")
    eyes.match_level = MatchLevel.LAYOUT
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + itemName + " Search Results Check", Target.window())

    # # End the test.
    eyes.close()
    print(u'STEP: Then I should see <items> in the search results')


@when("I click logout")
def step_impl(context):
    context.browser.implicitly_wait(10000)
    context.browser.find_element_by_css_selector('body > div.chik-header > div.top-header-container > div > a').click()

    print(u'STEP: When I click logout')


@then("I should be logged out of the application")
def step_impl(context):
    title = context.browser.title
    if "Chick-fil-A Login" in title:
        print("We Have logged out of the application")
    batch_info = BatchInfo('CFAHome - Logout Check')
    eyes.batch = batch_info
    eyes.open(context.browser, "CFAHome", "Logout Check")
    eyes.match_level = MatchLevel.LAYOUT
    eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + "Log Out", Target.window())

    # # End the test.
    eyes.close()


    print(u'STEP: Then I should be logged out of the application')


@then("I should see the Profile, Account Settings, and Update Information links")
def step_impl(context):
    if context.browser.find_element_by_css_selector('body > div.profile-page > div > div.tab-container'):
        print("on the user profile page")

    eyes.open(context.browser, "CFAHome", "Logout Check")
    eyes.match_level = MatchLevel.LAYOUT
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + "Log Out Check", Target.window())

    # # End the test.
    eyes.close()


    print(u'STEP: Then I should see the Profile, Account Settings, and Update Information links')


@when("The user clicks on the Email Icon")
def step_impl(context):
    context.browser.find_element_by_css_selector('body > div.chik-header > div.top-header-container > a.email-out').click()

    print(u'STEP: When The user clicks on the Email Icon')


@then("The user should be redirected to another page to sign in")
def step_impl(context):
    main_window = context.browser.window_handles
    context.browser.switch_to_window(main_window[1])
    title = context.browser.title
    if "Sign in to Outlook" in title:
        print (title, " - Yes, we are on the right page!")
    eyes.open(context.browser, "CFAHome", "EMail Check")
    eyes.match_level = MatchLevel.LAYOUT
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + "EMAIL CHECK", Target.window())

    # # End the test.
    eyes.close()

    context.browser.switch_to_window(main_window[0])
    print(u'STEP: Then The user should be redirected to another page to sign in')


@when("I click on a link to a (?P<report_tool>.+)")
def step_impl(context, report_tool):
    context.browser.find_element_by_css_selector("#txtSearch").send_keys(report_tool)
    context.browser.find_element_by_css_selector("#searchSection > ul > li:nth-child(1) > a").click()

    #context.browser.implicitly_wait(500)
    link = context.browser.find_element_by_css_selector("div[class$='source-title']")
    link.click()


    print("STEP: When I click on a link to a", report_tool)

@then("I should be redirected to a new tab")
def step_impl(context):

    main_window = context.browser.window_handles
    if len(main_window) >1:

        context.browser.switch_to_window(main_window[1])
        title = context.browser.title
        print(title)

    eyes.open(context.browser, "CFAHome", "Opening in new tab - check")
    eyes.match_level = MatchLevel.LAYOUT
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + "Opening in new tab - Check", Target.window())

    # # End the test.
    eyes.close()


    print(u'STEP: Then I should be redirected to a new tab')

