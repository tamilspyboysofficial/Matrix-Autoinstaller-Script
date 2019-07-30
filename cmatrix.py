import subprocess
a = ("cmatrix")
def cmatrix():
    subprocess.call("sudo apt-get install cmatrix", shell=True)
    b = subprocess.call(a)

cmatrix()
