import os
from selenium import webdriver
from applitools.selenium import Eyes, Target


# Initialize the eyes SDK and set your private API key.
keys = os.environ['APPLITOOLS_API_KEY']

print(keys)
#print(os.environ.keys())