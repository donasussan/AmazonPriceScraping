from bs4 import BeautifulSoup

import requests
import smtplib
import lxml

link = input("Paste the link of you favourite amazon item: ")
password_ = "bnsiayfabqvshjwk"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
# link = input("Paste the link of the item you want to track the price of: ")
response = requests.get(url=f'{link}', headers=headers)
amazon_webpage = response.text


soup = BeautifulSoup(amazon_webpage, "lxml")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

my_target_price =float(input("Enter your target price :"))


if price_as_float <= my_target_price:

        connection = smtplib.SMTP("smtp.gmail.com")
        my_email = "donasussanchacko@gmail.com"
        password = password_
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="donasussan2000@gmail.com",
        msg="Subject: YAYY! Amazon Price Dropped! \n\n Hello! This message is to inform you that the price of the item you wanted from amazon has dropped. Grab your deal!")
        print("Amazon Price Dropped :)")
        connection.close

else:
        print("Price not dropped :(")