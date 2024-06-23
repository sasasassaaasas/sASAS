# # # import random

# # # z,p,r=0,0,100

# # # A=[random.randint(-200,200) for i in range(r)]

# # # print(*A)

# # # for i in range(r):

# # #    if A[i]==0: z+=1

# # #    elif A[i]>0: p+=1

# # # print("max=",max(A),"  mix=",min(A))

# # # print ("0=",z,"positive=",p,"negative=",r-p-z)


















# # # from random import randint

# # # lst = [randint(-100, 100) for _ in range(20)]

# # # print(f' {min(lst)}')

# # # print() {max(lst)}')

# # # print(f' {lst.count(0)}')

# # # print(f' {len(filter(lambda x: x < 0, lst))}')

# # # print(f' {len(filter(lambda x: x > 0, lst))}')




# # def is_palindrome(input_str):

# # cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())

# # reversed_str = cleaned_str[::-1]

# # return cleaned_str == reversed_str

# # user_input = input(" ")

# # if is_palindrome(user_input):

# # print(".")

# # else:

# # print(".")

# def modify_text(text, reserved_words):

# for word in reserved_words:

# text = text.replace(word, word.upper())

# return text

# user_text = input(": ")

# reserved_words = input("): ").split()

# modified_text = modify_text(user_text, reserved_words)

# print("")

# print(modified_text)

# def count_sentences(text):

# sentences = text.split('.')

# return len(sentences)

# user_text = input(": ")

# sentences_count = count_sentences(user_text)

# print(":", sentences_count)