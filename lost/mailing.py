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


def read_mail():
    return 0
