from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
WORD_SEARCHED='poop'
ALTERNATIVE='ABC'
NUMBER_OF_TRIES=3
NUMBER_OF_QUESTIONS=100
driver=webdriver.Firefox()
driver.get("http://www.googlefeud.com/")
while NUMBER_OF_QUESTIONS!=0:
    question_has_been_answered=False
    question_element =driver.find_element_by_xpath('//*[@id="cats"]/span[4]').click()
    counter=NUMBER_OF_TRIES;
    while counter!=0:
        if question_has_been_answered==False:
            question_string=driver.find_element_by_xpath('//*[@id="rebox"]').send_keys(WORD_SEARCHED)
        else:
            question_string=driver.find_element_by_xpath('//*[@id="rebox"]').send_keys(ALTERNATIVE)
        search_button=driver.find_element_by_xpath('//*[@id="guess"]').click()
        counter-=1
        time.sleep(2)
        answer=driver.find_elements_by_class_name('answered')
        if len(answer)!=0 and question_has_been_answered==False:
            print driver.find_element_by_id('queryspan').text
            question_has_been_answered=True
            counter+=1

    next_round=driver.find_element_by_xpath('//*[@id="message"]').click()
    NUMBER_OF_QUESTIONS-=1
    time.sleep(2)

