##import webdriver from selenium
from selenium import webdriver
##import Select from selenium to use for selecting items from dropdown list
from selenium.webdriver.support.ui import Select
##import python unittest framework
import unittest
##import SiteElements class
from SiteModel import SiteElements
##create an instance of SiteElements Class
siteElements = SiteElements(webdriver)

##Login Function
def login():
    ##navigate to the mahara test demo site
    siteElements.driver.get("http://demo.mahara.org")
    ##print site title
    print siteElements.driver.title
    ##input username "student2" in the username field
    siteElements.get_user_name_element().send_keys("student2")
    ##input password "Testing1" in the password field
    siteElements.get_user_password_element().send_keys("Testing1")
    ##click on the submit button
    siteElements.get_login_button_element().click()
    ##check if logout link displayed
    islogoutvisible = siteElements.get_logout_link().is_displayed()
    ##print check status
    print "logout link display", islogoutvisible
    ## return login status
    return islogoutvisible

##Logout Function
def logout():
    ##click logout link
    siteElements.get_logout_link().click()
    ##check if username text field is displayed after logout
    isLoginVisible = siteElements.get_user_name_element().is_displayed()
    ##print display status
    print "login user name field display", isLoginVisible
    ##return logout status
    return isLoginVisible
##check hide real user name function
def hide_real_name_user_setting():
    ##click on the settings link
    siteElements.get_setting_link_element().click()
    ##check on the hide real user name checkbox
    siteElements.get_hide_real_name_checkbox_element().click()
    ##click on the preference save button
    siteElements.get_save_setting_button_element().click()
    ##wait about 10 seconds
    siteElements.driver.implicitly_wait(10)
    ##get save confirmation message
    confirmationtext=siteElements.get_preference_saved_message().text
    ##return confirmation status message
    return confirmationtext
##sort group name by "Latest Joined" function
def sort_group_name():
    ##click on the settings link
    siteElements.get_setting_link_element().click()
    ##select "Latest Joined" label from the group sort dropdown list
    Select(siteElements.get_group_name_sort_by_dropdown_element()).select_by_visible_text("Latest joined")
    ##click on the preference save button
    siteElements.get_save_setting_button_element().click()
    ##wait about 10 seconds
    siteElements.driver.implicitly_wait(10)
    ##get save confirmation message
    confirmationmessage=siteElements.get_preference_saved_message().text
    ##return confirmation status message
    return confirmationmessage

##Test Runner Class to run the test
class TestRunner(unittest.TestCase):
    ##class level test setup for maximize window and login
    @classmethod
    def setUpClass(cls):
        siteElements.driver.maximize_window()
        login()

##Test Hide Read User Name Settings Change
    def test_hide_real_name_user_settings(self):
        self.assertEqual(hide_real_name_user_setting(),"Preferences saved")
##Test Sort Group Name Settings Change
    def test_sort_group_name(self):
        self.assertEqual(sort_group_name(),"Preferences saved")
##class levvel test teardown logout and close browser
    @classmethod
    def tearDownClass(cls):
        logout()
        siteElements.driver.close()
##run the main test
if __name__ == "__main__":
    unittest.main()