import requests
import time
import smtplib
from plyer import notification

#----------------delivering  mail works only for gmail users-------------

myadd = 'enter your email address'
password = 'enter email password'
toadd = 'enter target email address'

def cryp(coin, H, L, ticker):
    count = 1

    while True:
        responce = requests.get("https://api.wazirx.com/api/v2/tickers")
        full = responce.json()
        buy = (full[coin]['buy'])
        sell = (full[coin]['sell'])
        lp = (full[coin]['last'])
        name = (full[coin]['name'])
        print("|", count, "|", {name}, " ", "|buy:- ", buy, "|", "  |sell:- ", sell, "|", "  |Last Price:- ", lp,
              "|".format(name))
        count += 1
        if H is not None and H < float(lp):
            print("alert!! prize went high at " + lp)
            alert("HIGHER", H)
            mail("HIGHER", H)
            break
        if L is not None and L > float(lp):
            print("alert!! prize went low")
            alert("LOWER", L)
            mail("LOWER", L)
            break
        time.sleep(ticker)





def alert(A, B):
    notification.notify(
        title = "PRICE ALERT!!!!",
        message = f"The price went {A} than your taret amount {B} ",
        app_icon = r"a.ico",
        timeout = 60
    )

def mail(A,B):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(myadd, password)
            subject = "PRICE ALERT"
            body = f"The price went {A} than your taret amount {B}",
            msg = f'subject: {subject}\n\n{body}'
            smtp.sendmail(myadd, toadd , msg)
    except smtplib.SMTPAuthenticationError:
        print("MAIL NOT DELIVERED!!!\nCheck your Login Credentials Properly.\n"
              "If still the error persists follow the following steps given below:\n"
              "login to gmail acc<<manage account<< security<< Less secure app access<< turn it on.")

if __name__ == "__main__":
    coin = input("Enter the coin name ex:dogeusdt ")
    H = input("Mark HIGH target : ")
    if H == '':
        H = None
    else:
        H = float(H)
    L = input("Mark the LOW target : ")
    if L == '':
        L = None
    else:
        L = float(L)
    ticker = int(input("Enter the ticker time(in seconds...3<): "))
    try:
        cryp(coin ,H , L, ticker)
    except KeyError:
        print(f"{coin} coin is unavailable..restart the program ")
    except Exception:
        print('An unnatural exception occurred try checking your internet connection..restart the program')







