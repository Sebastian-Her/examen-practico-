from Node import Node
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0  
        self.limit = limit  

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            logger.info("La pila esta totalmente vacia!")  
            return None

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item  
            self.top_item = self.top_item.get_next_node()  
            self.size -= 1  
            return item_to_remove.get_value()  
        else:
            logger.info("La pila esta totalmente vacia!")  
            return None

    def push(self, value):
        if self.has_space():
            item = Node(value) 
            item.set_next_node(self.top_item)  
            self.top_item = item  
            self.size += 1  
        else:
            logger.info("La pila esta llena ¡No queda espacio!")  

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
