from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class Bot:    
    def __init__(self, config):
        self.options = ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--incognito')

        self.url = config['url']
        self.input_locator = (By.XPATH, config['input_locator'])
        self.output_locator = (By.XPATH, config['output_locator'])
    
    def fetch(self, question):
        with Chrome(options=self.options) as driver:
            driver.get(self.url)
            time.sleep(15)
            
            input_element = driver.find_element(*self.input_locator)
            input_element.clear()
            input_element.send_keys(question)
            time.sleep(2)
            input_element.send_keys(Keys.CONTROL + Keys.ENTER)
            
            time.sleep(15)
            try:
                output = driver.find_element(*self.output_locator).text
            except TimeoutException:
                output = "ERROR"
            
            # time.sleep(25)
        
        return output

def test():
    config1 = {
        'url': "https://uk6ks.aitianhu.fun/#/chat/1002",
        'input_locator': '//*[@id="app"]/div/div[1]/div/div/div/div/div/div/footer/div/div/div[4]/div/div[1]/div[1]/textarea',
        'output_locator': '//*[@id="image-wrapper"]/div/div[2]/div[2]/div/div[1]/div/div/div/p',
    }
    config2 = {
        'url': "https://13.nb8.ltd/index/1002",
        'input_locator': '//*[@id="app"]/div/div[2]/div/div/div/div/div/div/div/footer/div[2]/div/div[4]/div/div[1]/div[1]/textarea',
        'output_locator': '//*[@id="image-wrapper"]/div/div[2]/div[2]/div[2]/div[1]',
    }

    config3 = {
        'url': "https://chat.waixingyun.cn/#/chat/gpt/1002",
        'input_locator': '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div/div/footer/div/div[1]/div/div[1]/div[1]/textarea',
        'output_locator': '//*[@id="image-wrapper"]/div/div[2]/div[2]/div/div[1]/div/div/p',
    }

    config4 = {
        'url': "https://macll.cn/",
        'input_locator': '/html/body/main/astro-island/div/div[4]/textarea',
        'output_locator': '/html/body/main/astro-island/div/div[3]/div[1]/div[2]/p',
    }

    config5 = {
        'url': "http://chat.darkflow.top/",
        'input_locator': '//*[@id="app-body"]/div/div[3]/div[2]/textarea',
        'output_locator': '//*[@id="app-body"]/div/div[2]/div[3]/div/div[2]/div[2]/p',
    }

    config6 = {
        'url': "https://chat.z-pt.com/?ref=sidebarkok",
        'input_locator': '//*[@id="app-body"]/div[2]/div[4]/div[2]/textarea',
        'output_locator': '//*[@id="app-body"]/div/div[2]/div[3]/div/div[2]/div[2]/p',
    }

    b = Bot(config5)
    
    question_list = [
        '鲁迅和周树人的关系？',
        '小明有5个苹果，中午吃了2个，晚上小美送给小明8个，现在小明还有几个苹果？',
        '大后天是星期一，昨天是星期几？'
    ]
    answer_list = []
    for q in question_list:
        answer_list.append(b.fetch(q))

    print(answer_list)

if __name__ == '__main__':
    test()
