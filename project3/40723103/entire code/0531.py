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

        
    
    def getposition(self,step):
        sim.simxSynchronousTrigger(self.clientID)
        sim.simxGetPingTime(self.clientID)
        deg = math.pi/180
        for i in range(step):
            res,joint1 = sim.simxGetObjectHandle(self.clientID, "Revoluure_joint6",  sim.simx_opmode_oneshot_wait)
            res,position = sim.simxGetJointPosition(self.clientID,joint1,sim.simx_opmode_streaming)
            ping_s,number = sim.simxGetPingTime(self.clientID)
            print(position,ping_s)
   
    def setrunningtime(self,number):
        sim.simxSynchronousTrigger(self.clientID)
        sim.simxGetPingTime(self.clientID)
        res,main_time = sim.simxGetFloatingParameter(self.clientID,number,sim.simx_opmode_oneshot_wait)
        sim.simxFinish(self.clientID)
        print('setting time')
        
      
    def velocity(self,max1,mag):
        res,joint0 = sim.simxGetObjectHandle(self.clientID, "Revoluure_joint6",  sim.simx_opmode_oneshot_wait)#定義物件名稱
        sim.simxSynchronousTrigger(self.clientID)#模擬同步化確認
        left_Code =sim.simxSetJointTargetVelocity(self.clientID,joint0 ,max1,sim.simx_opmode_oneshot_wait)#目標速度設定
        sim.simxSetIntegerParameter(self.clientID,sim.sim_intparam_speedmodifier,mag , sim.simx_opmode_oneshot_wait) #(調整速度倍率)
        print('finish velocity setting')
        
                 

    def settime(A):
         if max1>0 :
             A=sim.getSimulationTime()+3 

    def finishcoderunning(self): 
            sim.simxSynchronousTrigger(self.clientID)
            sim.simxStopSimulation(self.clientID, sim.simx_opmode_oneshot)
            #sim.simxFinish(self.clientID)
            print("finish code")
        
        
#call code section!!!!!

connected = ConnectedremoteAPI( )#類別取名(較好整理)
connected. connectedAPI()#連接coppeliasim服務端
connected.simulation()#啟動模擬
connected.getposition(2)#抓取物體位置
connected.settime= time.sleep(2)#延長開始模擬時間
connected.velocity(-6,1)#速度:倍率
connected.setrunningtime(5000)#設定模擬時間
connected.finishcoderunning()#停止模擬

print('finish entire code')