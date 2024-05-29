from Tweet import Tweet,DirectMessage,Retweet


class UserAccount():
    def __init__(self,alias, email, tweets, followers, timeline) :
        self.alias=alias #Cadena de caracteres
        self.email=email #Objeto de la clase email
        self._tweets=tweets #Lista de objetos de la clase Tweet
        self._followers=followers #Lista de objetos de la clase UserAccount
        self._timeline=timeline # Cola de objetos de la clase tweet

    def follow(self,user2): #user2 es un objeto de la clase UserAccount
        
        user2._followers.apend(self)
    
    
    def tweet(self,tweet1): #tweet1 es una cadena de caracteres
        
        send=Tweet(message=tweet1,sender=self)
        self._tweets.añadir_elemento(send)
        
        for follower in self._followers:
            follower._timeline.añadir_elemento(send)

    
    
    def write_direct_message(self,message,user2):#user2 es un ojeto de la clase UserAccount ; message es una cadena de caracteres.
        
        send=DirectMessage(message=message,sender=self,receiver=user2)
        user2._timeline.añadir_elemento(send)
    
    def retweet(self,message,tweet2): #message es una cadena de caracteres ; tweet2 es un objeto de la clase Tweet.
        
        send=Retweet(message=message,sender=self,reference=tweet2.sender)
        self._tweets.añadir_elemento(send)
        
        for follower in self._followers:
            follower._timeline.añadir_elemento(send)


    '''
    follow()
    -->Simplemente añade el objeto desde el que se llama al método a la cola almacenada en el atributo self._followers del objeto
    user2.

    tweet()
    -->primero crea un objeto de la clase Tweet almacenado en la variable send.Después lo guarda en la cola self._tweets del
    objeto desde el que se llama el método.Por último almacena el objeto de send en cada una de las colas del atributo _timeline
    de cada uno de los objetos de la cola en self._followers.


    write_direct_message()
    -->Dentro de la variable send almacena un objeto de la clase DirectMessage donde el mensaje privado es pasado a través
    del parámetro message del método y el usuario al que se quiere escribir es pasado por user2.
    La segunda línea se encarga de añadir en el timeline de user2 el tweet (y solo en el de user2).
    
    retweet()
    -->Almacena en la variable send un objeto de la clase Retweet.Después añade dicho objeto a cada una de las colasa del atributo  
    _timeline de cada uno de los objetos almacenados en la cola self._followers.'''


