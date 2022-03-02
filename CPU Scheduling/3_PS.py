if __name__ == "__main__":
    print("Enter the total number of process = ", end="")
    n = int(input())
    processes = []
    burst_time = []
    priority = []
    print("Enter the processes, burstTime, and priority value using space between:")
    for i in range(n):
        process, burstTime, priotyTime = input().split()
        processes.append(process)
        burst_time.append(int(burstTime))
        priority.append(int(priotyTime))

    new_burst_time = [x for _, x in sorted(zip(priority, burst_time))]
    new_processes = [x for _,x in sorted(zip(priority, processes))]
    priority.sort()

    print("After sort, my new table looks like:")
    print(f"Process    BurstTime    Priority")
    for i in range(n):
        print(f"  {new_processes[i]}\t\t\t{new_burst_time[i]}\t\t\t{priority[i]}")

    gantt_chart = "0"
    waiting_time = [0]
    burstTime_new = 0
    for i in range(n):
        burstTime_new += new_burst_time[i]
        gantt_chart += "  " + new_processes[i] + "  " + str(burstTime_new)
        if i != n-1:
            waiting_time.append(burstTime_new)

    print()
    print("My GANTT chart is: ")
    print(gantt_chart)
    # print(waiting_time)
    print()
    print("Average waiting time is: ", sum(waiting_time)/n, "ms")