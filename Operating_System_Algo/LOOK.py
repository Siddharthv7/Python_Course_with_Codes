def LOOK(queue, head, direction):
    total_seek_time = 0
    current_track = head

    queue.sort()

    while queue:
        if direction == "right":
            for track in range(current_track, max(queue) + 1):
                if track in queue:
                    total_seek_time += abs(current_track - track)
                    current_track = track
                    queue.remove(track)
            if queue:
                direction = "left"
                       
        elif direction == "left":
            for track in range(current_track, min(queue) - 1, -1):
                if track in queue:
                    total_seek_time += abs(current_track - track)
                    current_track = track
                    queue.remove(track)
            if queue:
                direction = "right"

    return total_seek_time

# Example usage:
if __name__ == "__main__":
    queue = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    direction = "right"
    total_seek_time = LOOK(queue, head, direction)
    print("Total seek time:", total_seek_time)
