import numpy as np
import random
import pkgaware as pkga
import pkgmon as mon
from pkgmon import Env as upenv

def random_function_gen(steps):
    for x in range(0,steps):
        funcs.append(random.randint(1,5))

def update_state(state, state2, reward, action, action2):
        predict = Q[state, action]
        target = reward + gamma * Q[state2, action2]
        Q[state, action] = Q[state, action] + alpha * (target - predict)

def choose_action(state,action,abso,objects):
        action=0
        if np.random.uniform(0, 1) < epsilon:
                action = objects.sample(state,action,reward)
        else:
                action = random.choice(Actions)
        return action

def SFSchlr(queue,objects,packages):
        abso=1
        for func in queue:
                t = 0
                st1=objects.get_environment()
                action1 = choose_action(st1,ch_action,abso,pack2)
                while t < max_steps:
                        state2, reward, abso, done = packages.step(action1,st1,func,func_path)
                        action2 = choose_action(state2)
                        st1 = state2
                        action1 = action2
                        t += 1
                        reward += reward
                        if done:
                                break

epsilon = 0.65
max_steps = 100
alpha = 0.6
gamma = 0.7
initial_container=5
inittal_packages=0
Actions=['A1','A2','A3','A4','A5','A6']
queue1=['f4','f1','f2','f3','f2']
reward = 0
ch_action='A1'


Q = np.zeros((initial_container, inittal_packages))

env=np.array([[1,['certifi', 'charset-normalizer', 'docopt', 'idna', 'pip', 'pipreqs', 'requests', 'setuptools', 'urllib3', 'wheel', 'yarg'],1],
               [2,['certifi', 'charset-normalizer', 'docopt', 'idna', 'pip', 'pipreqs', 'requests', 'setuptools', 'urllib3', 'wheel', 'yarg'],1],
               [3,['certifi', 'charset-normalizer', 'docopt', 'idna', 'pip', 'pipreqs', 'requests', 'setuptools', 'urllib3', 'wheel', 'yarg'],1]
] , dtype=object)

docker_file_path="/opt/scheduler/Docker"
docker_image_name="lab/srvless"
docker_image_ver="0.1"
func_path="/opt/scheduler/Functions"




core1=mon.Env(env,docker_file_path,func_path,docker_image_name)
watch=mon.ContainerWatch()
watch.start()
pack1=pkga.FuncEnv()
pack2=pkga.Discrete(600)
SFSchlr(queue1,watch,pack1)
