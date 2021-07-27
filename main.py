import sys # import sys to get command line arguments
from parking_lot.run_commands import RunCommands

run_command_obj = RunCommands()

try:
    input_file = sys.argv[1]
except IndexError as e:
    input_file = None


if input_file and input_file.endswith(".txt"):
    
    with open(input_file) as fp:
        commads = fp.readlines()

    for command_input in commads:
        command_input = command_input.strip().split(" ")
        print(run_command_obj.run_command(command_input))
else:
    
    while True:
        command_input = input().strip().split(" ")
        print(run_command_obj.run_command(command_input))
    

