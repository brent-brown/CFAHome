# Created by brent.brown at 1/17/20
Feature: Search - Desktop View
  # Enter feature description here

  Scenario: Search Buckets - No filters selected
    Given I am on the CFAHome webpage
    When I navigate to the search Page
    Then I should see "All" search bucket header
    And I should see "People" search bucket header
    And I should see "Locations" search bucket header
    And I should see "Reports and Tools" search bucket header
    And I should see "Resources" search bucket header
    And I should see "News" search bucket header
    Then The user is on the search page

  Scenario: Search Filters - No filters selected
    Given I am on the CFAHome webpage
    And I navigate to the search Page
    When I view the left side of the Page
    Then I should see the "Person Type","Location Type", "Resource Type","Categories" and "Tags" filter

  Scenario: Search Results - Person Type filter selected
    Given I am on the CFAHome webpage
    When I am on the Search page
    And  I have selected the "Contractor" Person Type filter
    Then I should see the "contractor" filter selected
    And I should see "Department field" filters


  Scenario: Search Results - Location Type filter selected
    Given I am on the CFAHome webpage
    And I navigate to the search Page
    And  I have selected a "Location Type" filter
    Then I should see the "Location Type" filter selected
    And I should see a "State" filter

  Scenario: Search Results - Resource Type filter selected
    Given I am on the CFAHome webpage
    And I navigate to the search Page
    And  I have selected the 'Resource' search Bucket
    And I have selected a "Resource Type" filter
    And I should see "Categories" filter options
    And I should see "Tags" filter options

  Scenario: Search Results - Resource Type filter selected - Results
    Given I am on the CFAHome webpage
    And I navigate to the search Page
    And I have selected a "Resource Type" filter
    And I should see a "Resource type" filter selected
    And I should see several "Resources" appearing
    Then I should see a list of Resources

  Scenario: Search Results - News Search bucket selected
    Given I am on the CFAHome webpage
    And I navigate to the search Page
    When  I have selected the 'News' search Bucket
    And I should see "Categories" filter options
    And I should see "Tags" filter options
    And I should see News results displaying
    And I should see the most recent news appearing first





