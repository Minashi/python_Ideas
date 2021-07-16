import threading

# When creating threads, add them to this list
list_Of_Threads = []


# function thread to check if threads are alive
def thread_Check():
    # checker if a thread died
    error_Check = False

    # Loop, and when a thread dies do else
    while not error_Check:
        # Check each thread in list if dead
        for thread in list_Of_Threads:
            if thread.is_alive():
                pass
            else:
                error_Check = True
    else:
        # if thread died do this
        pass


# Create thread
thread_1 = threading.Thread(target=thread_Check)

# Start thread
thread_1.start()
