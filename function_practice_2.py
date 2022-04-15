# -*- coding: utf-8 -*-

def dog(n):
    print("Sounds like a dog.") 
    n = int(input(""))
    return n


def cat():
    print("Sounds like a cat.")


def main():
    answer = input("Hello, type in woof or meow:\n")

    if answer.lower() == "meow":
        cat()
    elif answer.lower() == "woof":
        dog(answer)
    
if __name__ == '__main__':
    main()  