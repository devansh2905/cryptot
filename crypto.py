import requests
import time
import smtplib
from plyer import notification

#----------------delivering  mail works only for gmail users-------------

myadd = 'enter your email address'
password = 'enter email password'
toadd = 'enter target email address'

def cryp(coin, HL, target, ticker):
    count = 1

    while True:
        if HL == (1 or 2):
            responce = requests.get("https://api.wazirx.com/api/v2/tickers")
            full = responce.json()
            buy = (full[coin]['buy'])
            sell = (full[coin]['sell'])
            lp = (full[coin]['last'])
            name = (full[coin]['name'])
            print("|", count, "|", {name}, " ", "|buy:- ", buy, "|", "  |sell:- ", sell, "|", "  |Last Price:- ", lp,
                  "|".format(name))
            count += 1
            if HL == 1 and target < float(lp):
                print("alert!! prize went high at " + lp)
                alert("HIGHER", target)
                mail("HIGHER", target)
                break
            if HL == 2 and target > float(lp):
                print("alert!! prize went low")
                alert("LOWER", target)
                mail("LOWER", target)
                break
            time.sleep(ticker)
        else:
            print("invalid input for High Low")
            break

def alert(A, B):
    notification.notify(
        title = "PRICE ALERT!!!!",
        message = f"The price went {A} than your taret amount {B} ",
        app_icon = r"a.ico",
        timeout = 60
    )

def mail(A,B):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(myadd, password)
        subject = "PRICE ALERT"
        body = f"The price went {A} than your taret amount {B}",
        msg = f'subject: {subject}\n\n{body}'
        smtp.sendmail(myadd, toadd , msg)


if __name__ == "__main__":
    coin = input("Enter the coin name ex:dogeusdt ")
    target = float(input("enter a target: "))
    HL = int(input("press 1 to alert if goes high: \npress 2 to alert if goes low: "))
    ticker = int(input("Enter the ticker time(in seconds...3<): "))
    try:
        cryp(coin ,HL , target, ticker)
    except KeyError:
        print(f"{coin} coin is unavailable..restart the program ")
    except smtplib.SMTPAuthenticationError:
        print("MAIL NOT DELIVERED!!!\nCheck your Login Credentials Properly.\n"
              "If still the error persists follow the following steps given below:\n"
              "login to gmail acc<<manage account<< security<< Less secure app access<< turn it on.")
    except Exception:
        print('An unnatural exception occurred try checking your internet connection..restart the program')







