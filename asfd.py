import selenium
import selenium.webdriver
import re


def getNumberByName(name):
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500&jl=%E5%8C%97%E4%BA%AC&kw=" + name + "&sm=0&p=1"
    # 调用firefox
    driver = selenium.webdriver.Chrome(r"D:\python file\chromedriver_win32\chromedriver.exe")
    # 调用url
    driver.get(url)
    # 网页源代码
    pagesource = driver.page_source
    restr = "<em>(\\d+)</em>"
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()
    return mylist[0]


namelist = ["java", "python", "php"]

for str in namelist:
    print(getNumberByName(str))
