
class countcost:
    def ballonCost(self):
        green = 0
        purple = 0
        users = []
        new = []
        final = []
        test_cases = int(input())
        bal_cost = input().split(' ')
        a,b = list(map(int, bal_cost))
        for numbers in range(test_cases):
            participants = int(input())
            
            for i in range(participants):
                help = input().split(' ')
                users.append(help)
            
            for i in range(len(users)):
                for j in range(len(users[i])):
                    new.append(int(users[i][j]))
            for i in range(len(new)):
                if i%2 == 0:
                    if new[i] == 1:
                        green += 1
                if i%2 != 0:
                    if new[i] == 1:
                        purple += 1

            final.append((a*green)+(b*purple))
            users.clear()
            new.clear()
            participants = 0
            green = 0
            purple = 0
        for nm in range(len(final)):
            print(final[nm])
            
        
obj = countcost()
obj.ballonCost()
