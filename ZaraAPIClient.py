import requests

class ZaraAPIClient:
    API_URL = "https://www.zara.com/tr/tr/products?ajax=true"

    def fetch_products(self):
        response = requests.get(self.API_URL, headers={"User-Agent": "Mozilla/5.0"})
        return response.json().get("productSummaries", [])
