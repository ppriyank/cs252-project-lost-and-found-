from django.core.mail import send_mail
import getpass, imaplib
import email
import datetime

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

def process_mail(mb):
    server = imaplib.IMAP4("newmailhost.cc.iitk.ac.in", 143)
    server.login("abhijain", "password")
    server.select("INBOX")
    server.select()
    # result, data = server.search(None, '(SUBJECT "LOST")')
    # typ, data = server.search(None, 'ALL')
    date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
    result, data = server.uid('search', None,
                              '(SENTSINCE {date} HEADER Subject "LOST")'.format(date=date))

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    id_list= id_list[::-1]

    for num in id_list:

        typ, data = server.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        print email_message['To']
        print email.utils.parseaddr(email_message['From'])

        print 'Message %s\n%s\n' % (num, data[0][1])
        break

    server.expunge()
    server.close()
    server.logout()
