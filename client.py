# MATTHEW FLAVIN
# CS 478
# ASSIGNMENT 5
# 4/30/21

# IMPORTS
import socket
from datetime import date

# SET HOST AND PORT INFO
_HOST = '127.0.0.1'
_PORT = 65432

# PRINT MENU AND INFO AT START
print('\n')
print("Rock, Paper, Scissors; Classification Server")
print("Matthew Flavin")
print(date.today())
print("Example Usage: \'myhand.jpg\'")
print("Enter 'help' to see commands. \n")

# MAIN LOOP
while True:
    # INPUT PROMPT
    _COMMAND = input('>> client ').lower()

    # IF HELP COMMAND
    if _COMMAND == 'help':
        print('Ensure that server.py is running before attempting to use model.')
        print("\'quit\' to exit program.")
        print('\'filename\' to use model. \n')

    # IF QUIT COMMAND
    elif _COMMAND == 'quit':
        break

    elif _COMMAND == '':
        # PRINT MENU AND INFO AT START
        print('\n')
        print("Rock, Paper, Scissors; Classification Server")
        print("Matthew Flavin")
        print(date.today())
        print("Example Usage: \'myhand.jpg\'")
        print("Enter 'help' to see commands. \n")

    # BEGIN PREDICTION
    else:
        # CONNECT TO SERVER VIA SOCKET
        _SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _SOCKET.connect((_HOST, _PORT))

        # OPEN THE IMAGE BASED ON INPUT, I.E: paper1.png
        _FILE = open(_COMMAND, 'rb')
        _DATA = _FILE.read(1024)

        # ITERATE THROUGH FILE, SEND TO SERVER
        while (_DATA):
            _SOCKET.send(_DATA)
            _DATA = _FILE.read(1024)

        # SUCCESS MESSAGE
        print("Image Sent To Server.")

        # SHUTDOWN SOCKET 
        _SOCKET.shutdown(socket.SHUT_WR)

        # GET RESULT FROM SERVER, PRINT
        _RESULT = _SOCKET.recv(1024).decode()
        print(_RESULT)

        # CLOSE SOCKET
        _SOCKET.close()