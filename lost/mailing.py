from django.core.mail import send_mail
import getpass, imaplib
import email
import datetime
from models import Data
import re

def form_entry(mail):
    print  "Script ------"
    send_mail(
        '[Notification] Lost and Found entry submitted',
        'Your account just submitted a Lost/Found Entry',
        'dosa@iitk.ac.in',
        [mail],
        fail_silently=False,
    )
    print "----------------"

def process_mail():
    server = imaplib.IMAP4("newmailhost.cc.iitk.ac.in", 143)
    server.login("ppriyank", "password")
    server.select("INBOX")
    server.select()
    result, data = server.search(None, '(SUBJECT "LOST")')
    # typ, data = server.search(None, 'ALL')
    # date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
    # result, data = server.uid('search', None,
    #                           '(SENTSINCE {date} HEADER Subject "LOST")'.format(date=date))
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    id_list= id_list[::-1]
    for num in id_list:
            count = 0
            typ, data = server.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            # message = email.parser.Parser().parse(file)
            # date_of_mail = message['Date']
            email_message = email.message_from_string(raw_email)
            email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
            email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
            subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
            date = str(email.header.make_header(email.header.decode_header(email_message['Date'])))
            print email_message['Date']
            # print datetime.datetime.strptime(email_message['Date'], '%a, %d %b %Y %H:%M:%S %z').strftime('%m-%d-%y')
            # print datetime.date.strftime( email_message['Date'], "%m/%d/%y")
            # strftime("%Y-%m-%d", strtotime(email_message['Date'])
            # print strftime("%Y-%m-%d", strtotime(email_message['Date']))
            date.replace('-', '+')
            temp = date.split('+')
            t = datetime.datetime.strptime(temp[0], '%a, %d %b %Y %H:%M:%S ')
            my_date_obj = t.date()
            # print t
            t = str(t)
            print "-----------" , t.split(" ")
            temp = t.split(" ")
            date = temp[0]

            if subject == 'LOST':
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        line = body.decode('utf-8')
                        for string in line.splitlines():
                            # print string
                            # temp = re.split( ";", string  )
                            temp = string.split(":")
                            # print temp
                            if temp[0] =='NAME':
                                # print "first"
                                count = count +1
                                name= temp[1]
                            elif temp[0]=='rollno':
                                roll = temp[1]
                                count = count + 1
                                # print "second"
                            elif temp[0] == 'desc':
                                desc = temp[1]
                                count = count + 1
                                # print "third"
                            elif temp[0] == 'status':
                                count = count + 1
                                # print "fourth"
                                if temp[1] == 'FOUND':
                                    sta= 1
                                else :
                                    sta = 0
                        else:
                            continue
                if count == 4 :
                    print date
                    p = Data(name=str(name), email = email_from ,rollno= roll ,  description= desc, date = date , status = sta  )
                    p.save()
                    server.store(num, '+FLAGS', '\\Deleted')
            else:
                continue
    server.expunge()
    server.close()
    server.logout()
