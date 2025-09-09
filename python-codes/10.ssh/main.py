import paramiko
ip = "127.0.0.1"
kullanici = "mpekmezci"
sifre = "my-password-01"
komut = "ls -al"
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,kullanici,sifre,timeout = 10)

stdin,stdout,stderr = ssh.exec_command(komut)
sonuc = stdout.read()
print(sonuc.decode("utf-8"))

ssh.close()
