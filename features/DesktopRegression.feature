# Created by brent.brown at 2/18/20
Feature: Desktop Regression
  # Enter feature description here

  Scenario Outline: Search results check - Exact Match
    Given I am on the CFAHome webpage
    When I search for <items>
    Then I should see <items> in the search results
   Examples: Search Items
      | items                   |
      | Chicken Supply          |
      | Lemon Juicers Program   |

  Scenario: Logout Check
    Given I am on the CFAHome webpage
    When I click logout
    Then I should be logged out of the application

  Scenario: User Profile Check
    Given I am on the CFAHome webpage
    When I click on the user Icon
    Then I should be on the User Profile page
    Then I should see the Profile, Account Settings, and Update Information links

  Scenario: Checking contents of bookmark page
    Given I am on the CFAHome webpage
    When I click on the "Bookmark" icon
    And I am on the bookmark page
    Then The user should be able to view their bookmarks

  Scenario: Email Check
    Given I am on the CFAHome webpage
    When The user clicks on the Email Icon
    Then The user should be redirected to another page to sign in

  Scenario Outline: Opening in new tab - Check
    Given I am on the CFAHome webpage
    When I click on a link to a <report_tool>
    Then I should be redirected to a new tab
    Examples: Search Items
       | report_tool             |
       | Backstage Tour          |
       | BlueJeans               |

