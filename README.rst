==============
django-sendsms
==============


A simple api to send SMS messages with django. The api is structured the same way as djangos own email api.

快速安装
============

::

    pip install django-sendsms

配置参数 ``SENDSMS_BACKEND`` (默认为 ``'sendsms.backends.console.SmsBackend'``)::

    SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend'


基本用法
===========

Sending SMSs is like sending emails::

    from sendsms import api
    api.send_sms(body='I can haz txt', from_phone='+41791111111', to=['+41791234567'])

you can also make instances of ``SmsMessage``::

    from sendsms.message import SmsMessage
    message = SmsMessage(body='lolcats make me hungry', from_phone='+41791111111', to=['+41791234567'])
    message.send()


定义后端
===============

Creating custom ``SmsBackend`` s::

    from sendsms.backends.base import BaseSmsBackend
    from some.sms.delivery.api

    class AwesomeSmsBackend(BaseSmsBackend):
        def send_messages(self, messages):
            for message in messages:
                for to in message.to:
                    try:
                        some.sms.delivery.api.send(
                            message=message.body,
                            from_phone=message.from_phone,
                            to_phone=to,
                            flashing=message.flash
                        )
                    except:
                        if not self.fail_silently:
                            raise

Then all you need to do is reference your backend in the ``SENDSMS_BACKEND`` setting.

