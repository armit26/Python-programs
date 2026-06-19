import time

start_time = None
total_time = 0

while True:
    print("====== Study Session Tracker ======")
    print("1. Start Session")
    print("2. End Session")
    print("3. Show Total Study Time")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if start_time is None:
            start_time = time.time()
            print("Study session started.")
        else:
            print("A study session is already running.")

    elif choice == 2:
        if start_time is not None:
            end_time = time.time()

            session_duration = end_time - start_time
            total_time = total_time + session_duration

            start_time = None

            print("Study session ended.")
            print("Session duration:", round(session_duration, 2), "seconds")
        else:
            print("No active study session.")

    elif choice == 3:
        hours = int(total_time // 3600)
        minutes = int((total_time % 3600) // 60)
        seconds = int(total_time % 60)

        print("Total study time today:")
        print(hours, "hours", minutes, "minutes", seconds, "seconds")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")