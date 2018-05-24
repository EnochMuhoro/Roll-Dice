import random
def main():
    min=1
    max=6
    roll_again="yes"
    print("rolling the dice...")
    print("the values are...")
    print("random.randint(min,max)")
    print(random.randint(min,max))
    roll_again = input ("roll the dice again?")
if  __name__=='__main__':main()