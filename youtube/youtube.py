# coding=utf-8

import requests
import pickle
import os
import json
import time
import traceback
from bs4 import BeautifulSoup as BS4

import config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["PATH"] += ":"+os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/libs"


def restart():
    global br
    try:
        br.close()
    except:
      # br = webdriver.PhantomJS()
       br = webdriver.Firefox()
       login()

def login():



    br = webdriver.Firefox()
    br.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26hl%3Den%26action_handle_signin%3Dtrue%26next%3D%252Ffeed%252Fhistory')

    try:
        br.find_element_by_id('Email').send_keys(config.youtube_username)
        br.find_element_by_id('next').click()

        WebDriverWait(br, 10).until(
            EC.presence_of_element_located((By.ID, "Passwd"))
        )
        br.find_element_by_id('Passwd').send_keys(config.youtube_password)
        br.find_element_by_id('signIn').click()

        WebDriverWait(br, 10).until(
            EC.presence_of_element_located((By.ID, "yt-masthead-account-picker"))
        )
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            br.find_element_by_class("load-more-text").click()
            if newHeight == lastHeight:
                break
            lastHeight = newHeight
        
        br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(br, 10).until(
            EC.presence_of_element_located((By.text, "Load more"))   
        )
        br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        


    except Exception as e:
        print traceback.format_exc(e)
        br.save_screenshot('error.png')




if __name__ == '__main__':
    login()


