if __name__ == "__main__":

    n = int(input()) #number of process
    processes = []
    burst_time = []
    for i in range(n):
        process, burstTime = input().split()
        processes.append(process)
        burst_time.append(int(burstTime))

    new_processes = [x for _,x in sorted(zip(burst_time, processes))]
    burst_time.sort()

    gantt_chart = "0"
    waiting_time = [0]
    burstTime_new = 0
    for i in range(n):
        burstTime_new += burst_time[i]
        gantt_chart += "  " + new_processes[i] + "  " + str(burstTime_new)
        if i != n-1:
            waiting_time.append(burstTime_new)

    print(new_processes)
    print(burst_time)
    print("My GANTT chart is: ")
    print(gantt_chart)
    print(waiting_time)

    print("Average waiting time is: ", sum(waiting_time)/n, "ms")