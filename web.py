#This program will log in to your ACORN profile, and tell you how much money you owe to the UofT, how much (if any) awards (scolarships, UTAPS, etc) you will be getting, and the net amount you owe (or don't owe)

from selenium import webdriver
from time import sleep

class WebBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login_and_check_owing(self):
        self.driver.get('https://www.acorn.utoronto.ca/')

        #Click on the login button
        login_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/p[2]/a')
        login_button.click()

        #Enter the username and password
        username_field = self.driver.find_element_by_xpath('//*[@id="username"]')
        
        # YOUR UTORID GOES HERE
        username_field.send_keys('')

        password_field = self.driver.find_element_by_xpath('//*[@id="password"]')
        
        # YOUR PASSWORD GOES HERE
        password_field.send_keys('')

        #Click the login button to log in
        enter = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/form/button')
        enter.click()

        #Wait 1s for the xPath to fully load in
        sleep(1)

        #Get the amount owing
        amount_owing = self.driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[1]/a').text
        
        #Print the amount owing
        print('You owe: ' + amount_owing)
        return amount_owing
        
    def upcoming_awards(self):
        upcoming_awards = self.driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[2]/div[6]/div[3]/div/div[2]').text
        print("You're getting: " + upcoming_awards)
        return upcoming_awards
        
    def calculate_net(self):
        
        a = self.driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[1]/a').text
        
        b = self.driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[2]/div[6]/div[3]/div/div[2]').text
        
        #Remove the dollar signs
        owe = a.strip("$")
        get = b.strip("$")
        
        #Remove the comma (otherwise can't convert to float)
        owe = owe[:1] + owe[2:]
        get = get[:1] + get[2:]
        
        #How much you owe (>0=you owe, <0=you're in surplus)
        net = float(owe)-float(get)
        
        if net<0:
            print("You are in surplus of: " + str(float(get)-float(owe)))
        else:
            print("You're net owing is: " + str(net))


bot = WebBot()
bot.login_and_check_owing()
bot.upcoming_awards()
bot.calculate_net()