import random
MAX, MIN = int(input("Enter Max Value: ")),int(input("Enter Min Value: "))
def alphabetaprun(depth,branch,index,player,values,alpha,beta,count):
    if depth == 0:
        count += 1
        return values[index],count
    if player:
        best = MIN
        for i in range(0,branch):
            value,count = alphabetaprun(depth-1,branch,index * 2 + i,False,values,alpha,beta,count)
            best = max(best,value)
            alpha= max(alpha,best)
            if beta <= alpha:
                break
        return best,count
    else:
        best = MAX
        for i in range(0,branch):
            value,count = alphabetaprun(depth-1,branch,index * 2 + i,True,values,alpha,beta,count)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best,count
    
ID = input("Enter your id: ") #20201003
small, big = int(input("Enter min value: ")), int(input("Enter max value: "))
depth = int(ID[0])*2
branch = int(ID[2])
print(branch)
HP = int(ID[7])*10+int(ID[6])
values = []
for i in range(branch**depth):
    values.append(random.randint(small,big))
Attack, PruneCount = alphabetaprun(depth,branch,0,True,values,MIN,MAX,count=0)
print("1. Depth and Branches ratio is ",depth,":",branch)
print("2. Terminal States (leaf node values) are ",[i for i in values])
print("3. Left life(HP) of the defender after maximum damage caused by the attacker is ",HP-Attack)
print("4. After Alpha-Beta Pruning Leaf Node Comparisons ",PruneCount)