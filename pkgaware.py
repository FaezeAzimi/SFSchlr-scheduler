import numpy as np
import os
import random as _random
import process as pros
import datetime
import time

class Discrete():
    def __init__(self, n):
        assert n >= 0
        self.n = n
        super(Discrete, self).__init__((), np.int64)

    def sample(state,action,abso):
        Actions=['A1','A2','A3','A4','A5','A6']
        container_id=[i[0] for i in state]
        if abso == 1:
           action1 = action
        elif abso == 1:
           Actions1=[i for i in Actions if action not in i]
           action1 =_random.choice(Actions1)
        return action1

    def contains(self, x):
        if isinstance(x, int):
            as_int = x
        elif isinstance(x, (np.generic, np.ndarray)) and (x.dtype.char in np.typecodes['AllInteger'] and x.shape == ()):
            as_int = int(x)
        else:
            return False
        return as_int >= 0 and as_int < self.n

class Space(object):

    def __init__(self, shape=None, dtype=None):
        self.shape = None if shape is None else tuple(shape)
        self.dtype = None if dtype is None else np.dtype(dtype)
        self.np_random = None
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    def create_seed(a=None, max_bytes=8):
        if a is None:
            a = _bigint_from_bytes(os.urandom(max_bytes))
        elif isinstance(a, str):
            a = _bigint_from_bytes(a[:max_bytes])
        elif isinstance(a, integer_types):
            a = a % 2**(8 * max_bytes)
        else:
            raise error.Error('This is not a valid seed: {} ({})'.format(type(a), a))
        return a

    def contains(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        return self.contains(x)

class FuncEnv():
    def reset(self):
        pass
    def step(self,action,state,func,func_path):
        log_loc="/opt/scheduler/Log/time_output.log"
        observation, reward, done, info = self.env.step(action)
        container_id=[i[0] for i in state]
        if action == 'A1':
            containerid =_random.choice(container_id)
            list1=(os.popen('docker exec '+containerid+' pip list'))
            v1=datetime.datetime.now()
            os.popen('docker cp '+func_path+'/. '+containerid+':/opt')
            os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
            v2=datetime.datetime.now()
            v = v2 - v1
            elasped=v.microseconds
            cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
            list2=(os.system(cmd))
            sim = self.percentage_sim(list1, list2)
            reward,abso=self.compute_reward(sim)
            output=str(func)+str(elasped)
            with open(log_loc, "a") as myfile:
                myfile.write("output")
        elif action == 'A2':
            for ci in container_id:
                list1=(os.popen('docker exec '+containerid+' pip list'))
                cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
                list2=(os.system(cmd))
                sim = self.percentage_sim(list1, list2)
                if sim > 0.6:
                    containerid=ci
                else:
                    containerid =_random.choice(container_id)
                v1=datetime.datetime.now()
                os.popen('docker cp '+func_path+'/. '+containerid+':/opt')
                os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
                v2=datetime.datetime.now()
                v = v2 - v1
                elasped=v.microseconds
                reward,abso=self.compute_reward(sim)
                output=str(func)+str(elasped)
                with open(log_loc, "a") as myfile:
                    myfile.write("output")
        elif action == 'A3':
            for ci in container_id:
                list1=(os.popen('docker exec '+containerid+' pip list'))
                cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
                list2=(os.system(cmd))
                sim = self.percentage_sim(list1, list2)
                if sim > 0.6:
                    containerid=ci
                    satu=os.popen('docker exec '+containerid+' free -g | awk NR==2{print $7}')
                    if satu > 80 :
                        time.sleep(5) 
                    else:
                        containerid =_random.choice(container_id)
                    v1=datetime.datetime.now()
                    os.popen('docker cp '+func_path+'/. '+containerid+':/opt')
                    os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
                    v2=datetime.datetime.now()
                    v = v2 - v1
                    elasped=v.microseconds
                    reward,abso=self.compute_reward(sim)
                    output=str(func)+str(elasped)
                    with open(log_loc, "a") as myfile:
                        myfile.write("output")
        elif action == 'A4':
            containerid =_random.choice(container_id)
            satu=os.popen('docker exec '+containerid+' free -g | awk NR==2{print $7}')
            if satu > 80:
                image_ver=1
                os.popen('docker commit '+containerid+" "+func+':'+image_ver) 
                containerid=os.popen('docker build -t '+func+':'+image_ver+' /opt/scheduler/Docker')
            else:
                containerid =_random.choice(container_id)
            list1=(os.popen('docker exec '+containerid+' pip list'))
            v1=datetime.datetime.now()
            os.popen('docker cp '+func_path+'/. '+containerid+':/opt')
            os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
            v2=datetime.datetime.now()
            v = v2 - v1
            elasped=v.microseconds
            cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
            list2=(os.system(cmd))
            sim = self.percentage_sim(list1, list2)
            reward,abso=self.compute_reward(sim)
            output=str(func)+str(elasped)
            with open(log_loc, "a") as myfile:
                myfile.write("output")
        elif action == 'A5':
            for ci in container_id:
                list1=(os.popen('docker exec '+containerid+' pip list'))
                cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
                list2=(os.system(cmd))
                sim = self.percentage_sim(list1, list2)
                if sim > 0.6:
                    containerid=ci
                    satu=os.popen('docker exec '+containerid+' free -g | awk NR==2{print $7}')
                    if satu > 80:
                        image_ver1=1
                        os.popen('docker commit '+containerid+" "+func+':'+image_ver1) 
                        containerid=os.popen('docker build -t '+func+':'+image_ver1+' /opt/scheduler/Docker')
                    else:
                        containerid =_random.choice(container_id)
                v1=datetime.datetime.now()
                os.popen('docker cp /opt/scheduler/Functions/. '+containerid+':/opt')
                os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
                v2=datetime.datetime.now()
                v = v2 - v1
                elasped=v.microseconds
                reward,abso=self.compute_reward(sim)
                output=str(func)+str(elasped)
                with open(log_loc, "a") as myfile:
                    myfile.write("output")
        elif action == 'A6':
            image_ver2=0
            containerid=os.popen('docker build -t '+func+':'+image_ver2+' /opt/scheduler/Docker')
            list1=(os.popen('docker exec '+containerid+' pip list'))
            v1=datetime.datetime.now()
            os.popen('docker cp '+func_path+'/. '+containerid+':/opt')
            os.popen('docker exec '+containerid+' python /opt/'+func+'/'+func+'.py')
            v2=datetime.datetime.now()
            v = v2 - v1
            elasped=v.microseconds
            cmd = "cat "+func_path+"/{0}/requirements.txt | awk -F'==' '{print $1}'".format(func)
            list2=(os.system(cmd))
            sim = self.percentage_sim(list1, list2)
            rewar=self.compute_reward(sim)
            output=str(func)+str(elasped)
            image_ver2=image_ver2+1
            with open(log_loc, "a") as myfile:
                myfile.write("output")
            self.frames.append(observation)
        return self._get_observation(), reward, abso, done

    def compute_reward(sim,container_id):
        reward=0
        if sim > 60:
            reward += 1.0
            diff=1
        else:
            reward -= 1.0
            diff=0
        if pros.get_cont_info(container_id)['ind'] == True:
            reward += 0.5
            diff=1
        if pros.get_cont_info(container_id)['cnt'] == container_id:
            reward += 0.5
            diff=1
        else:
            reward -= 1.0
            diff=0
        return reward,diff
    
    def percentage_sim(s1, s2):
        assert len(s1)==len(s2), "Lists must have the same shape"
        nb_agreements = 0  # initialize counter to 0
        for idx, value in enumerate(s1):
            if s2[idx] == value:
                nb_agreements += 1      
        percentage_agreement = nb_agreements/len(s1)
        return sim  
