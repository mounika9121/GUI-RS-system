from dependencies.ssh_connect import SSHInterface



conn2 = SSHInterface('192.169.01.3', 'root', 'root@123')
conn2.connect()