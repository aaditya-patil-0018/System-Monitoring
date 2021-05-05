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
    #traceback.print_stack()
    print(repr(traceback.extract_stack()))
    print(repr(traceback.format_stack()))
    #exit()

def register_signal():
    return signal.signal(signal.SIGUSR1, sigusr1_handler)

def loop():
    while True:
        time.sleep(2)

def monitoring():
    pid = os.getpid()
    systm = SysMonitoring(pid)
    run = True
    while run:
        stats = systm.cpu_stats()
        mem = systm.memory()
        check_cpu_1 = systm.tracking_cpu_stats(stats[0])
        check_cpu_2 = systm.tracking_cpu_stats(stats[1])
        check_memory = systm.tracking_memory(mem)
        if check_cpu_1 == False or check_cpu_2 == False or check_memory == False:
            #os.kill(self.pid, signal.SIGUSR1)
            register_signal()
            sigusr1_handler()
            run = False
            return False
        return True

if __name__ == '__main__':
    #print(pid_write())
    #loop()
    stats = monitoring()
    while stats:
        print('This program is running')
        time.sleep(1)
