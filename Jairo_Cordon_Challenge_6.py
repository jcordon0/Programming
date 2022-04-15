# -*- coding: utf-8 -*-
def FileControl():
    
    print("\n")
    fun_files = open('C:\\Users\\JCord\\Desktop\\FunWithFiles.txt', 'r')
    
    movie_1 = fun_files.readline()
    movie_2 = fun_files.readline()
    movie_3 = fun_files.readline()
    
    print('************************')
    print(f'{movie_1}\n{movie_2}\n{movie_3}')
    print('************************')
    
    fun_files = open('C:\\Users\\JCord\\Desktop\\FunWithFiles.txt', 'a')
    question = input("What is your favorite movie?\n")
    movie_4 = question
    fun_files.write(f'\n{movie_4}')
    
    fun_files.close()
    print(f'\nGood choice, I also like {movie_4}.')
    
def main():
    FileControl()
    
if __name__ == '__main__':
    main()