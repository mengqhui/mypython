import os
import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#chrome_options.add_argument('--headless')

chrome_options.add_argument(
    'blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度

profile_dir = os.getenv('localappdata') + '\\Google\\Chrome\\User Data'
# chrome_options.add_argument("user-data-dir="+profile_dir)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)


def pnlMainArea(driver):
    h1 = driver.find_element_by_css_selector(
        '#headerContainer > div > div.rightColumnContent > h1').text
    js_executeScript = "document.getElementById('documentationtab').removeAttribute('style');"
    driver.execute_script(js_executeScript)
    time.sleep(30)
    documentationtab_a = driver.find_elements_by_xpath(
        "//a[contains(@id, 'hgcCategoryContainerHeaderLink')]")

    documentationtab = driver.find_element_by_css_selector(
        '#documentationtab > div.tabbed_data')
    documentationtab_a.reverse()
    for da in documentationtab_a:
        print(da.text)
        try:
            da.get_attribute('data-status')
        except Exception as e:
            print(e)
        else:
            if da.get_attribute('data-status') == '+':
                da.click()
                time.sleep(10)
    # ctl00_ContentBodyProducts_ctl04_tblItems > tbody > tr.tdSelectorClass_84 > td:nth-child(2) > a
    documentationtab_a = documentationtab.find_elements_by_xpath(
        "//a[contains(@href, 'http://lit.powerware.com/ll_download.asp?')]")

    documentationtab_d_a = [dda.get_attribute(
        'href') for dda in documentationtab_a]
    #driver.quit()
    return (h1, documentationtab_d_a)


def download_p(a):
    d_b = 'D:\\工作资料\\伊顿UPS\\'+a[0]
    prefs = {'download.default_directory': d_b}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    for bb in a[1]:
        print(bb)
        driver.get(bb)
    driver.quit()

if __name__ == "__main__":
    with open('D:\\工作资料\\伊顿UPS\\ETON 不间断电源(UPS).txt', 'r', encoding='u8') as etons:
        eu = etons.readlines()
        for ue in eu:
            ue = ue.strip()
            driver.get(ue)
            ddda = pnlMainArea(driver)
            download_p(ddda)
