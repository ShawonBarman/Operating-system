def findWaitingTime(n, bt, wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0
    while (1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0):
                done = False

                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if (done == True):
            break

if __name__ == "__main__":
    n = int(input("Enter the total number of process = "))
    processes = []
    burst_time = []
    print("Enter the processes, and burstTime using space between:")
    for i in range(n):
        ps, burstTime = input().split()
        processes.append(ps)
        burst_time.append(int(burstTime))

    quantam = int(input("Enter the Quantam value = "))

    wt = [0] * n
    findWaitingTime(n, burst_time, wt, quantam)

    gantt_chart = "0"
    burstTime_new = 0
    while max(burst_time) > 0:
        for i in range(n):
            if burst_time[i] >= quantam:
                burstTime_new += quantam
                burst_time[i] -= quantam
                gantt_chart += "  " + processes[i] + "  " + str(burstTime_new)
            elif burst_time[i] > 0 and burst_time[i] < quantam:
                x = burst_time[i]
                burstTime_new += x
                burst_time[i] -= x
                gantt_chart += "  " + processes[i] + "  " + str(burstTime_new)

    print()
    print("My GANTT chart is: ")
    print(gantt_chart)
    print()
    print("Average waiting time is: ", sum(wt)/n, "ms")
