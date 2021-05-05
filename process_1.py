import psutil
import time
import os, signal

'''
pid_file = open('pid.txt', 'r+')
pid = pid_file.readline()
pid_file.truncate(0)
pid_file.close()
'''

class SysMonitoring():
    # Asking for pid of the Flask program
    def __init__(self, pid):
        self.pid = pid

    # send signal to process id and for killing the process
    def sending_signal(self):
        os.kill(self.pid, signal.SIGUSR1)
        print("signal sent")

    # Getting the CPU Percent
    def cpu_stats(self):
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        print('-'*30)
        print('CPU PERCENT : ', cpu_percent)
        return cpu_percent

    # Getting the stats of memory and turning it into the dictionary
    def memory(self):
        mem = psutil.virtual_memory()
        '''memory_val_dict = {
                'total':mem[0],
                'available':mem[1],
                'percent':mem[2],
                'used':mem[3],
                'free':mem[4],
                'active':mem[5],
                'inactive':mem[6],
                'buffers':mem[7],
                'cached':mem[8],
                'shared':mem[9],
                'slab':mem[10],
                }'''
        memory_val_dict = {
                'total':mem[0],
                'available':mem[1],
                'percent':mem[2],
                'used':mem[3],
                'free':mem[4],
                }
        print('MEMORY PERCENT : ', memory_val_dict['percent'])
        print('-'*30)
        return memory_val_dict

    # Keeping Track of the CPU stats
    def tracking_cpu_stats(self, stats):
        if int(stats) > 80 and int(stats) <= 95:
            print('Running out of CPU!')
        elif int(stats) > 70:
            print('CPU Usage has touched the Threshold!')
            print('Program will restart the Flask Application ')
            #self.sending_signal()
            return False
        else:
            return True

    # Keeping Track of the memory
    def tracking_memory(self, mem):
        if int(mem['percent']) > 80 and int(mem['percent']) <= 95:
            print('Running out of Memory!')
        elif int(mem['percent']) > 70:
            print('Memory usage has touched the Threshold!')
            print('Program will restart the Flask Application')
            #self.sending_signal()
            return False
        else:
            return True

'''
    # Function for running
    def running(self):
        run = True
        while run:
            stats = self.cpu_stats()
            mem = self.memory()
            check_cpu_1 = self.tracking_cpu_stats(stats[0])
            check_cpu_2 = self.tracking_cpu_stats(stats[1])
            check_memory = self.tracking_memory(mem)
            if check_cpu_1 == False or check_cpu_2 == False or check_memory == False:
                run = False
            time.sleep(1)

# For Running the Program properly
if __name__ == '__main__':
    if pid == '':
        print('Please Make sure that the Flask Application is Running!')
    else:
        try:
            sm = SysMonitoring(int(pid))
        except:
            print('Pid is not proper!')
            quit()
        #sm.running()
'''
