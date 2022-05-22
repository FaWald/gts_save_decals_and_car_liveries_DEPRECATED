from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def print_hi(name):  # simple code to test
    print(f'Hi, {name}')


def selenium_start_driver_firefox():  # start selenium for Firefox | Tested: Works!
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    print('Starting driver "GeckoDriver" from Firefox/Mozilla')
    return driver


def selenium_start_driver_chrome():  # start selenium for Chrome | not tested yet!
    driver = webdriver.Chrome()
    print('Starting driver "WebDriver" from Chrome/Google')
    return driver


def open_gts_site(driver, player_id, url_tag):  # opens the gts livery search-engine our simplified data interface
    #Old Variant https://gts.gt-beginners.net/livery/?searchword=UweWald&lang=us
    #link = "https://gts.gt-beginners.net/livery/?cartag=&searchword=" + player_id + "&type=0&lang=us&d="
    link = "https://gts.gt-beginners.net/"+url_tag+"/?searchword=" + player_id + "&lang=us&"
    driver.get(link)
    print("Loading the website with the userprofile")
    pass


def print_element(elements):  # Turns HTMl Code to array
    element_list = []
    for src in elements:
        element_list.append(src.get_attribute('src'))
    return element_list


def searching_element(driver, searched_class):  # Searching element and return an Array with all the Links
    car_element = driver.find_elements(By.CLASS_NAME, searched_class)
    print(type(car_element))
    printArrayList = print_element(car_element)
    #print(printArrayList)
    return printArrayList


def liveryToURL(variable):  # switches the string for the livery to the searching Html-Tag
    returnValue = "None"
    if "CarLivery" == variable:
        returnValue = "livery"
    if "HelmetLivery" == variable:
        returnValue = "helmet"
    if "Decal" == variable:
        returnValue = "decal"
    if "SuitLivery" == variable:
        returnValue = "wear"
    if "Replay" == variable:
        returnValue = "replay"

    return returnValue


if __name__ == '__main__':
    print_hi('Selenium-Connection')
    drv = selenium_start_driver_firefox()
    player_id = "UweWald"
    open_gts_site(drv, player_id, "livery")
    searched_class = "sumb"
    elementArray = searching_element(drv, searched_class)
    print(elementArray)
