import ZaraAPIClient
import DatabaseManeger
import Product



class StockTrackerApp:
    def __init__(self):
        self.api = ZaraAPIClient()
        self.db = DatabaseManeger.DatabaseManager()

    def run(self):
        raw_products = self.api.fetch_products()
        for json_obj in raw_products:
            product = Product.from_json(json_obj)
            self.db.insert_or_update(product)
