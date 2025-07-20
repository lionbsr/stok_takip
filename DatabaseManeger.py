import sqlite3
import Product
import Notifier

class DatabaseManager:
    def __init__(self, db_path="stok_takip.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS urunler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT,
            fiyat REAL,
            eski_fiyat REAL,
            stok TEXT,
            onceki_stok TEXT,
            urun_kodu TEXT UNIQUE,
            gorsel_linki TEXT
        )""")
        self.conn.commit()

    def get_stok(self, urun_kodu):
        self.cursor.execute("SELECT stok FROM urunler WHERE urun_kodu = ?", (urun_kodu,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def insert_or_update(self, product: Product):
        eski_stok = self.get_stok(product.reference)
        if eski_stok != product.stock:
            Notifier.notify_terminal(product.name, eski_stok, product.stock)

        self.cursor.execute("""
        INSERT INTO urunler (isim, fiyat, eski_fiyat, stok, onceki_stok, urun_kodu, gorsel_linki)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(urun_kodu) DO UPDATE SET
            fiyat = excluded.fiyat,
            eski_fiyat = excluded.eski_fiyat,
            onceki_stok = urunler.stok,
            stok = excluded.stok,
            gorsel_linki = excluded.gorsel_linki
        """, (product.name, product.price, product.old_price,
              product.stock, product.stock, product.reference, product.image_url))
        self.conn.commit()
