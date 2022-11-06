Feature: Activities

  Background: user is able to access activities module in book my show application
    Given user is able to launch the browser
    When user is able to enter the url
    When user is able to click on activities
    Then user is able to select one activity
    And user is able to book the activity
    Then user is able to slect date and time
    And user is able to click on continue
    Then user is able to add the ticket
    Then user is able to select the ticket
    And user is able to click on proceed

  Scenario Outline:
    Then user is able to enter the full name "<full_name>"
    And user is able to enter the "<mobile_number>"
    Then user is able to enter the email address "<email_address>"
    And user is able to click on checkbox
    Then user is able to click on submit
    And user is able to click on proceed to pay
    Then user is able to enter the mobile number into textfield "<mobile_number>"
    And user is able to click on continue button


    Examples:
      |full_name            | |mobile_number | |email_address            |
      |shaik mahammad sohail| |9121694697    | |sohelshaik1742@gmail.com |
      |suvarna              | |9353781139    | |shjsdkj@gmail.com        |
      |sri                  |  |98765432     | |sri9343        |
      |anu                  |  |9113676419   | |anuj@gmail.com           |