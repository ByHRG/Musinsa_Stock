import requests
from bs4 import BeautifulSoup


class MUSINSA:
    def __init__(self):
        self.headers = {
            "Cookie": "_gf=A",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
        }
        self.payload = {}

    def url_setting(self, url):
        return url.split("products/")[-1].split("?")[0].split("/")[0]

    def run(self, product_code):
        if "musinsa" in product_code:
            product_code = self.url_setting(product_code)
        req = requests.get(
            "https://goods-detail.musinsa.com/api2/goods/" + product_code +"/curation", headers=self.headers
        )
        print(req.text)
        name = req.json()["data"]["curationTabs"][0]["curationGoodsList"][0]["goodsName"]
        price = req.json()["data"]["curationTabs"][0]["curationGoodsList"][0]["price"]
        img = req.json()["data"]["curationTabs"][0]["curationGoodsList"][0]["imageUrl"]
        output = {
            "Name": name,
            "Price": price,
            "Image": img,
            "Url": "https://www.musinsa.com/products/" + str(product_code),
            "Stock": {},
        }
        data_list = requests.get("https://goods.musinsa.com/api2/review/v1/view/filter?goodsNo="+product_code, headers=self.headers).json()["data"]["filterOption"]["firstOptions"]
        for i in data_list:
            output["Stock"].update({i["txt"]: i["qty"]})
        return output


url = 'https://www.musinsa.com/products/4289228'
print(MUSINSA().run(url))
