import subprocess  

## MP :shell=True for pipe and directions
p=subprocess.Popen(["cat /proc/net/arp | grep 192.168.1.1| awk '{print $4}'>>/var/tmp/maclist"],shell=True)
p.wait()
###################
p=subprocess.Popen(["cat", "/var/tmp/maclist"], stdout=subprocess.PIPE)
p.wait()
#outputOfTheProcess=p.stdout.read().strip().decode('ascii')
outputOfTheProcess=p.stdout.read().strip().decode('utf-8')
print(outputOfTheProcess)


