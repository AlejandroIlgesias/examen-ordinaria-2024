class Cola:
    def __init__(self):
        self.queue = []
    def añadir_elemento(self, x):
        return self.queue.insert(0, x)
    def eliminar_elemento(self):
        return self.queue.pop()
    
    def vacio(self):
        return len(self.queue) == 0
    def ultimo(self):
        return self.queue[-1]
    def primero(self):
        return self.queue[0]
    
'''La cola FIFO es perfecta para tratar y almacenar los tweets de un usuario en este caso.
El primer tweet que escribe el ususario va a ser el primero que se elimina del timeline de sus
seguidores.El objetivo seria no tener más de 5 tweets en el timeline de cada seguidor.
Si se quiere ver todos los tweets de alguien se puede hacer accediendo al atributo tweets
a traves de un método.Asi cuando llegue el sexto tweet ,se eliminará el primer tweet escrito
(el más antiguo) convirtiéndose así éste en el quinto tweet del timeline(el más reciente). '''