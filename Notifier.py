from plyer import notification

class Notifier:
    @staticmethod
    def notify_terminal(name, old_stock, new_stock):
        print(f"🔔 {name} - STOK DEĞİŞİMİ: {old_stock} → {new_stock}")

    @staticmethod
    def notify_desktop(message):
        from plyer import notification
        notification.notify(title="Zara Stok Değişimi", message=message, timeout=5)

    @staticmethod
    def notify_email(message):
        # SMTP gönderimi yapılabilir
        pass
