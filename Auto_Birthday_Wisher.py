import pandas as pd
import datetime
import smtplib
import os
# Enter your authentication details
GMAIL_ID = 'samkrv7@gmail.com'
GMAIL_PSWD = 'aayushlove'


def sendEmail(to, sub, msg):
    print(f"To: {to}")
    print(f"Subject: {sub}")
    print(f"Message: {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday) 
        if(today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Message']) 
            writeInd.append(index)
    print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        print(df.loc[i, 'Year'])
    print(df) 
    df.to_excel('data.xlsx', index=False)