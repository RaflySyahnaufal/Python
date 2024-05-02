class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()  # Perbaikan: tambahkan tanda kurung ()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

# Inisialisasi stack  
s = Stack()

# Push elemen ke stack
s.push('B')
s.push('U')
s.push('D')
s.push('I')

# Memanggil data terakhir pada stack dan menghapusnya
print(s.pop())  # Output: 'I'
print(s.pop())  # Output: 'D'
print(s.pop())
print(s.pop())