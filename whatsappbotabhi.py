from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re

chrome_browser = webdriver.Chrome(
        executable_path='WhatsApp-Chatbot-master/WhatsApp-Chatbot-master/driver/chromedriver_win32/chromedriver.exe')

chrome_browser.get('https://web.whatsapp.com/')
time.sleep(5)
chrome_browser.switch_to_window(chrome_browser.window_handles[1])
chrome_browser.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
time.sleep(5)
chrome_browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
chrome_browser.switch_to_window(chrome_browser.window_handles[0])    

time.sleep(20)






user_name='Shivam'
user= chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()



time.sleep(30)

#COPY FROM HERE

ip_msg = chrome_browser.find_elements_by_class_name('_3Whw5')
j=-1
msg = ip_msg[j].text
   
print(msg)
     
'''
whatsapp_input=chrome_browser.find_element_by_class_name('_2UL8j')
whatsapp_input.click()
intro="Hello there I'm his assistant Mitsuku, Abhishek is busy, if the thing you wanna talk is urgent then please call him"
whatsapp_input.send_keys(intro)
whatsapp_send=chrome_browser.find_element_by_class_name('_1U1xa')
whatsapp_send.click()
'''
     
chrome_browser.switch_to_window(chrome_browser.window_handles[1])


'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(chrome_browser, 20)

chrome_browser.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pb-widget__description__chat-now__button')))

chrome_browser.execute_script("window.stop();")
'''
#time.sleep(20)
bot= chrome_browser.find_element_by_class_name('pb-widget__description__chat-now__button')
bot.click()



time.sleep(5)
bot_input= chrome_browser.find_element_by_id('pb-widget-input-field')
bot_input.click()

bot_input.send_keys(msg)

time.sleep(5)
bot_input= chrome_browser.find_element_by_class_name('pb-widget__input__send__container')
bot_input.click()




op_bot = chrome_browser.find_elements_by_class_name('pb-chat-bubble__bot')
bot_output="Mitsuku: "+op_bot[-1].text
print(bot_output)

chrome_browser.switch_to_window(chrome_browser.window_handles[0])

whatsapp_input=chrome_browser.find_element_by_class_name('_2UL8j')
whatsapp_input.click()
whatsapp_input.send_keys(bot_output)



whatsapp_send=chrome_browser.find_element_by_class_name('_1U1xa')
whatsapp_send.click()


prev_msg=msg
'''
whatsapp_input=chrome_browser.find_element_by_id('_3FRCZ')
whatsapp_input.click()
'''




a=True
while a:
    chrome_browser.switch_to_window(chrome_browser.window_handles[0]) 
    ip_msg = chrome_browser.find_elements_by_class_name('_3Whw5')
    msg = ip_msg[-1].text
    if msg==bot_output:
        msg=ip_msg[-2].text
    else:
        pass
   # x = re.findall("^$",msg)
    #if x:
     #   if type(msg)==str:
    #msg=msg[1:]     
    #print(msg)
    
    if(msg==prev_msg):
        continue
    else:
        chrome_browser.switch_to_window(chrome_browser.window_handles[1])
        
        '''bot= chrome_browser.find_element_by_class_name('pb-widget__description__chat-now__button')
        bot.click()'''



        time.sleep(5)
        bot_input= chrome_browser.find_element_by_id('pb-widget-input-field')
        bot_input.click()
    
        bot_input.send_keys(msg)

        time.sleep(5)
        bot_input= chrome_browser.find_element_by_class_name('pb-widget__input__send__container')
        bot_input.click()



        time.sleep(5)
        op_bot = chrome_browser.find_elements_by_class_name('pb-chat-bubble__bot')
        bot_output="Mitsuku: "+op_bot[-1].text
        print(bot_output)

        chrome_browser.switch_to_window(chrome_browser.window_handles[0])

        whatsapp_input=chrome_browser.find_element_by_class_name('_2UL8j')
        whatsapp_input.click()
        whatsapp_input.send_keys(bot_output)


    
        whatsapp_send=chrome_browser.find_element_by_class_name('_1U1xa')
        whatsapp_send.click()
        prev_msg=msg
        
    