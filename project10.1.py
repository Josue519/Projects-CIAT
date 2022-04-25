"""
File project10.1.py
Josue Marante 

Illustrates the producer/consumer problem with thread synchronization.
Makes producer wait intil multiple consumers read each datum.


"""

import time, random 
from threading import Thread, currentThread, Condition 

class SharedCell(object):
    """Shared data for the producer/consumer problem. """

    def __init__(self, numConsumers) : 
        self.numConsumers = numConsumers
        self.waitList = []
        self.data = -1
        self.writeable = True 
        self.condition = Condition()
        self.consumerCondition = Condition()

    def setData(self, data) : 
        """Producer's method to write to shared data."""
        self.condition.acquire()
        while not self.writeable:
            self.condition.wait()
            print("%s setting data to %d" % \
                (currentThread().getName(), data))
            self.data = data 
            self.writeable = False 
            self.condition.notify()
            self.condition.release()
            if len(self.waitlist) == self.numConsumers:
                #Reset the wait list, release the writer, 
                #and realease all readers.
                self.waitList = []
                self.consumerCondition.acquire()
                self.consumerCondition.notifyAll()
                self.consumerCondition.release()

    def getData(self):
        """Consumer's method to read from shared data."""
        #wait on consumer condition if you have 
        #already consumed this datum.
        if currentThread() in self.waitList:
            self.consumerCondition.acquire()
            self.consumerCondition.wait()
            #wait for the writer to finish if datum has not been produced.

            self .condition.acquire()
            while self.writeable:
                self.condition.wait()
            print("%s accessing data %d" % \
                 (currentThread().getName(), self.data))
            #check for releasing the producer and other consumers 
            if len(self.waitlist) == self.numConsumers -1:
                #Reset the waitlist, release the writer, and all readers 
                self.waitList = []
                self.writeable = True
                self.consumerCondition.acquire()
                self.consumerCondition.notifyAll()
                self.consumerCondition.release()
            else:
                #more consumers, will go on wait list
                self.waitlist.append(currentThread())
            self.condition.notify()
            self.condition.release()
            return self.data
class Producer(Thread):
    """Represents a producer."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accessrs, and a maximum sleep interval."""
        Thread.__init__(self, name = "Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and write to shared cell. """
        print("%s starting up\n" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())
        

class Consumer(Thread):
    """Represents a consumer."""

    def __init__(self, name, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accessrs, and a maximum sleep interval."""
        Thread.__init__(self, name = "Consumer" + name)
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and write to shared cell. """
        print("%s starting up\n" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.setData(count + 1)
        print("%s is done consuming\n" % self.getName())

def main():
    """Get number of accesses from user, create a shared cell."""
    numConsumers = int(input("Enter the number of consumer: "))
    accessCount = int(input("Enter the number of consumers: "))
    cell = SharedCell(numConsumers)
    p = Producer(cell, accessCount, 4)
    consumers = []
    for count in range(numConsumers):
        consumers.append(Consumer(str(count), cell, accessCount, 4))
    print("Starting the threads")
    p.start()
    for c in consumers:
        c.start()


if __name__ == "__main__":
    main()


    

