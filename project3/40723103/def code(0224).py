import math 
import time
import sim 
import simConst

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
print("Connection success")

def connectedAPI():
    if clientID!=-1:
        print ('Connected to remote API server')
    else:
        print('cant not to connnected')
            
    
def simulation() :
    sim.simxSynchronous(clientID,1)
    #同步模式
    sim.simxSynchronousTrigger(clientID)
    # Start simulation
    sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)
    print ("Simulation start")
        
def velocity(max1,max2):
    #res,joint0 = sim.simxGetObjectHandle(clientID, "Revolute_joint0",  sim.simx_opmode_oneshot_wait)
    #res,joint1 = sim.simxGetObjectHandle(clientID, "Revolute_joint1",  sim.simx_opmode_oneshot_wait)
    res,main_handle = sim.simxGetObjectHandle(clientID, 'Cuboid0', sim.simx_opmode_blocking)
    res,joint0 = sim.simxGetObjectHandle(clientID, "left_motor",  sim.simx_opmode_oneshot_wait)
    res,joint1 = sim.simxGetObjectHandle(clientID, "right_motor",  sim.simx_opmode_oneshot_wait)
    sim.simxSynchronousTrigger(clientID)
    
    left_Code =sim.simxSetJointTargetVelocity(clientID,joint0 ,max1,sim.simx_opmode_oneshot_wait)
    right_Code = sim.simxSetJointTargetVelocity(clientID,joint1 ,max2,sim.simx_opmode_oneshot_wait)
    #right_Code = sim.simxSetJointTargetVelocity(clientID,joint1 ,max3,sim.simx_opmode_oneshot_wait)
    print('finish velocity setting')
     

def settime(A):
    #sim.simxGetSimulationTime()
     if max1>0 :
         A=sim.getSimulationTime()+3 

def sleeptime(sec):
    #return hour*3600 + min*60 + sec
    #second = sleeptime(hour,min,sec)
    while 1==1:
        time.sleep(sec)
        print ('finish')
        return sec
#sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot)
#sim.simxFinish(clientID)

#call code section!!!!!


simulation()
velocity(20,20)
sectime=sleeptime(5)
#settime(2)


print('finish entire code')

'''
def main_position()
 res, main_position = sim.simxGetObjectPosition(clientID, main_handle, -1, sim.simx_opmode_blocking)
        if res >= 0:
            print('main_position'  + str(main_position))
        else:
            print('cant found main_position')
'''
        