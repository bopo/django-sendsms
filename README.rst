==============
django-sendsms
==============


一个简单的API发送短信 Django API 结构相同使用自己的电子邮件的API。


快速安装
============

::

    pip install django-sendsms

配置参数 ``SENDSMS_BACKEND`` (默认为 ``'sendsms.backends.console.SmsBackend'``)::

    SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend'


基本用法
===========

发送短信是发送电子邮件::

    from sendsms import api
    api.send_sms(body='I can haz txt', from_phone='+41791111111', to=['+41791234567'])

还可以制作实例 ``SmsMessage``::

    from sendsms.message import SmsMessage
    message = SmsMessage(body='lolcats make me hungry', from_phone='+41791111111', to=['+41791234567'])
    message.send()


定义后端
===============

创建自定义 ``SmsBackend`` ::

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


然后，所有你需要做的是参考你的后台在 ``SENDSMS_BACKEND`` 设置。
