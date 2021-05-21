import subprocess
import psutil

a = subprocess.run(['ipconfig'])

b = subprocess.run(['ipconfig'])

procs_list = [psutil.Process(a.pid), psutil.Process(b.pid)]

def on_terminate(proc):
     print("process {} terminated".format(proc))

# waits for multiple processes to terminate
gone, alive = psutil.wait_procs(procs_list, timeout=3, callback=on_terminate)