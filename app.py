import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook

WEBHOOK_URL = ''

STRONA_URL = "https://basketzone.pl/index.php?action=szukaj&szukaj=NIKE+AIR+JORDAN+4&sort=id"

ILE_CZEKAC = 30

def wyslij_webhooka(nazwa_buta):
    webhook = DiscordWebhook(
        url=WEBHOOK_URL, rate_limit_retry=True,
        content=nazwa_buta)
    response = webhook.execute()

def daj_nazwe_buta(STRONA_URL):
    strona = requests.get(url=STRONA_URL)
    zupa = BeautifulSoup(strona.content, 'html.parser')
    buty = zupa.find("div", class_="product")
    nazwa_buta = buty.find("div", class_="name").text
    return nazwa_buta

def main():
    poczatkowy_but = daj_nazwe_buta(STRONA_URL)
    time.sleep(ILE_CZEKAC)
    while True:
        nowy_but = daj_nazwe_buta(STRONA_URL)

        if poczatkowy_but != nowy_but:
            wyslij_webhooka(nowy_but)
            poczatkowy_but = nowy_but
            
        time.sleep(ILE_CZEKAC)

if __name__ == "__main__":
    main()
