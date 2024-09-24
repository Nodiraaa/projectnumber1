import requests
from bs4 import BeautifulSoup

for i in range(1, 1000):
    url = "https://avtoelon.uz/avto/gorod-tashkent/?price-currency=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    containers = soup.find_all("div", {"class": "list-item"})

    for car_info in containers:
        try:
            title = car_info.find("span", {"class": "a-el-info-title"}).text
            price = car_info.find("span", {"class": "price"}).text
            price = price.replace("Цена:", "").replace("y.e.", "")
            title_splitted = title.split(",")
            postion = None
            try:
                postion = title_splitted[1].replace("позиция", "")
            except:
                pass
            print(f"Name: {title_splitted[0]}")
            print(f"Postion: {postion}")
            print(f"Price: {price}")
        except:
            pass


