class Email:
    def __init__(self):
        pass
    def enviar (self):
        print('Sen envia un e-mail')
class Sms:
    def __init__(self):
        pass
    def enviar (self):
        print('Se envia un SMS')

class NotificaciónMixta(Email, Sms):
    def __init__(self):
        pass
    
    @classmethod
    def cambio_comportamiento (cls):
        if cls.__bases__ == (Email, Sms):
            cls.__bases__ = (Sms, Email)
        else:
            cls.__bases__ = (Email,Sms)

notificacion1 = NotificaciónMixta()

notificacion1.enviar()
print(NotificaciónMixta.__mro__)

NotificaciónMixta.cambio_comportamiento()

notificacion1.enviar()
print(NotificaciónMixta.__mro__)

NotificaciónMixta.cambio_comportamiento()

notificacion1.enviar()
print(NotificaciónMixta.__mro__)