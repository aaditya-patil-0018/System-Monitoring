import signal
import traceback
import time, os, sys
from process_1 import SysMonitoring

def pid_write():
    # For storing the pid of the file running
    pid_file = open('pid.txt', 'w')
    # Getting the pid
    pid = os.getpid()
    # Writing the pid
    pid_file.write(str(pid))
    # Closing the file
    pid_file.close()
    return pid

def sigusr1_handler():
    print("Received SIGUSR1 ")
    traceback.print_stack()
    print(repr(traceback.extract_stack()))
    print(repr(traceback.format_stack()))
    exit()

def register_signal():
    return signal.signal(signal.SIGUSR1, sigusr1_handler)

def loop():
    while True:
        time.sleep(2)


if __name__ == '__main__':
    #print(pid_write())
    #loop()
    pid = os.getpid()
    systm = SysMonitoring(pid)
    systm.running()
    #systm.tracking_memory()
    #systm.tracking_cpu_stats()
