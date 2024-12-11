# Node.py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_next_node(self, next_node):
        self.next = next_node