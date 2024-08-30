#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    
    def learn(self, text):
        self.text = text
        if isinstance(self.text, str):
            self.knowledge.append(self.text)