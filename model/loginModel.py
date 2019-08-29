# -*- coding: utf-8 -*-


class loginModel(object):

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self,userName):
        self._userName=userName

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password=password

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self,message):
        self._message=message

    @property
    def vecode(self):
        return self._vecode

    @vecode.setter
    def vecode(self,vecode):
        self._vecode=vecode



