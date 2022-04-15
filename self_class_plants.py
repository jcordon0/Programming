# -*- coding: utf-8 -*-
class Plants:
    def __init__(self, thorns, color, size):
        
        self.__thorns = thorns
        self.__color = color
        self.__size = size
    
    def set_thorns(self, thorns):
        self.__thorns = thorns
        
    def set_color(self, color):
        self.__color = color
        
    def set_size(self, size):
        self.__size = size
        
    def set__thorns(self):
        return self.__thorns
    
    def set__color(self):
        return self.__color
    
    def set__size(self):
        return self.__size