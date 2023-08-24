#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self,first_name,last_name):
        super().__init__(self,first_name,last_name)
        self.knowledge = []

    
    def learn(self, skill):
        if isinstance(skill, str):
            self.knowledge.append(skill)
            return self.knowledge
        