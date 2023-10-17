import os 
import random 
import time 
import sys 
from colorama import Fore, Back 




def lock1_caesar_puzzle():
    # generating and storing nums
    rand_repeat = random.randint(3, 9)
    nums = []

    for i in range(rand_repeat):
        pass_question = random.randint(1, 26)
        nums.append(pass_question)

    return nums 
# =============================================
# print(lock1_caesar_puzzle())


def lock1_caesar_code(nums):
    # nums = lock1_caesar_puzzle()

    lock1_code = ""
    for n in nums:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        letter = alpha[n-1]
        lock1_code = lock1_code + letter

    return lock1_code
# =============================================
# nums = lock1_caesar_puzzle()
# code = lock1_caesar_code(nums)
# print(code)


def lock2():
    code = [6, 19, 15, 3, 9, 5, 20, 25]
    print(f"\n{code}")
    
    print("\nDecode the above code")
    user_in = input("> ")
# =============================================


# =============================================
def lock_master(thing_to_lock=lock2):
    correct_ans = False 

    while not correct_ans: 
        lock1 = lock1_caesar_puzzle()
        code = lock1_caesar_code(lock1)

        print(lock1)
        user_in = input("\nConvert the above to a string of lowercase letters: ")

        if user_in == code:
            print("*Correct*")
            correct_ans = True 
            thing_to_lock()

        else:
            os.system("cls")
# =============================================
# lock_master()