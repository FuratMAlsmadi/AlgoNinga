""" Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob's computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it."""
#class packets 
#user 

import random


class Alice :
    def __init__(self,name):
        self._name =  name 
    def send(self):
        packet = random.sample(range(0, 3000), 5)
        return packet
        
class Bob:
    def __init__(self,name,status="Listen"):
        self._name = name 
        self._status = status 
        self._packets = [0]*5
    def receive(self,packets):
        self._packets = packets
    def get_state(self):
        return self._status 
    def change_state(self,new_status):
        self._status = new_status
    def get_packets(self):
        return self._packets
    def clean_packet(self):
        self._packets = [0]*5
        print("Cleaning......")
        

x = True 
person1 = Alice("Alice")
person2 = Bob("Bob")
while x :
    user = input("Send Exit: ")
    if user.lower().strip() == "send":
       if person2.get_state() == "Listen":
           person2.receive(person1.send())
           print(person2.get_packets())
           person2.clean_packet()
       person2.change_state(random.choice(["Listen","NotListening"]))
    if user.lower().strip() == "exit":
        x = False 