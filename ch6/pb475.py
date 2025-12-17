# Write a "pager" program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing
# each time to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to
# close the file.
filename = input("Enter file name: ")
f = open(filename, "r")
while True:
    count = 0
    # Display 25 lines
    while count < 25:
        line = f.readline()
        if line == "":
            f.close()
            print("End of file")
            exit()
        print(line, end="")
        count += 1

    # Ask user
    choice = input("\nEnter 'continue' to see more or 'stop' to exit: ")

    if choice == "stop":
        f.close()
        print("File closed")
        break