import os

import applitools
# from applitools.common import BatchInfo
# from selenium import webdriver
# from applitools.selenium import Eyes



eyes = Eyes()
batch_info = BatchInfo('CFAHome - Search Batch')
eyes.batch = batch_info

# Initialize the eyes SDK and set your private API key.
eyes.api_key = os.environ['APPLITOOLS_API_KEY']
#eyes.api_key = 'Q9IT3T103XThPKgfJV21YwfRxdhyw109Ug97TM4YEtmg1HZw110'

#Sauce Labs Credentials
SAUCE_USERNAME = 'sso-chick-fil-a-brent.brown'
SAUCE_ACCESS_KEY = '8963a173-6756-41db-8a8d-0f00417bd859'
# capabilities = \
#     {
#         'browserName': 'chrome',
#         'browserVersion': 'latest',
#         'platformName': 'OS X 10.11',
#         'sauce:options': {
#             'name': 'Testing Selenium with Behave - Chrome',
#         }}


capabilities = {
  'browserName':'Chrome',
  'platform':'OS X 10.11',
  'version':'latest',
  'name':'CFAHome -Search - Chrome (MAC OSX 10.11)'
}

print(capabilities['browserName'])
def before_all(context):



    print("Executing before all")


def before_feature(context, feature):







    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):


    context.browser = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %
                         (SAUCE_USERNAME, SAUCE_ACCESS_KEY)

    )

    id = context.browser.session_id
    #eyes.open(context.browser, "CFAHome","hh")

    print('Link to your job: https://saucelabs.com/jobs/%s' % id)

    # eyes.open(context.browser, "CFAHome","Search")
    context.browser.get("https://int.portal.cfahome.com")
    context.browser.implicitly_wait(500)

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




    print("Before scenario\n")


def after_scenario(context, scenario):
    #eyes.close()
    context.browser.quit()

    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")
