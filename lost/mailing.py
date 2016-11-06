from django.core.mail import send_mail

def form_entry(mail):
    print  "--------------------"
    send_mail(
        '[Notification] Lost and Found entry submitted',
        'Your account just submitted a Lost/Found Entry',
        'dosa@iitk.ac.in',
        [mail],
        fail_silently=False,
    )

def process_mail(mb):
        print "Processing: mail box"
        if mb.email_box_type == 'pop3':
            if mb.email_box_ssl:
                if not mb.email_box_port: mb.email_box_port = 995
                server = poplib.POP3_SSL(mb.email_box_host, int(mb.email_box_port))
            else:
                if not mb.email_box_port: mb.email_box_port = 110
                server = poplib.POP3(mb.email_box_host, int(mb.email_box_port))
            server.getwelcome()
            server.user(mb.email_box_user)
            server.pass_(mb.email_box_pass)

            messagesInfo = server.list()[1]

            for msg in messagesInfo:
                msgNum = msg.split(" ")[0]
                msgSize = msg.split(" ")[1]
                full_message = "\n".join(server.retr(msgNum)[1])

                # Do something with the message

                server.dele(msgNum)
            server.quit()

        elif mb.email_box_type == 'imap':
            if mb.email_box_ssl:
                if not mb.email_box_port: mb.email_box_port = 993
                server = imaplib.IMAP4_SSL(mb.email_box_host, int(mb.email_box_port))
            else:
                if not mb.email_box_port: mb.email_box_port = 143
                server = imaplib.IMAP4(mb.email_box_host, int(mb.email_box_port))
            server.login(mb.email_box_user, mb.email_box_pass)
            server.select(mb.email_box_imap_folder)
            status, data = server.search(None, 'ALL')
            for num in data[0].split():
                status, data = server.fetch(num, '(RFC822)')
                full_message = data[0][1]

                # Do something with the message

                server.store(num, '+FLAGS', '\\Deleted')
            server.expunge()
            server.close()
            server.logout()
