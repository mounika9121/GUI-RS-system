import paramiko


class SSHInterface:

    def __init__(self, ip, username, password):
        self.ssh_client = None
        self.ip = ip
        self.username = username
        self.password = password
        #self.cmd = cmd

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("please wait, connecting with remote server....")
            self.ssh_client.connect(hostname=self.ip, username=self.username, password=self.password)
            print("Successfully connected to server")
        except Exception as e:
            raise Exception("Fail to connect server: {}".format(str(e)))

    def runCommand(self,cmd):
        #stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        response = stdout.read().decode('utf-8')
        return (response)

if __name__ == "__main__":
    conn = SSHInterface('192.168.0.18','sai','sai')
    conn.connect()
    resp = conn.runCommand('ls')
    print(resp)


"""
user_name = "sai"
passwd = "sai"
ip = "192.168.0.16"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("please wait, connecting with remote server")
ssh_client.connect(hostname=ip, username=user_name, password=passwd)
cmd = "ls -lrt path"
print("please wait, executing command")
stdin,stdout,stderr = ssh_client.exec_command(cmd)
print("successfully executed command")
output = stdout.read().decode('utf-8')
print(output)
"""