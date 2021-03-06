from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.conf import settings
from django.core.mail import send_mail
from smtplib import SMTPException
import logging

logger = logging.getLogger(__name__)
# Create your models here.


class ContactPageMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class ContactPage(Page):
    intro = models.CharField(max_length=255, default='Leave us a Message')
    thankyou_page_title = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):
        from contact.forms import ContactMessageForm
        if request.method == 'POST':
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                message = form.save()
                # sending the email
                try:
                    sent_from = 'steppingstoneswebpage@gmail.com'
                    sent_from_password = 'E8TcPC2z7C8v'
                    to = ["mfalmegriffin@gmail.com", "griffinmfalme@gmail.com"]
                    subject = "Icanary Website Contact Message"
                    body = message.message

                    email_body = """
                            New Message from The KID Website
                            From: %s
                            E-mail: %s
                            Phone Number: %s
                            Message: %s
                            """ % (message.name,
                                   message.email,
                                   message.phone,
                                   body,
                                   )
                    send_mail(
                        "KID Website Inquiry Contact Us Page",
                        email_body,
                        settings.EMAIL_HOST_USER,
                        ["mfalmegriffin@gmail.com"],
                        fail_silently=False,
                    )
                except SMTPException as e:

                    logger.error(e)

                return render(request, 'thankyou.html', {
                    'page': self,
                    'contact': message
                }
                )
        else:
            form = ContactMessageForm()
        return render(request, 'contact_page.html', {
            'page': self,
            'form': form,
        })
