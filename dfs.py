# Program to implement DFS search algorithm
# Initialization of stack
stack = []
final_path = []

# Our graph represented in form of adjacency list
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
If status is 3 -> then the node is dequeued.
'''
status = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1}

print("\t----DFS Search Algorithm------\n")
# Display the adjacency list that is being used.
print("Adjacency List Used: \n")
for key, value in adj_list.items():
    print(key, ':', value)

start = input("\nEnter the starting vertex: ")
dest = input("Enter the ending vertex: ")

# Pushing the first node onto the stack
stack.append(start)
# Setting it's status to 2 as it now goes into ready state
status[start] = 2

while True:
    # Pop the node on the top of stack
    node = stack.pop()
    # Add the popped node on the final list
    final_path.append(node)
    # Set the status of popped node to 3
    status[node] = 3
    # Get the adjacent nodes of the popped nodes from adjacent list
    adj_nodes = adj_list[node]
    # For each node that is adjacent to the popped node
    for node in adj_nodes:
        # If the node is in ready state or untouched:
        if status[node] == 1:
            # Push that node onto the stack
            stack.append(node)
            # Set the status of that node to waiting (2)
            status[node] = 2
    # If the stack is empty then exit the loop
    if not stack:
        break

print(f"\nPath from {start} to {dest} is: \n",)
for each in final_path:
    print(each, ' -> ', end='')
