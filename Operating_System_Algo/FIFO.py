from queue import Queue

def pageFaults(pages, n, capacity):
    # To represent set of current pages.
    # We use a set so that we quickly check if a page is present in the set or not.
    s = set()

    # To store the pages in FIFO manner
    indexes = Queue()

    # Start from initial page
    page_faults = 0
    for i in range(n):
        # Check if the set can hold more pages
        if len(s) < capacity:
            # Insert it into the set if not present already which represents page fault
            if pages[i] not in s:
                s.add(pages[i])

                # Increment page fault
                page_faults += 1

                # Push the current page into the queue
                indexes.put(pages[i])

        # If the set is full then need to perform FIFO
        else:
            # Check if the current page is not already present in the set
            if pages[i] not in s:
                # Pop the first page from the queue
                val = indexes.queue[0]
                indexes.get()

                # Remove the indexes page
                s.remove(val)

                # Insert the current page
                s.add(pages[i])

                # Push the current page into the queue
                indexes.put(pages[i])

                # Increment page faults
                page_faults += 1

    return page_faults

# Driver code
if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    page_faults = pageFaults(pages, n, capacity)
    hits = n - page_faults
    print("Page faults =", page_faults)
    print("Number of hits =", hits)
    print("Hit ratio =", hits / page_faults if page_faults > 0 else 0)
