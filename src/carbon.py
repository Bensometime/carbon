import subprocess

text = subprocess.call("ls", shell=True)
print(text)
subprocess.call("exit", shell=True)
