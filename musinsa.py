import httpx


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
        req = httpx.get(
            f"https://order.musinsa.com/api2/order/v1/inventories?goodsNo={product_code}", headers=self.headers
        )

        output = {
            "Url": "https://www.musinsa.com/products/" + str(product_code),
            "Stock": {},
        }

        for i in req.json()["data"]["inventories"][0]["goodsOptions"]:
            output["Stock"].update({i["goodsOption"]: i["quantity"]})
        return output
