import random
while True:
    def randomnum():
        return random.randint(1,10)
        def getnum():
            num = input("Enter a number between 1 - 10: ")
            return num
            def numberguess(n):
                for i in range(1,11):
                    x = randomnum()
                    if i == 1 and x==n:
                        print("You won.\n")
                        y="you won"
                        print("$"*len(y))
                        break
                    elif i == 10:
                        i = "Nasty Defeat."
                        print(i)
                        print('-'*len(i))
                        print()
                        break
                    def main():
                        title ="\n NUMBER GUESSING GAME "
                        print(title)
                        print('<>'*12)
                        print()
                        num = getnum()
                        valid = num.isdigit() and 0<int(num)<11
                        if not valid:
                            print("Worning! Please enter a valid number.")
                            return num
                            numberguess(int(num))
                            if __name__ == '__main__':
                                main()