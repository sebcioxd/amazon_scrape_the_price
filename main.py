import requests
from bs4 import BeautifulSoup as bs
import re
import smtplib
import time

login_email = "" #Here type your email
login_password = "" #Here type your google password for app / learn more just by typing app paswords google
to_mail = "" #Type the mail you want to sent the information to:

def get_price():
    url = 'https://www.amazon.pl/Acer-Nitro-Komputer-stacjonarny-i5-12400/dp/B09VLL1NW3/ref=sr_1_5?dib=eyJ2IjoiMSJ9.wCjUbBpqDyN09SqmNmTr0y5ZVPDuwLR3JnZYeMJ--wdR0cojVGuQcRsDRp3KqlG4g35w4PzbdJQwUQc3-V63NyT6QBdpwyh0mNwFpEyDaHZMS7UUr-_-pWhvB9VroNHribDFgU2ImBBOEDpVDInq_iG2QuUbM9TZjsYPTqXKYVqhcDsaa1EdT7Gqaz7qCrWqR_Tuc0K_muzmOLVd9mipfsbQbqi5rZCBMtq2-l3mcEDnKjWPNj7kUvJypYN5WzpYRgyykrWGluyzpKx1lyTy2-fFibbm7pC0LHsLKxqoSeM.__cpPIpr6TMc0Ms2Agy9xAPH2cQ0t0Ckjyg9K1z0aLs&dib_tag=se&keywords=pc&qid=1710077100&sr=8-5&th=1'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}

    page = requests.get(url, headers=headers)
    soup = bs(page.text, "html.parser")
    price = soup.find('span', attrs={'class':'a-price-whole'})
    price_text = price.text
    converted_price = int(re.sub(r'\D', '', price_text)) #Get rid of any whitespaces and symbols
    print(converted_price)

    if converted_price < 3900:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #estabilish connection with gmail server
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(f'{login_email}', f'{login_password}')

    subject = "The price fell down wow!"
    body = f"Check the amazon link: https://www.amazon.pl/Acer-Nitro-Komputer-stacjonarny-i5-12400/dp/B09VLL1NW3/ref=sr_1_5?dib=eyJ2IjoiMSJ9.wCjUbBpqDyN09SqmNmTr0y5ZVPDuwLR3JnZYeMJ--wdR0cojVGuQcRsDRp3KqlG4g35w4PzbdJQwUQc3-V63NyT6QBdpwyh0mNwFpEyDaHZMS7UUr-_-pWhvB9VroNHribDFgU2ImBBOEDpVDInq_iG2QuUbM9TZjsYPTqXKYVqhcDsaa1EdT7Gqaz7qCrWqR_Tuc0K_muzmOLVd9mipfsbQbqi5rZCBMtq2-l3mcEDnKjWPNj7kUvJypYN5WzpYRgyykrWGluyzpKx1lyTy2-fFibbm7pC0LHsLKxqoSeM.__cpPIpr6TMc0Ms2Agy9xAPH2cQ0t0Ckjyg9K1z0aLs&dib_tag=se&keywords=pc&qid=1710077100&sr=8-5&th=1"

    msg = f"Subject: {subject}\n\n {body}"
    server.sendmail(
        f"{login_email}",
        f"{to_mail}",
        msg
    )
    print("Email has been sent!")
    server.quit()


def main():
    get_price()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(86400)



