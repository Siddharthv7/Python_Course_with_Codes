def SCAN(queue, head, direction, max_size, min_size):
    total_seek_time = 0
    current_track = head

    queue.sort()

    while queue:
        if direction == "right":
            queue.append(max_size)

            for track in range(current_track, max(queue) + 1):
                if track in queue:
                    total_seek_time += abs(current_track - track)
                    current_track = track
                    queue.remove(track)
            direction = "left"
        
        elif direction == "left":
            for track in range(current_track, min(queue) - 1, -1):
                if track in queue:
                    total_seek_time += abs(current_track - track)
                    current_track = track
                    queue.remove(track)
            direction = "right"

    return total_seek_time

# Example usage:
if __name__ == "__main__":
    queue = [98, 183, 37, 122, 14, 124, 65, 67]
    max_size = 200
    min_size = 0
    head = 53
    direction = "right"

    total_seek_time = SCAN(queue, head, direction, max_size, min_size)
    print("Total seek time:", total_seek_time)
