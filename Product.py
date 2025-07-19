

class Product:
    def __init__(self, name, price, old_price, stock, reference, image_url):
     self.name = name 
     self.price = price 
     self.old_price = old_price
     self.stock = stock
     self.reference = reference
     self.image_url = image_url


    
def from_json(json_obj):
    name = json_obj.get("seo", {}).get("keyword", "Bilinmiyor")
    price = json_obj.get("price", 0) / 100
    old_price = json_obj.get("oldPrice", 0) / 100
    stock = json_obj.get("availability", "bilinmiyor")
    reference = json_obj.get("reference", "yok")
    image_url = json_obj.get("url", "")
    return Product(name, price, old_price, stock, reference, image_url)