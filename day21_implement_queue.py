
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def empty(self):
        return not self.stack1 and not self.stack2
        
    def push(self, num: int):
        self.stack1.append(num)
        #print(f"Pushed {num} to stack1")
        
    def peek(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def pop(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    



if __name__ == "__main__":
    
    q = MyQueue()
    
    q.push(1)
    q.push(2)
    q.push(3)
    
    print(q.peek())
    print(q.pop())   
    print(q.pop())  
    print(q.empty()) 
    print(q.pop())  
    print(q.empty()) 

    
