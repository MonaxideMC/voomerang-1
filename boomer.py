import imaplib
import email as mlz
import os
import mailbox
from bs4 import BeautifulSoup as bsoup
#Getpass for hiding the password prompt in the commandline
from getpass import getpass


class Snail:
    #usname = input('enter email name:')
    usname = input('Please enter your full email address: ')
    sesame = getpass()
    #sesame = ''
    im_url = "imap.gmail.com"
    prvdr = imaplib.IMAP4_SSL(im_url)

    def conx(self):
        try:
            Snail.prvdr.login(Snail.usname, Snail.sesame)

            print("successfully connected to: {}".format(Snail.usname))

        except:
            print("Login Failed, Please check your credentials.")

    def read_em(self):
        readerz = Snail.prvdr
        #print('{}'.format(readerz.list()))
        readerz.select('INBOX')
        result, data = readerz.uid('search', None, "ALL")
        box_itemlist = data[0].split()

        for index, itemz in enumerate(box_itemlist):
            result2, email_data= readerz.uid('fetch', itemz, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = mlz.message_from_string(raw_email)
            to_ = email_message['To']
            from_ = email_message['From']
            subz_ = email_message['Subject']
            bods_ = email_message['Body']
            print(index+1)
            print("email was sent from... {}".format(from_))
            #print('{}\n {}\n {}\n {}'.format(to_, from_, subz_, bods_))

            for part in email_messsage.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    sps= bsoup(body, "html.parser")
                    soups = sps.get_text()
                    #print(body)
                    print(soups)

# clientz=Snail()
# clientz.conx()
# clientz.read_em()
