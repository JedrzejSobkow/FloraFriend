import datetime
import json
import threading
import time
import wx
from plyer import notification

from src.root.models.flower_model import FlowerModel

class Notifier:
    def __init__(self, flower):
        self.flower = flower
        self.running = True

    def check_notification(self):
        next_watering_datetime = datetime.datetime.strptime(self.flower.nextWatering, '%Y-%m-%d %H:%M:%S')
        current_datetime = datetime.datetime.now()
        if current_datetime >= next_watering_datetime:
            title = f"Czas na podlewanie kwiatka: {self.flower.name}"
            message = f"Nadszedł czas na podlewanie kwiatka: {self.flower.name}"
            notification.notify(title=title, message=message, timeout=10)
            threading.Timer(86400, self.check_notification).start()  # Sprawdź ponownie za 24 godziny

# Utwórz obiekt klasy FlowerModel
flower = FlowerModel("Sunflower", wx.Colour(255, 56, 16), 3, nextWatering="2024-06-06 10:47:50")

# Utwórz obiekt klasy Notifier i przekaż do niego obiekt klasy FlowerModel
notifier = Notifier(flower)

# Uruchom sprawdzanie powiadomień w osobnym wątku
threading.Thread(target=notifier.check_notification).start()

# Tutaj można dodać kod interfejsu użytkownika lub inny kod

# Przykład zamknięcia aplikacji po naciśnięciu przycisku
running = True

def on_exit(event):
    notifier.running = False  # Zatrzymaj sprawdzanie powiadomień
    app.ExitMainLoop()  # Zamknij pętlę główną aplikacji

app = wx.App()
frame = wx.Frame(None, title="Flower Notification App", size=(400, 300))
exit_button = wx.Button(frame, label="Exit")
exit_button.Bind(wx.EVT_BUTTON, on_exit)
frame.Show()
app.MainLoop()
