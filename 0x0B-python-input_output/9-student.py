#!/usr/bin/python3
''' define a module Student '''


class Student:
    ''' define class Student '''
    def __init__(self, first_name, last_name, age):
        ''' initialize a student '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' return dictionary description '''
        return self.__dict__
