
# HERITAGE CLASSE (GENERALISATION)
class Animal: pass

class Dog( Animal ): pass

class Cat( Animal ): pass

class BengalCat( Cat ): pass

# CLASSES ABSTRAITS / INTERFACES
import abc

class Communicates( abc.ABC ):
    @abc.abstractmethod
    def make_signal(self):
        """a CONTRACT to be overwritten by the user"""
        pass

    @abc.abstractmethod
    def receive_signal(self):
        """a CONTRACT to be overwritten by the user"""
        pass

class MyBluetoothController( Communicates ):
    def make_signal(self):  
        ... # si on les overwrite pas, ca va pas compiler
    
    def receive_signal(self):
        ...

