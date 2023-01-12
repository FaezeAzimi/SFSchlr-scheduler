import os

class Env:
    def __init__(self,environment,dock_file,func_path,img_name):
        self.environment=environment
        self.docker_file=dock_file
        self.image_name=img_name
        self.image_ver="0.1"
        self.build_image(dock_file,img_name)
        self.init_containers(environment,img_name)
    
    def set_image_ver(self,img_ver):
        self.image_ver=img_ver

    def get_dockerfile(self):
        return self.docker_file

    def get_state(self):
        return self.environment

    def build_image(self,dock_file,img_name):
        if self.check_oldimage(img_name) == True :
            output=os.popen('docker build -t '+img_name+':'+self.image_ver+' '+dock_file)
        else:
            self.remove_oldimage(img_name)
            output=os.popen('docker build -t '+img_name+':'+self.image_ver+' '+dock_file)

    def check_oldimage(self,img_name):
        output = os.popen('docker images | grep '+img_name+':'+self.image_ver)
        output = output.read()
        if len(output) != 0:
            return False
        else:
            return True
            
    def remove_oldimage(self,img_name):
        output = os.popen('docker rmi '+ img_name+':'+self.image_ver)

    def init_containers(self,env,img_name):
        for count,pkg,size in env:
            output = os.popen('docker run -d --name serverless'+str(count)+' --memory='+str(size)+'g --cpuset-cpus='+str(size-1)+' '+img_name+':'+self.image_ver)