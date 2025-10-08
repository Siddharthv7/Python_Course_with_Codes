def round_robin(processes, quantum):
    n = len(processes)
    remaining_burst_time = [process[1] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    # Simulate the round-robin scheduling algorithm
    while True:
        all_finished = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                all_finished = False
                if remaining_burst_time[i] > quantum:
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    current_time += remaining_burst_time[i]
                    waiting_time[i] = current_time - processes[i][1]
                    remaining_burst_time[i] = 0

        if all_finished:
            break

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print table header
    print("Process\tWaiting Time\tTurnaround Time")

    # Print table rows for each process
    for i in range(n):
        print(f"{processes[i][0]}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    return avg_waiting_time, avg_turnaround_time


# Example usage
if __name__ == "__main__":
    # Format for processes: [(process_id, burst_time), ...]
    processes = [(1, 10), (2, 5), (3, 8), (4, 6)]
    quantum = 2

    avg_waiting_time, avg_turnaround_time = round_robin(processes, quantum)
    print("\nAverage Waiting Time using Round Robin algorithm:", avg_waiting_time)
    print("Average Turnaround Time using Round Robin algorithm:", avg_turnaround_time)
