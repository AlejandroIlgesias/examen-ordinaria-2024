from datetime import date

class Tweet():
    def __init__(self,time=date(0,0,0),message="",sender=None):
        
        self.time=time #Objeto de la clase Date de python
        if len(message)>140:
            raise ValueError("Superado el límite de caracteres")
        self.message=message #Cadena de caracteres
        self.sender=sender #Objeto de la calse UserAccount

    def __str__(self):
        return self.time+" : "+self.message
    

class DirectMessage(Tweet):
    
    def __init__(self, time, message, sender,receiver):
        super().__init__(time, message, sender)
        self.receiver=receiver #Objeto de la clase UserAcount

class Retweet(Tweet):

    def __init__(self, time, message, sender,reference):
        super().__init__(time, message, sender)
        self.reference=reference #Objeto de la clase UserAccount

'''La fecha dependerá del momento en el que se cree el tweet.Por defecto tiene 0/0/0.'''