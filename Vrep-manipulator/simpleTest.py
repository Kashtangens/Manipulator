import vrep
import sys
import time
import math

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

print(vrep.simxGetObjects(clientID, vrep.sim_handle_all, vrep.simx_opmode_oneshot_wait))

errorCode, angle1=vrep.simxGetObjectHandle(clientID,'LBR4p_joint1',vrep.simx_opmode_blocking)
errorCode, angle2=vrep.simxGetObjectHandle(clientID,'LBR4p_joint2',vrep.simx_opmode_blocking)
errorCode, angle3=vrep.simxGetObjectHandle(clientID,'LBR4p_joint4',vrep.simx_opmode_blocking)
errorCode, angle4=vrep.simxGetObjectHandle(clientID,'LBR4p_joint5',vrep.simx_opmode_blocking)
errorCode, angle5=vrep.simxGetObjectHandle(clientID,'LBR4p_joint6',vrep.simx_opmode_blocking)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()

l = 1.5
p = 0.5
ang = 0
r = 4.5
H = 0.75
while True:
    x = float(input())
    y = float(input())
    z = float(input())
    r = math.sqrt(x*x + y*y + (z-H)*(z-H))
    h = r-p
    if (h <= (2*l)):
        ang = math.acos(h/(2*l))
        d = math.asin(math.sqrt(x*x + y*y)/r)
    vrep.simxSetJointTargetPosition(clientID, angle1, math.atan2(y, x), vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID, angle2, ang-d, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID, angle3, -2*ang, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID, angle4, 0, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID, angle5, ang, vrep.simx_opmode_streaming)
    time.sleep(1)