def bankers_algorithm(allocated, max_needed, available):
    # Get the number of processes and resources
    num_processes = len(allocated)
    num_resources = len(available)

    # Initialize arrays to track the state of each process and resource
    finish = [False] * num_processes
    safe_sequence = []
    work = available.copy()

    # Calculate the remaining needs of each process
    need = [[max_needed[i][j] - allocated[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # Iterate until all processes are finished or no safe sequence is possible
    while len(safe_sequence) < num_processes:
        # Flag to check if a process is found that can be allocated resources
        found = False
        # Iterate through each process
        for i in range(num_processes):
            # Check if the process is not finished and its resource needs can be satisfied
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                # Process can be allocated resources
                finish[i] = True
                safe_sequence.append(i)
                # Release allocated resources
                for j in range(num_resources):
                    work[j] += allocated[i][j]
                found = True
                break  # Break the loop to search for the next process

        # If no such process is found, break the loop to avoid infinite loop
        if not found:
            break

    # Check if a safe sequence is found
    if len(safe_sequence) == num_processes:
        return safe_sequence
    else:
        return None

# Example usage
allocated_resources = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1]   # P3
]

max_resources = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2]   # P3
]

available_resources = [3, 3, 2]

safe_sequence = bankers_algorithm(allocated_resources, max_resources, available_resources)
if safe_sequence:
    print("Safe Sequence:", safe_sequence)
else:
    print("No safe sequence exists!")
