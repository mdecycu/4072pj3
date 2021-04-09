import math 
import time
import datetime
import sim 
import simConst


class  ConnectedremoteAPI:
    def __init__(self):
        sim.simxFinish(-1)
        self.clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
        print("Connection success")
          
    def connectedAPI(self):
        if self.clientID!=-1:
            print ('Connected to remote API server')
        else:
            print('cant not to connnected')
            
        
    def simulation(self) :
        sim.simxSynchronous(self.clientID,1)
        #同步模式
        sim.simxSynchronousTrigger(self.clientID)
        # Start simulation
        sim.simxStartSimulation(self.clientID, sim.simx_opmode_oneshot_wait)
        print ("Simulation start")
    
    def getposition(self,number):
        res,joint1 = sim.simxGetObjectHandle(self.clientID, "Revolute_joint5",  sim.simx_opmode_oneshot_wait)
        #number returnCode，number position = simxGetJointPosition（number clientID，number jointHandle，number operationMode）
        res,position = sim.simxGetJointPosition(self.clientID,joint1,sim.simx_opmode_streaming)
        ping_s,number = sim.simxGetPingTime(self.clientID)
        print(position,ping_s)
    '''
        #number returnCode，array position = simxGetObjectPosition（number clientID，number objectHandle，number relativeToObjectHandle，number operationMode）
        res,position = sim.simxGetObjectPosition(self.clientID,joint1,-1,sim.simx_opmode_streaming)
        print(position)
    '''
    def setrunningtime(self,number):
        #number returnCode，number paramValue = simxGetFloatingParameter（number clientID，number paramIdentifier，number operationMode）
        #sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier, -1, sim.simx_opmode_oneshot_wait) #(調整速度倍率)
        
        
        res,main_time = sim.simxGetFloatingParameter(self.clientID,50,sim.simx_opmode_oneshot_wait)
        '''
        number returnCode = simxSetIntegerParameter（number clientID，number paramIdentifier，number paramValue，number operationMode）
        # skip every second simulation frame display
        sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier, 2, sim.simx_opmode_oneshot_wait) # skip 3 out of 4 simulation frame display
        sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier, -1, sim.simx_opmode_oneshot_wait) # time step is half of normal time step
        sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier, -2, sim.simx_opmode_oneshot_wait) # time step is 1/4 of normal time step
        
        if (sim_call_type==sim_childscriptcall_initialization) then

        end

        if (sim_call_type==sim_childscriptcall_sensing) then
            local simTime=simGetSimulationTime()
            simSetFloatSignal("mySimulationTime",simTime)
        end
        
        time.sleep(5)
        for n in range(0, 5+1):#測試開始模擬到結束次數比較
            sim.simxStartSimulation(self.clientID, sim.simx_opmode_oneshot)
            ping_s = sim.simxGetPingTime(self.clientID)
            sim.simxStopSimulation(self.clientID, sim.simx_opmode_oneshot)
            ping_p = sim.simxGetPingTime(self.clientID)
            print( "start ping", ping_s)
            print ("stop ping", ping_p)
            print ("n = ", n)
       
        time.sleep(number)
        ping_s = sim.simxGetPingTime(self.clientID)
        print(ping_s)
        #number = sim.simxGetLastCmdTime(self.clientID)#(沒有作用)
        
        #number deltaTimeLeft=sim.wait(number deltaTime,Boolean simulationTime)(Lua的函式，但可通用)
        #settime = sim.wait(self.delatime,3)

        #b=sim.getSystemTimeInMs()#(運行模擬時間)
        #sim.getSimulationTime
        '''       
    def velocity(self,max1,mag):
        #res,joint0 = sim.simxGetObjectHandle(clientID, "Revolute_joint0",  sim.simx_opmode_oneshot_wait)
        #res,joint1 = sim.simxGetObjectHandle(clientID, "Revolute_joint1",  sim.simx_opmode_oneshot_wait)
        res,main_handle = sim.simxGetObjectHandle(self.clientID, 'Revo', sim.simx_opmode_blocking)
        res,joint0 = sim.simxGetObjectHandle(self.clientID, "motor",  sim.simx_opmode_oneshot_wait)
        #res,joint1 = sim.simxGetObjectHandle(self.clientID, "right_motor",  sim.simx_opmode_oneshot_wait)
        sim.simxSynchronousTrigger(self.clientID)
        left_Code =sim.simxSetJointTargetVelocity(self.clientID,joint0 ,max1,sim.simx_opmode_oneshot_wait)
        #right_Code = sim.simxSetJointTargetVelocity(self.clientID,joint1 ,max2,sim.simx_opmode_oneshot_wait)
        #right_Code = sim.simxSetJointTargetVelocity(clientID,joint1 ,max3,sim.simx_opmode_oneshot_wait)
        sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier,mag , sim.simx_opmode_oneshot_wait) #(調整速度倍率)
        number = sim.simxGetLastCmdTime(self.clientID)
        print('finish velocity setting')
         

    def  setjointposition(self,angle,step):
        deg = math.pi/180
        for i in range(step):
            res,joint0 = sim.simxGetObjectHandle(self.clientID, "motor",  sim.simx_opmode_oneshot_wait)
            sim.simxSetJointPosition(self.clientID,joint0,i*angle*deg,sim.simx_opmode_oneshot_wait)
            #print("finish setposition")
        
        sim.simxSetJointPosition(angle,step)

    def settime(A):
        #sim.simxGetSimulationTime()
         if max1>0 :
             A=sim.getSimulationTime()+3 

    def finishcoderunning(self):
            #sec=sim.getSimulationTime()+3 
            sim.simxSynchronousTrigger(self.clientID)
            sim.simxStopSimulation(self.clientID, sim.simx_opmode_oneshot)
            #sim.simxFinish(self.clientID)
            print("finish code")
        
        
#call code section!!!!!

connected = ConnectedremoteAPI( )#類別取名(較好整理)
connected. connectedAPI()#連接coppeliasim服務端
connected.simulation()#啟動模擬
connected.getposition(2200)#抓取物體位置
connected.settime=time.sleep(3)#延長開始模擬時間
connected.velocity(1,0)#速度:倍率
#connected.setrunningtime(5000)
#connected.setjointposition(10,36)#移動連桿件
connected.finishcoderunning()#停止模擬

print('finish entire code')

