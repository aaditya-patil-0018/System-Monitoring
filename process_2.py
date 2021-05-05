import signal
import traceback
import time, os, sys
from process_1 import SysMonitoring

# This function is not needed for now; as we are running this file directly
def pid_write():
    pid_file = open('pid.txt', 'w')
    pid = os.getpid()
    pid_file.write(str(pid))
    pid_file.close()
    return pid

# This function is for receiving the signal and Tracebacking the problem
def sigusr1_handler():
    print("Received SIGUSR1 ")
    #traceback.print_stack()   # This method was not working so it's commented
    tb = open('traceback.txt', 'w')
    tb.write(f'{repr(traceback.extract_stack())}\n')
    tb.write(f'{repr(traceback.format_stack())}')
    tb.close()
    print('Traceback has been written in the traceback.txt file!!')
    #exit()

# This is for registering the signal
def register_signal():
    return signal.signal(signal.SIGUSR1, sigusr1_handler)

# This function is for Monitoring System
# We use the methods from process 1 file here
# This is more like the running function which we was used in process 1 first
def monitoring(pid):
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
    # Getting the pid of this program
    pid = os.getpid()
    # Calling the monitoring process
    stats = monitoring(pid)
    # While loop for keep running the process until every stats of system is well
    while stats:
        print('This program is running')
        time.sleep(2)
        # Keeping check of system
        stats = monitoring(pid)
