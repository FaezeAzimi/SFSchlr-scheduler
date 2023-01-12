import threading
from time import sleep
import os
import numpy as np

class ContainerWatch(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_name = "ContainerWatch"
        self.thread_ID = 63454
        self.env=np.array([])
    def run(self):
        while True:
            self.update_env()
            sleep(10)

    def update_env(self):
        output = os.popen('docker ps | grep serverless')
        ncon=self.get_containers(output)
        list=[]
        for i in ncon:
            pkgs=self.get_packages(i)
            list.append([i,pkgs,1])
        self.env=np.array(list)
    
    def get_containers(self,container):
        ncon = []
        lines=container.read()
        locs=self.find_all(lines,'serverless')
        for i in locs:
            ncon.append(int(lines[i+10:i+11]))
        ncon.sort()
        return ncon
    
    def find_all(self,lines, sub):
        result = []
        i = 0
        while i < len(lines):
            i = lines.find(sub, i)
            if i == -1:
                return result
            else:
                result.append(i)
                i += 1 
        return result
    
    def get_packages(self,con):
        output = os.popen("docker exec serverless"+str(con)+" pip list --disable-pip-version-check | awk '{ print $1 }'")
        lst=output.read().splitlines()
        del lst[0:2]
        return lst

    def kill_container(con):
        output = os.popen("docker stop serverless"+str(con))
        output = os.popen("docker container prune")
        
    def upgrade_container(con,env):
        output = os.popen("docker stop serverless"+str(con))
        for count,pkg,size in env:
            output = os.popen('docker run -d --name serverless'+str(count)+' --memory='+str(size+1)+'g --cpuset-cpus='+str(size+1)+' '+img_name+':'+self.image_ver)

    def downgrade_container(con,env):
        output = os.popen("docker stop serverless"+str(con))
        for count,pkg,size in env:
            output = os.popen('docker run -d --name serverless'+str(count)+' --memory='+str(size-1)+'g --cpuset-cpus='+str(size-1)+' '+img_name+':'+self.image_ver)

    