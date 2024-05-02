class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
# Inisialisasi stack
s = Stack()

nama = input('Masukkan nama : ')
namaTerbalik = ''

for i in nama:
    s.push(i)
    
for i in range(s.size()):
    namaTerbalik += s.pop()

print(namaTerbalik)