import datetime
import time
import threading

stop_thread = False
global_tank = []
global_stocke_1 = []
global_stocke_2 = []


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task(threading.Thread):
    name = None
    period = None
    execution_time = None

    ############################################################################
    def __init__(self, name, period, execution_time, tank_write=False, stocke_write=False):

        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.tank_write = tank_write
        self.stocke_write = stocke_write

        threading.Thread.__init__(self)

    ############################################################################
    def run(self):

        global global_tank
        global global_stocke_1
        global global_stocke_2

        while (not stop_thread):

            print(self.name + " : Starting task")

            if (self.tank_write == True):

                global_tank.append(self.name + " : getting the Oil: " + datetime.datetime.now().strftime("%H:%M:%S"))

            else:
                while (len(global_tank) > 0):
                    print(self.name + " : " + global_tank[0])
                    del global_tank[0]


            # Implementation: Machines & stock
            if (self.stocke_write == True):

                global_stocke_1.append(self.name + " : add the oil of machine_1 into the stock 1: " + datetime.datetime.now().strftime("%H:%M:%S"))
                print(global_stocke_1)

                global_stocke_2.append(self.name + " : add the oil of machine_2 into the stock 2: " + datetime.datetime.now().strftime("%H:%M:%S"))
                print(global_stocke_2)


            time.sleep(self.execution_time)
            print(self.name + " : Stopping task")
            time.sleep(self.period - self.execution_time)


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    task_list = []

    # Instanciation of task objects

    task_list.append(my_task(name="pump_1", period=5, execution_time=2, tank_write=True))
    task_list.append(my_task(name="pump_2", period=15, execution_time=3, tank_write=True))
    task_list.append(my_task(name="machine_1", period=5, execution_time=3, stocke_write=True))
    task_list.append(my_task(name="machine_2", period=5, execution_time=5, stocke_write=True))

    for current_task in task_list:
        current_task.start()










