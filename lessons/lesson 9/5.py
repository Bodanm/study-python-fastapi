from abc import ABC, abstractclassmethod


class MakeCall(ABC):
    @abstractclassmethod
    def make_call(self):
        pass


class SendSms(ABC):
    @abstractclassmethod
    def send_sms(self):
        pass


class GetInternet(ABC):
    @abstractclassmethod
    def get_internet(self):
        pass


class MobilePhone(MakeCall, SendSms, GetInternet):
    def make_call(self):
        print("calling to abonement...")

    def send_sms(self):
        print("sending sms to abonement...")

    def get_internet(self):
        print("get connect to abonement...")

class StacionarPhone(MakeCall):
    def make_call(self):
        print("calling to abonement...")


mobile_phone = MobilePhone()
mobile_phone.make_call()
mobile_phone.send_sms()
mobile_phone.get_internet()
print("----------")
stacionar_phone = StacionarPhone()
stacionar_phone.make_call()
