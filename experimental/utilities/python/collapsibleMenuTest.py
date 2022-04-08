from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "http://localhost:3000/introduction/"
driver = webdriver.Firefox()
driver.get(url)

menuToggleClose = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/button')
menuToggleClose.click()
sleep(0.5) # give time for the new element to be rendered
menuToggleOpen = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div[2]')
menuToggleOpen.click()

preface = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[1]/a')
preface.click()

step1 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[2]/a')
step1.click()

step2 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[3]/a')
step2.click()

step3 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[4]/a')
step3.click()

step4 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[5]/a')
step4.click()

algoTips = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[6]/a')
algoTips.click()

misc = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/aside/div/nav/ul/li[7]/a')
misc.click()