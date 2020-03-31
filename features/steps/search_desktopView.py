

from applitools.common import MatchLevel
from behave import *

import features.environment
from features.pages.CFAHomePageObjects import *
from applitools.selenium import Eyes, Target
import applitools.selenium


use_step_matcher("re")


@given("I am on the CFAHome webpage")
def step_impl(context):

    # popUpMessage = context.browser.find_element_by_css_selector("#wm-shoutout-170936")
    # context.browser.implicitly_wait(500)
    # if popUpMessage.is_displayed():
    #     context.browser.find_element_by_css_selector(
    #         '#wm-shoutout-170936 > div.wm-content > div.buttons-wrapper > span').click()
    # else:
    #     return

    welcome = context.browser.find_element_by_css_selector('body > div.chik-header > div > a.logo-container > img')
    # content = context.browser.find_element_by_css_selector('div.prefName')
    if welcome.is_displayed():
        print('STEP: I am on the CFAHome Page')
    else:
        print('STEP: I am NOT on the CFAHome Page')





@then('I should see "All" search bucket header')
def step_impl(context):
    #print(Locators.ALL_BUCKET)
    if context.browser.find_element_by_css_selector("body > header > div > div:nth-child(1) > a").is_displayed():

    # and context.browser.find_element_by_css_selector(Locators.PEOPLE) \
    # and context.browser.find_element_by_css_selector(Locators.NEWS) \
    # and context.browser.find_element_by_css_selector(Locators.RESOURCES) \
    # and context.browser.find_element_by_css_selector(Locators.REPORTS_TOOLS):

    #eyes.open(context.browser, "CFAHome", "All Search Bucket")
    # eyes.force_full_page_screenshot = True

    # eyes.check(context.browser.current_url, Target.window())
    # # End the test.
    # eyes.close()
        print("All Bucket Header Found")

    else:

    # eyes.open(context.browser, "Search - Desktop", "Search Buckets - No filters selected")
    # eyes.force_full_page_screenshot = True

    # eyes.check("Search " + Locators.ALL_BUCKET.text() + " Not found", Target.window())
    # # End the test.
    # eyes.close()

        print ("Something is missing")


@step('I should see "People" search bucket header')
def step_impl(context):
    if context.browser.find_elements_by_css_selector('#bcktPeople'):
        print("People Search Bucket Found")

    # eyes.open(context.browser, "Search", "All - Desktop View", {'width': 800, 'height': 600})
    # eyes.force_full_page_screenshot = True

    # eyes.check(context.browser.current_url +" People Search Bucket", Target.window())
    # # End the test.
    # eyes.close()

    else:
        #eyes.open(context.browser, "Search", "All - Desktop View - Error")
        # eyes.force_full_page_screenshot = True
        # eyes.check("Search " + "People Search Bucket -  Not found", Target.window())
        # # End the test.
        # eyes.close()

        return ("Something is missing")


@step('I should see "Locations" search bucket header')
def step_impl(context):
    if context.browser.find_element_by_css_selector('#bcktLocations'):
        return True
        # eyes.open(context.browser, "Search", "All - Desktop View", {'width': 800, 'height': 600})
        # eyes.force_full_page_screenshot = True

        # eyes.check(context.browser.current_url +" Locations Search Bucket", Target.window())
        # # End the test.
        # eyes.close()

    else:
        # eyes.open(context.browser, "Search", "All - Desktop View - Error")
        # eyes.force_full_page_screenshot = True
        # eyes.check("Search " + Locators.LOCATIONS + " Not found", Target.window())
        # # End the test.
        # eyes.close()

        return ("Something is missing")


@step('I should see "Reports and Tools" search bucket header')
def step_impl(context):
    if Locators.ALL_BUCKET and Locators.REPORTS_TOOLS:
        return True
        # eyes.open(context.browser, "Search", "All - Desktop View", {'width': 800, 'height': 600})
        # eyes.force_full_page_screenshot = True

        # eyes.check(context.browser.current_url, Target.window())
        # # End the test.
        # eyes.close()

    else:
        eyes.open(context.browser, "Search", "All - Desktop View - Error")
        eyes.force_full_page_screenshot = True
        eyes.check("Search " + Locators.REPORTS_TOOLS + " Not found", Target.window())
        # # End the test.
        eyes.close()

        # return ("Something is missing")


@step('I should see "Resources" search bucket header')
def step_impl(context):
    if context.browser.find_element_by_css_selector(
            '#search-page > article > section > div.search-heading-divider > div.search-heading-container > h3'):
        print("it ie displayed")

        # eyes.open(context.browser, "Search", "All - Desktop View", {'width': 800, 'height': 600})
        # eyes.force_full_page_screenshot = True

        # eyes.check(context.browser.current_url + " Resource Header", Target.window())
        # # End the test.
        # eyes.close()

    else:
        eyes.open(context.browser, "Search", "All - Error")
        # eyes.force_full_page_screenshot = True
        eyes.check("Search " + Locators.RESOURCES + " Not found", Target.window())
        # # End the test.
        eyes.close()

        return ("Something is missing")


@step('I should see "News" search bucket header')
def step_impl(context):
    if Locators.ALL_BUCKET and Locators.NEWS:
        print()
    # return True
    # eyes.open(context.browser, "Search", "All - Desktop View", {'width': 800, 'height': 600})
    # eyes.force_full_page_screenshot = True
    # eyes.check(context.browser.current_url + " News Header", Target.window())
    # #eyes.check("Search - ALL", Target.window())
    # # End the test.
    # eyes.close()


    else:



        return ("Something is missing")


@when("I am on the Search page")
def step_impl(context):
    context.browser.find_element_by_css_selector("#searchSection > img.search-icon").click()
    context.browser.implicitly_wait(1500)
    title = context.browser.title
    # assert "Search" in title
    # eyes.branch_name = "Search"
    # eyes.open(context.browser, "CFAHome", "Search Page")
    # eyes.force_full_page_screenshot = True
    ##eyes.check(context.browser.current_url + " On Search Page", Target.window())
    # # End the test.
    # eyes.close()

    print(u'STEP: When I am on the Search page')


@then("The user is on the search page")
def step_impl(context):
    eyes.open(context.browser, "CFAHome", "Search Buckets - No filters selected")
    eyes.match_level = MatchLevel.LAYOUT
    eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + " Search P", Target.window())

    # # End the test.
    eyes.close()


@step("I navigate to the search Page")
def step_impl(context):
    # eyes.check(context.browser.current_url + " Navigating to Search Page", Target.window())

    context.browser.find_element_by_css_selector('#searchSection > img.search-icon').click()
    context.browser.implicitly_wait(500)

    #For SAFARI
    # popUpMessage = context.browser.find_element_by_css_selector("#wm-shoutout-170936")
    # context.browser.implicitly_wait(500)
    # if popUpMessage.is_displayed():
    #     context.browser.find_element_by_css_selector(
    #         '#wm-shoutout-170936 > div.wm-content > div.buttons-wrapper > span').click()
    # else:
    #     return

    print('STEP: And I navigate to the search Page')


@when("I view the left side of the Page")
def step_impl(context):
    if context.browser.find_element_by_css_selector('div:nth-child(2) > div.filter-block > label:nth-child(2) > span'):
        if context.browser.find_element_by_css_selector(
                'div:nth-child(2) > div.filter-block > label:nth-child(1) > span'):
            if context.browser.find_element_by_css_selector(
                    'div:nth-child(2) > div.filter-block > label:nth-child(3) > span'):
                print("All Exist")
                # eyes.check(context.browser.current_url + " Left Menu is visible", Target.window())

                # print(context.browser.find_element_by_css_selector(Locators.CATEGORYTYPE).text)

    else:
        # eyes.check(context.browser.current_url + " Left Menu is not visible", Target.window())
        print("something is missing")

    print('STEP: When I view the left side of the Page')


@then('I should see the "Person Type","Location Type", "Resource Type","Categories" and "Tags" filter')
def step_impl(context):
    title = context.browser.title
    assert "Person" in context.browser.find_element_by_css_selector(Locators.PERSONTYPE).text
    assert "Location" in context.browser.find_element_by_css_selector(Locators.LOCATIONTYPE).text
    assert "Resource" in context.browser.find_element_by_css_selector(Locators.RESOURCETYPE).text
    assert "Categories" in context.browser.find_element_by_css_selector(Locators.CATEGORYTYPE).text
    assert "Tags" in context.browser.find_element_by_css_selector(Locators.TAGSTYPE).text

    eyes.open(context.browser, "CFAHome", "Search Filters - No filters selected")
    # Take Screenshot
    eyes.match_level = MatchLevel.LAYOUT
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url, Target.window())
    # # End the test.
    eyes.close()

    print(
        u'STEP: Then I should see the "Person Type","Location Type", "Resource Type","Categories" and "Tags" filter')


@step('I have selected the "Contractor" Person Type filter')
def step_impl(context):
    context.browser.find_element_by_css_selector(Locators.contractorBox).click()
    context.browser.implicitly_wait(500)

    print(u'STEP: And  I have selected the "Contractor" Person Type filter')


@then('I should see the "contractor" filter selected')
def step_impl(context):

    if context.browser.find_element_by_css_selector('#srchBucketMore').is_displayed():

    # staff_type = context.browser.find_elements_by_css_selector('div[class="card-id"]')
    # #print(staff_type)
    # while context.browser.find_element_by_css_selector('#srchBucketMore').is_displayed():
    #     context.browser.find_element_by_css_selector('#srchBucketMore').click()
    # else:
    #     for i in staff_type:
    #         if i.text == "Contractor":
    #             continue
    #         else:
    #             print(i.text, "Shouldn't be listed")
    #         print(i.text)
    #
    # # context.browser.find_element_by_css_selector('div[class="card-id"]')
        print(u'STEP: Then I should see the "contractor" filter selected')


@step('I should see "Department field" filters')
def step_impl(context):
    eyes.open(context.browser, "CFAHome", "Department Filter Selected")
    #eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + " Dept Field", Target.window())

    eyes.close()
    # print(Locators.DEPT_TYPE)
    if context.browser.find_element_by_css_selector(Locators.DEPT_TYPE).text == "Department":
        print("Right Page")




    else:
        print('Wrong Page')

    print(u'STEP: And I should see "Department field" filters')


@step('I have selected a "Location Type" filter')
def step_impl(context):
    context.browser.find_element_by_xpath('//span[contains(@class, "filter-text") and text() ="Dwarf House " ]').click()

    # print(filterType)
    # listFilter =[]
    # for i in filterType:
    #    listFilter.append(i.text)

    # context.browser.find_elements_by_css_selector(filterType[3]).click()

    print(u'STEP: And  I have selected a "Location Type" filter')


@then('I should see the "Location Type" filter selected')
def step_impl(context):
    if context.browser.find_element_by_xpath(
            '//span[contains(@class, "filter-text") and text() ="Dwarf House " ]').is_selected():
        print(u'STEP: Then I should see the "Location Type" filter selected')


@step('I should see a "State" filter')
def step_impl(context):
    if context.browser.find_element_by_xpath("//label[contains(@class, 'filter-item')]").is_displayed():
        print("Yup, its displayed.")
        # eyes.open(context.browser, "CFAHome", "Search Results - Location Type filter selected")

        # Take Screenshot
        # eyes.check(context.browser.current_url, Target.window())

        # # End the test.

        eyes.open(context.browser, "CFAHome", "Location Type Filter")
        #eyes.force_full_page_screenshot = True
        eyes.check(context.browser.current_url + " Location Type Filter", Target.window())
        eyes.close()

    print(u'STEP: And I should see a "State" filter')


@step("I have selected the 'Resource' search Bucket")
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/header/div/div[5]/a').click()

    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And  I have selected the \'Resource\' search Bucket')


@step('I have selected a "Resource Type" filter')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_element_by_css_selector(
        "#bcktResources").click()
    context.browser.implicitly_wait(500)
    # eyes.open(context.browser, "CFAHome", "Search Results - Resource Type filter selected")

    # Take Screenshot
    # eyes.check(context.browser.current_url, Target.window())

    # # End the test.
    # eyes.close()

    print(u'STEP: And I have selected a "Resource Type" filter')


@step('I should see "Categories" filter options')
def step_impl(context):
    assert context.browser.find_element_by_css_selector(
        '#search-page > aside > div:nth-child(3) > div.filter-heading').is_displayed()


    print(u'STEP: And I should see "Categories" filter options')


@step('I should see "Tags" filter options')
def step_impl(context):
    eyes.open(context.browser, "CFAHome", "Tags Filter")
    eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + " Tags Filter", Target.window())

    eyes.close()
    assert context.browser.find_element_by_xpath(
        '//div[contains(@class, "filter-heading") and text() = " Tags"]').is_displayed()

    print(u'STEP: And I should see "Tags" fitler options')


@step('I should see a "Resource type" filter selected')
def step_impl(context):
    context.browser.find_element_by_xpath(
        '//span[contains(@class, "filter-text") and text() = "Excel " ]').click()
    if context.browser.find_element_by_xpath(
            '//span[contains(@class, "filter-text") and text() = "Excel " ]').is_selected():
        print("it is selected")
    else:
        print('it is not selected')

    print(u'STEP: And I should see a "Resource type" filter selected')


@step('I should see several "Resources" appearing')
def step_impl(context):
    count = len(context.browser.find_elements_by_css_selector("#search-page > article > section"))

    if count > 1:
        print("multiple results found")
        # eyes.open(context.browser, "CFAHome", "Resource Type filter selected - Results")

        # Take Screenshot
        # eyes.check(context.browser.current_url, Target.window())

        # # End the test.
        # eyes.close()
    else:
        print("Hmmm not enough results found")
        # eyes.open(context.browser, "CFAHome", "Resource Type filter selected - ERROR")

        # Take Screenshot
        # eyes.check(context.browser.current_url, Target.window())

        # # End the test.
        # eyes.close()

    print(u'STEP: And I should see several "Resources" appearing')


@then("I should see a list of Resources")
def step_impl(context):
    count = len(context.browser.find_elements_by_xpath('//div[contains(@class, "source-title") ]'))
    if count > 1:
        print("resources found")
    else:
        print("Hmmm not enough resources found")

    print(u'STEP: Then I should see a list of Resources')

    eyes.open(context.browser, "CFAHome", "List Of Resources")
    eyes.force_full_page_screenshot = True
    eyes.check(context.browser.current_url + " List of Resources", Target.window())
    eyes.close()


@when("I have selected the 'News' search Bucket")
def step_impl(context):
    context.browser.find_element_by_css_selector('#bcktNews').click()

    print(u'STEP: When  I have selected the \'News\' search Bucket')


@step("I should see News results displaying")
def step_impl(context):
    if context.browser.find_element_by_css_selector('div.search-heading-container > h3').is_displayed():
        pass
    else:
        print("failed")

    print(u'STEP: And I should see News results displaying')


@step("I should see the most recent news appearing first")
def step_impl(context):
    newsCount = len(context.browser.find_elements_by_css_selector('div.article-date'))
    newsDate = context.browser.find_elements_by_css_selector('div.article-date')
    nn = []

    for i in newsDate:
        nn.append(i.text)
    print(nn)

    if nn[0] > nn[1]:
        print("most recent is displayed")
        eyes.open(context.browser, "CFAHome", "Most Recent News")

        # Take Screenshot
        eyes.check(context.browser.current_url + "Most recent news", Target.window())

        # # End the test.
        eyes.close()
    else:
        # eyes.open(context.browser, "CFAHome", "Search Results - News Search bucket selected - ERROR")

        # Take Screenshot
        # eyes.check(context.browser.current_url, Target.window())

        # # End the test.
        # eyes.close()
        return

    # print(newsCount)
    # if newsCount < 1:
    #     return Exception
    #
    #
    # else:
    #     print("News Count = ", newsCount)

    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And I should see the most recent news appearing first')


    @given("I am on the CFAHome Page")
    def step_impl(context):
        eyes.open(context.browser, "CFAHome", "Search - Desktop View")
        context.browser.get("https://int.portal.cfahome.com")
        context.browser.implicitly_wait(600)

        theUser = context.browser.find_element_by_xpath('//*[@id="okta-signin-username"]')
        theUser.clear()

        enterUN = os.environ['CFAUSER_ADMIN']
        theUser.send_keys(enterUN)

        passsword = context.browser.find_element_by_css_selector("#okta-signin-password")
        passsword.clear()
        enterPW = os.environ['CFAPW_ADMIN']
        passsword.send_keys(enterPW)

        context.browser.find_element_by_css_selector("#okta-signin-submit").click()
        context.browser.implicitly_wait(200)

        popUpMessage = context.browser.find_element_by_xpath('//*[@id="wm-shoutout-170936"]')
        context.browser.implicitly_wait(500)
        if popUpMessage.is_displayed():
            context.browser.find_element_by_css_selector(
                '#wm-shoutout-170936 > div.wm-content > div.buttons-wrapper > span').click()
        else:
            return

        welcome = context.browser.find_element_by_css_selector('body > div.chik-header > div > a.logo-container > img')
        # content = context.browser.find_element_by_css_selector('div.prefName')
        if welcome.is_displayed():
            print('STEP: I am on the CFAHome Page')
        else:
            print('STEP: I am NOT on the CFAHome Page')
