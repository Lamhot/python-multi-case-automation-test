##import webdriver from selenium
from selenium import webdriver
##define Site Elements Class
class SiteElements:
    ##Use Firefox Web Driver
    driver=webdriver.Firefox()
    ##initialize site elements object
    def __init__(self, driver=webdriver):

        print "this is site elements class for containing elements"

    ##user name text field
    def get_user_name_element(self):
        usernametextfield = self.driver.find_element_by_id("login_login_username")
        return usernametextfield

    ##password text field
    def get_user_password_element(self):
        userpassword = self.driver.find_element_by_id("login_login_password")
        return userpassword

    ##login button
    def get_login_button_element(self):
        loginbutton = self.driver.find_element_by_id("login_submit")
        return loginbutton

    ##logout link
    def get_logout_link(self):
        logoutlink = self.driver.find_element_by_link_text("Logout")
        return logoutlink
    ##setting link
    def get_setting_link_element(self):
        settinglink=self.driver.find_element_by_link_text("Settings")
        return settinglink
    ##hide real name check box
    def get_hide_real_name_checkbox_element(self):
        hiderealnamecheckbox=self.driver.find_element_by_id("accountprefs_hiderealname")
        return hiderealnamecheckbox
    ##save settings button
    def get_save_setting_button_element(self):
        savebutton=self.driver.find_element_by_id("accountprefs_submit")
        return savebutton
    ##group name sort by drop downlist
    def get_group_name_sort_by_dropdown_element(self):
        groupnamedropdownelement=self.driver.find_element_by_id("accountprefs_groupsideblocksortby")
        return groupnamedropdownelement
    ##preference saved message
    def get_preference_saved_message(self):
        messageelement=self.driver.find_element_by_xpath("//div[@class='ok']")
        return messageelement