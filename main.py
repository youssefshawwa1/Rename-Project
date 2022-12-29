from jCreater import jsonCreater as JSO
from Renam import ReMovDelCon as R
def main():
    while True:
        print("What Do you Want To Do: \n")
        userWant = str(input("A: All\nR: Rename & Convert SRT & Move\nJ: Create JSON\n>  "))
        if len(userWant) < 1 or userWant == 'exit':
            print('\n\n\nExiting...\nGoodBye.')
            break
        settings = str(input("Settings D: Default\nC: Costom\n>  "))
        if len(settings) < 1 or settings == 'exit':
            print('\n\n\nExiting...\nGoodBye.')
            break
        elif settings == 'c':
            s = False
        elif settings == 'd':
           s = True
        else:
            print('Please Chose or type exit: ')
            continue
        if userWant == 'a':
            R(s)
            JSO(s)
            continue
        elif userWant == 'r':
            R(s)
            continue
        elif userWant == 'j':
            JSO(s)
            continue
        else:
            print('Please Chose or type exit: ')
            continue
if __name__ == "__main__":
    main()