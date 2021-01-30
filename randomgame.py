import random
class game:
    def firstfun(self):
        luckyline = 'This is an platform where you can win a number of prices. Play well and win more. Be carefull in your mind that you will get only limited turns to play. So, Play well.'
        return (list(luckyline.split(' ')))
    

    def secondFun(self, luckylist):
        count = 0
        actual = 0
        selectionwords = []
        def final(actuall):
            if actuall == 4:
                print('Won Full prize')
            elif actuall == 3:
                print('Won 50% prize')
            else:
                print('Play again')
        
        print(f'This is an platform where you can win a number of prices. Play well and win more. Be carefull in your mind that you will get only limited turns to play. So Play well. \n You have to select the words from this content')
        for i in range(15):
            selectionwords.append(random.choice(luckylist))
        # print(selectionwords)
        while True:
            guess = input()
            if guess in selectionwords:
                actual += 1
            count += 1
            if count == 4:
                print('Your chances are finished')
                final(actual)
                break

obj1 = game()
obj1.secondFun(obj1.firstfun())
