#multithreading
##import subprocess
##import StringIO
##
##proc=subprocess.Popen(['cmd.exe','tasklist',"/FO","CSV"], stdout=subprocess.PIPE)
##output=proc.communicate()[0]
##
##for line in StringIO.StringIO(output).readlines():
##    line=line.replace(",","\t")
##    print line    
##
##print "process return code",proc.returncode
##print "process id", proc.pid
##import time
##time.sleep(2)
##print "---------------------------------------------------"
##
##print output
##
###2 way
###proc=


##################################################################

import threading
from time import sleep,ctime

class MyThread(threading.Thread):

    def __init__(self, id, lock):
        threading.Thread.__init__(self)
        self.id=id
        self.lock=lock


    def run(self):
        with self.lock:
            print 'start loop',self.id, 'at:',ctime()

        import random
        sleep(random.randrange(1,10))

        with self.lock:
            print 'loop', self.id, 'done at:',ctime()


def main():
    print 'starting at:', ctime()
    threads=[]

    nloops=range(5,10)
    for i in nloops:
        t=MyThread(i)
        threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print 'all DONE at:',ctime()


if __name__ == '__main__':
    main()
        

