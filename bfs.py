# Program to implement the BFS search algorithm

front = -1
rear = -1

queue = []

orig = []

adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['B', 'G'],
    'D': ['C', 'G'],
    'E': ['C', 'F'],
    'F': ['C', 'H'],
    'G': ['F', 'H', 'I'],
    'H': ['E', 'I'],
    'I': ['F']
}
'''
If status is 1 -> ready state
If status is 2 -> the node is enqueued and is said to be in waiting state.
If status is 3 -> then then node is dequeued.
'''
status = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1}

print("\t------BFS Search Algorithm------\n")

print("Graph used is shown by the below adjacency list")
print("Adjacency List: \n")
for key, value in adj_list.items():
    print(key, ':', value)
start = input("\nEnter the starting vertex: ")
dest = input("Enter the ending vertex: ")
queue.append(start)
orig.append('0')
front += 1
rear += 1
while True:
    selected_node = queue[front]
    status[selected_node] = 3
    front += 1
    adj_nodes = adj_list[selected_node]
    for node in adj_nodes:
        
        if status[node] == 1:
        
            queue.append(node)
            orig.append(selected_node)
          
            status[node] = 2
          
            rear += 1
   
    if queue[rear] == dest:
        break

final_path = list()

node = queue[rear]  
parent = orig[rear] 

final_path.append(node)

while True:
    
    index = queue.index(parent)
   
    node = queue[index]
   
    parent = orig[index]
   
    final_path.append(node)
   
    if parent == '0':
        break

final_path = final_path[::-1]

print(f"\nPath from {start} to {dest} is: \n",)
for each in final_path:
    print(each, ' -> ', end='')
