input_queue = list(map(int, input("Enter the value for queue: ").split(", "))) #98, 183, 37, 122, 14, 124, 65, 67
head_start = int(input("Enter the head starts : "))
lower_bound = int(input("Enter the lower bound : "))
upper_bound = int(input("Enter the upper bound : "))
# print(input_queue)
# print(head_start)
path = []
path.append(head_start)
total_distance = ""
ans = 0
head_to_lower_bound = []
head_to_upper_bound = []
while input_queue != []:
    for x in input_queue:
        if x < head_start:
            head_to_lower_bound.append(x)
            input_queue.pop(input_queue.index(x))
        elif x > head_start:
            head_to_upper_bound.append(x)
            input_queue.pop(input_queue.index(x))
head_to_lower_bound.append(lower_bound)
head_to_lower_bound.sort()
head_to_upper_bound.sort()
# print(head_to_lower_bound)
# print(head_to_upper_bound)
while head_to_upper_bound != []:
    x = 0
    if head_to_upper_bound != [] and head_to_lower_bound == []:
        x = head_to_upper_bound.pop(0)

    if head_to_lower_bound != []:
        x = head_to_lower_bound[-1]
        head_to_lower_bound.pop(head_to_lower_bound.index(x))
    path.append(x)
    if x > head_start:
        total_distance += "(" + str(x) + "-" + str(head_start) + ")"
        ans += (x - head_start)
    else:
        total_distance += "(" + str(head_start) + "-" + str(x) + ")"
        ans += (head_start - x)

    if len(head_to_upper_bound) > 0:
        total_distance += " + "

    head_start = x

print(f"Path: {path}")
print(f"Total Distances: {total_distance}")
print(f"Illustration shows total head movement of {ans} cylinders")