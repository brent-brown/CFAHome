# Created by brent.brown at 1/14/20h
Feature: Check Bookmark Page
  # Enter feature description here
  
@demo
  Scenario: Checking contents of bookmark page
    Given I am on the CFAHome Page
    When I click on the "Bookmark" icon
    And I am on the bookmark page
    Then The user should be able to view their bookmarks

    # Enter steps here