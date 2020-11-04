from selenium import webdriver


class CreateAnAccountPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def first_name_label(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/label[1]")

    def first_name_input_box(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@id='txtname']")

    def last_name_label(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/label[2]")

    def last_name_input_box(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@id='txtlastname']")

    def email_label(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/label[3]")

    def email_input_box(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@id='txtemail']")

    def password_label(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/label[4]")

    def password_input_box(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@id='txtpassword']")

    def create_account_button(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@value='Create an Account']")

    def already_register_link(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/input[@value='Already Registered? Login']")

    def first_name_container(self):
        return self.driver.find_element_by_xpath("//span[@id='nm']/ul/li")

    def last_name_container(self):
        return self.driver.find_element_by_xpath("//span[@id='nm1']/ul/li")

    def email_container(self):
        return self.driver.find_element_by_xpath("//div[@id='phn']/ul/li")

    def password_container(self):
        return self.driver.find_element_by_xpath("//div[@id='pass']/ul/li")

    def window(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']")

    def close_button(self):
        return self.driver.find_element_by_xpath("//div[@id='signup']/i")











