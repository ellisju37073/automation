# Automate Ping
# Justin Ellis
# CNE 335
from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Justin Ellis")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server_ip = "34.209.241.29"
    my_rsa_key_file = r"C:\Users\ellis\.ssh\JE_CNE"
    username = "ubuntu"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))

    # TODO - Call Ping method and print the results
