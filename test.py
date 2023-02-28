
# Python3 program to demonstrate
# working of Alpha-Beta Pruning
 
# Initial values of Alpha and Beta
MAX, MIN = 1000,-1000
 
# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth,branch, nodeIndex, maximizingPlayer,
            values, alpha, beta,count=0):
  
    # Terminating condition. i.e
    # leaf node is reached
   
    if depth == 0:
        count += 1
        return values[nodeIndex],count
 
    if maximizingPlayer:
      
        best = MIN
 
        # Recur for left and right children
        # number of branch
        for i in range(0, branch):
             
            val,count= minimax(depth -1,branch, nodeIndex * 2 + i,
                          False, values, alpha, beta,count)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                
                break
        
        return best, count
      
    else:
        best = MAX
 
        # Recur for left and
        # right children
        for i in range(0, branch):
          
            val,count = minimax(depth -1,branch, nodeIndex * 2 + i,
                            True, values, alpha, beta,count)
            best = min(best, val)
            beta = min(beta, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                
                break

        return best, count
      
# Driver Code

  
ID = '20201003'
depth = int(ID[0])*2
branch = int(ID[2])
print(branch)
HP = int(ID[7])*10+int(ID[6])
values = [18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18] 
print("Left life(HP) of the defender after maximum damage caused by the attacker is ",minimax(depth,branch,0,True,values,MIN,MAX,count=0))