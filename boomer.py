import imaplib as dmail
import email as mlz
from bs4 import BeautifulSoup as bsoup


class Snail:
    #usname = input('enter email name:')
    usname = 'voomerzboomerzboom@gmail.com'
    sesame = input('enter pass:')
    #sesame = ''
    im_url = "imap.gmail.com"
    prvdr = dmail.IMAP4_SSL(im_url)

    def conx(self):
        try:
            Snail.prvdr.login(Snail.usname, Snail.sesame)

            print("successfully connected to: {}".format(Snail.usname))

        except:
            print("was unable to connect check settings/password")

    def read_em(self):
        readerz = Snail.prvdr
        #print('{}'.format(readerz.list()))
        readerz.select('INBOX')
        result, data = readerz.uid('search', None, "ALL")
        box_itemlist = data[0].split()

        for index, itemz in enumerate(box_itemlist):
            result2, email_data= readerz.uid('fetch', itemz, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_messsage = mlz.message_from_string(raw_email)
            to_ = email_messsage['To']
            from_ = email_messsage['From']
            subz_ = email_messsage['Subject']
            bods_ = email_messsage['Body']
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