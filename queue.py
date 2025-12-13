#This file contence a class which is queue implementation and we create a instance of it and say queue_obj1.add(request) 
# it will add this request in obj1_array and if we create queue_obj2 and we add its own seperate reuest then it will store
# the request in that instance array 



class MailQueue:
    def __init__(self):
        self.queue = []

    def add(self, request):
        self.queue.append(request)
        print(f"Added request: {request}")

    def process(self):
        request = self.queue.pop(0)
        print(f"Processing request: {request} and updated array is {self.queue}") 
