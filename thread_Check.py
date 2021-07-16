import threading

# When creating threads, add them to this list
list_Of_Threads = []


# Function that appends thread to list
def append_Thread(thread):
    list_Of_Threads.append(thread)


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


# Active thread being checked
def active_Thread():
    active = True

    while active:
        pass


# Create threads
thread_1 = threading.Thread(target=active_Thread)
thread_2 = threading.Thread(target=thread_Check)


# Start threads
thread_1.start()
thread_2.start()

# Append active thread to list
append_Thread(thread_1)
