from celery import shared_task
from .models import Post, Response
from django.core.mail import send_mail


@shared_task
def respond_send_email(respond_id):
    respond = Response.objects.get(id=respond_id)
    send_mail(
        subject=f'MMORPG Billboard: новый отклик на объявление!',
        message=f'Доброго дня, {respond.post.author}, ! На ваше объявление есть новый отклик!\n'
                f'Прочитать отклик:\nhttp://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='testSK1337@yandex.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def respond_accept_send_email(response_id):
    respond = Response.objects.get(id=response_id)
    print(respond.post.author.email)
    send_mail(
        subject=f'MMORPG Billboard: Ваш отклик принят!',
        message=f'Доброго дня, {respond.author}, Автор объявления {respond.post.title} принял Ваш отклик!\n'
                f'Посмотреть принятые отклики:\nhttp://127.0.0.1:8000/responses',
        from_email='testSK1337@yandex.ru',
        recipient_list=[respond.post.author.email, ],
    )


