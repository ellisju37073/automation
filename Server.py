import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file, username, upgrade_command):
        # TODO -
        self.server_ip = server_ip
        self.username = username
        self.command = upgrade_command
        self.key_file = key_file


    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 5 %s" % self.server_ip) #https://stackoverflow.com/questions/48468135/baccess-denied-option-c-requires-administrative-privileges
        return result

    def upgrade(self):
        # TODO - Use os module to ping the server
        #https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/
        # Create the ssh client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file(self.key_file)
        # Make the connection to the server
        ssh_client.connect(hostname=self.server_ip, username=self.username, pkey=k)

        # execute the command
        #https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/#:~:text=Using%20Paramiko%20Module%20in%20Python%20to%20Execute%20Remote,lsb_release%20-a%20on%20our%20remote%20server%2C%20side-b%3A%20
        stdin, stdout, stderr = ssh_client.exec_command(self.command)

        # Return the result from both stdout and error
        result = stdout.readlines() + stderr.readlines()

        # Disconnect
        ssh_client.close()

        return result