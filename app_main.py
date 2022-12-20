from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import json


def get_info_from_praktika(
        driver: webdriver.Firefox,
        url: str,
        sleep_time: int = 5
) -> dict:

    data: dict = {}

    driver.get(url=url)
    time.sleep(sleep_time)

    titles = driver.find_elements(By.CLASS_NAME, "event_title")
    descriptions = driver.find_elements(By.CLASS_NAME, "event_description")
    dates = driver.find_elements(By.CLASS_NAME, "date")
    times = driver.find_elements(By.CLASS_NAME, "time")

    length = len(titles)
    for i in range(0, length):
        event = {
            'event_description': descriptions[i].text,
            'date': dates[i].text,
            'time': times[i].text
        }
        data[titles[i].text.capitalize()] = event
    return data


def main():

    driver = webdriver.Firefox()
    praktika_data: dict = get_info_from_praktika(driver=driver, url="https://praktikatheatre.ru/schedule")
    driver.close()

    with open("data/praktika_data.json", 'w', encoding="UTF-8") as file:
        json.dump(praktika_data, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
