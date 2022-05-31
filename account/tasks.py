from django.core.mail import send_mail

from spotify.celery import app
from .send_email import send_confirmation_email
from django.core.mail import send_mail

@app.task
def send_activation_code(to_email, code):
    # send_confirmation_email(email)  # 1-способ
    # code = user.activation_code  # 2-способ
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    # to_email = user.email
    send_mail(
        'ЗдравствуйтеЮ активируйте ваш аккаунт ',
        f'Для того чтобы активироват ваш аккаунт нужно перейти по ссылке: {full_link}',
        'from@example.com',
        [to_email, ],
        fail_silently=False, )

