def sjf(processes):
    n = len(processes)
    burst_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    # Extract burst times from processes
    for i in range(n):
        burst_time[i] = processes[i][1]

    # Sort processes based on burst time
    processes.sort(key=lambda x: x[1])

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]
        total_waiting_time += waiting_time[i]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]
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
    processes = [(1, 6), (2, 8), (3, 7), (4, 3)]

    avg_waiting_time, avg_turnaround_time = sjf(processes)
    print("\nAverage Waiting Time using SJF algorithm:", avg_waiting_time)
    print("Average Turnaround Time using SJF algorithm:", avg_turnaround_time)
