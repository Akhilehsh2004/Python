queue = [1,2,3,4,5,6]

print("Original queue is : ", queue)

queue.append(7)

print("Queue after inseertion is ", queue)

queue.pop(0)

print("Queue after deletion is : ", queue )

print("Value obtained after peep operation is : ", queue[len(queue) - 1])