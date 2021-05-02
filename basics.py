environment_matrix = [[None, 0],
                  [-100, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 100],
                  [0, 0],
                  [100, 0],
                  [0, 0],
                  [0, None]]

print type(environment_matrix)
#environement matrix=reward,action   ,state is the index value  ---> environment_matrix[1] = 2nd cell [-100,0] means if we move left (first value) and goes to 1st state, reward is -100 and move right reward is 0

#q_table = [[left,right-stat1],[left,right-state2],...[state10]]

# in q table each column are the actions and the rows are the states
#values : maximum expected reward that the robot will get if it takes that action at that state

q_table = [[0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0]]

#we need to updte values at each iteration---this is a iterative process

# Q learnign algortihm
"""1.initialize q table
2.choose an action
3.perform action
4.measure reward
5.update q value

New Q(s,a) = old Q(s,a)  + alpha * [R(s,a)+gamma*maxQ'(s',a') - old Q(s,a)]

alpha = learning rate 
gamma = discount factor

maxQ'(s',a') = maximum expected future reward given the new state (s') and all posible actions at that state


"""

#initial_state = 2

#initial_action = 1        # 0 = left ,1 = right

#access item in a list of lists

print environment_matrix[1][0]


#function to update  q table 

#it takes a state and a action as inputs 

print q_table

def qTableUpdate(s,a):
	q_table[s][a] = q_table[s][a] + 0.9*(environment_matrix[s][a] +1.0*(max(q_table[s+a][0],q_table[s+a][1]))-q_table[s][a])


#max() =  maximum expected future reward given the new state (s') and all possible actions at that new state

qTableUpdate(5,1)  #sart from state 6 and move right

print q_table   #output 6th state = [0,90]  that means best action in that state is move right as seen in reard table also---confirmed


#now we are in  state 7 ...and choose a random action...lets say right(1)
qTableUpdate(6,1)
print q_table

qTableUpdate(7,1)
print q_table

qTableUpdate(8,1)
print q_table

qTableUpdate(9,0)
print q_table

qTableUpdate(8,0)
print q_table

qTableUpdate(7,0)
print q_table

#now 8th row updated--> best acrtion is in state 8th is to move left as confirmed also by reqard table

#next : utomate this process using a loop



