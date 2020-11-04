from selenium import webdriver


class FooterNav:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def home_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[1]/a")

    def about_us_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[2]/a")

    def contact_us_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[3]/a")

    def privacy_policy_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[4]/a")

    def terms_conditions_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[5]/a")

    def disclaimer_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[6]/a")

    def cookies_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[7]/a")

    def sitemap_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[8]/a")

    def refund_policy_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[9]/a")

    def make_payment_link(self):
        return self.driver.find_element_by_xpath("//ul[@class='footermenu']/li[10]/a")

    def facebook_link(self):
        return self.driver.find_element_by_xpath("//div[@class='col-12 col-md-4 sociali rspdl0 rspdr0']/a[1]")

    def twitter_link(self):
        return self.driver.find_element_by_xpath("//div[@class='col-12 col-md-4 sociali rspdl0 rspdr0']/a[2]")

    def pinterest_link(self):
        return self.driver.find_element_by_xpath("//div[@class='col-12 col-md-4 sociali rspdl0 rspdr0']/a[4]")

    def instagram_link(self):
        return self.driver.find_element_by_xpath("//div[@class='col-12 col-md-4 sociali rspdl0 rspdr0']/a[5]")





