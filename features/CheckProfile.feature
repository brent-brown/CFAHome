# Created by brent.brown at 1/11/20
Feature: Check User's Profile
  # Enter feature description here

  Scenario: Profile Checker
    Given I am on the CFAHome Page
    When I click on the user Icon
    Then I should be on the User Profile page

    # Enter steps here