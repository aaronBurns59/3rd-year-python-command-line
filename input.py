# import used for reading input from the console
import sys

# prints the name of the script that is running
# print (f"Script is called {sys.argv[0]}")

# for argv in sys.argv:
#     # allows you to list the extra information in a command line
#     print(sys.argv)

if len(sys.argv) == 2:
    print("We're ready to go.")
else:
    print("you should supply a single file name. ")