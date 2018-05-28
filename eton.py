import json
import requests
import os

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('--headless')

chrome_options.add_argument(
    'blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度

profile_dir = os.getenv('localappdata') + '\\Google\\Chrome\\User Data'
# chrome_options.add_argument("user-data-dir="+profile_dir)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
'''
#headerContainer > div > div.leftColumnContent > a > img
#headerContainer > div > div.rightColumnContent
#headerContainer > div > div.rightColumnContent > h1
#techspecstab > div
#techspecstab > div > table.dataTableNew > tbody > tr:nth-child(5) > td:nth-child(1)
#featurestab > div
#documentationtab > div.tabbed_data
#ctl00_ContentBodyProducts_ctl01_tblItems > tbody > tr.tdSelectorClass_9 > td:nth-child(2)
'''
'''
#ProductImageDiv
#ctl00_ContentBody_pnlMainArea
#ctl00_ContentBody_pnlMainArea > div:nth-child(1) > h1
#productdescription
'''
js_executeScript="document.getElementById('featurestab').removeAttribute('display');"

def pnlMainArea(driver):
    ProductImageDiv = driver.find_element_by_css_selector('#ProductImageDiv')
    ContentBody = driver.find_element_by_css_selector(
        '#ctl00_ContentBody_pnlMainArea')
    h1 = ContentBody.find_element_by_css_selector('div:nth-child(1) > h1').text
    productdescription = ContentBody.find_element_by_css_selector(
        '#productdescription').text
    ProductImageDiv_i = ProductImageDiv.get_attribute('innerHTML')
    ContentBody_innerhtml = ContentBody.get_attribute('innerHTML')
    with open(productdescription+'-'+h1+'.html', 'a+', encoding='u8')as a:
        a.write(ProductImageDiv_i)
        a.write(ContentBody_innerhtml)


def eton(driver):
    img = driver.find_element_by_css_selector(
        '#headerContainer > div > div.leftColumnContent > a > img')
    rightColumnContent = driver.find_element_by_css_selector(
        '#headerContainer > div > div.rightColumnContent')
    techspecstab = driver.find_element_by_css_selector('#techspecstab > div')
    featurestab = driver.find_element_by_css_selector('#featurestab > div')
    documentationtab = driver.find_element_by_css_selector(
        '#documentationtab > div.tabbed_data')

    rightColumnContent_innerhtml = rightColumnContent.get_attribute(
        'innerHTML')
    techspecstab_innerhtml = techspecstab.get_attribute('innerHTML')
    featurestab_innerhtml = featurestab.get_attribute('innerHTML')

    h1 = rightColumnContent.find_element_by_css_selector('h1').text
    with open(h1+'.html', 'a+', encoding='u8')as op:
        op.writelines([rightColumnContent_innerhtml,
                       techspecstab_innerhtml, featurestab_innerhtml])

    UPS = techspecstab.find_elements_by_css_selector(
        'tbody > tr > td:nth-child(1) > a')
    print(UPS[0])
    herf = ['http://powerquality.eaton.com.cn' +
            u.get_attribute('href') for u in UPS]
    img_src = img.get_attribute('src')
    with open(img_src.split('/')[-1], 'wb') as jpg:
        r = requests.get(img_src)
        jpg.write(r.content)

    documentationtab_a = documentationtab.find_elements_by_css_selector('a')
    js_executeScript="document.getElementById('documentationtab').removeAttribute('style');"
    driver.execute_script(js_executeScript)
    for da in documentationtab_a:
        try:
            da.get_attribute('data-status')
        except Exception as e:
            print(e)
        else:
            if da.get_attribute('data-status') == '+':
                da.click()
    documentationtab_d_a = documentationtab.find_elements_by_css_selector('a')
    with open('documentationtab.txt', 'a+', encoding='u8')as sd:
        for dda in documentationtab_d_a:
            print(dda)
            if dda.get_attribute('href') is not None:
                sd.write(dda.get_attribute('href'))

    try:
        driver.find_element_by_css_selector(
            '#ImageBar > li:nth-child(1) > a').click()
    except Exception as e:
        print(e)
    else:
        more_imgs = driver.find_elements_by_css_selector('#cboxPhoto')
        more_img_src = [mi.get_attribute('src') for mi in more_imgs]
        # .split('/')[-1]
    for mis in more_img_src:
        fn = mis.split('/')[-1]
        r = requests.get(mis)
        with open(fn, 'wb')as jpg:
            jpg.write(r.content)
    for he in herf:
        driver.get(he)
        pnlMainArea(driver)


if __name__ == "__main__":
    with open('D:\\工作资料\\伊顿UPS\\ETON 不间断电源(UPS).txt', 'r', encoding='u8')as etons:
        eu = etons.readlines()
        for ue in eu:
            ue = ue.strip()
            driver.get(ue)
            eton(driver)
