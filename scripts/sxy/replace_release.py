#! /usr/bin/env
#coding=utf-8

#说明: only package release-pack


import sys, shutil, os, string

#Jenkins config file
jenkins_path = '/Users/rts/.jenkins/jenkins_config'
workspace = os.getenv("WORKSPACE")

#new sxy config file
app_path=os.path.join(workspace,"app/src/main/assets")

#配置文件名称
#sxy
#app -config
app_android_sxy ='env_config.json'
#jenkins-config
android_release_sxy = 'config_rel.json'


def copy_file(app_android_config,android_release_file,app_path):
    if not os.path.exists(app_android_config):
        shutil.copy(android_release_file,app_path)
    else:
        shutil.copy(android_release_file,app_android_config) #新文件，旧文件


def choose_config(app,system):
    jenkins_file_path = jenkins_path+'/'+app+'/'+system
    if app =='sxy':
        if system == 'android':
            android_release_file = jenkins_file_path+'/'+android_release_sxy
            app_android_config = app_path+'/'+app_android_sxy
            copy_file(app_android_config, android_release_file, app_path)
            #shutil.copy(android_release_file,app_android_config)

if __name__ == '__main__':  #定义主函数

    args = sys.argv
    #get app system package &&translate to lower
    app = args[1].lower()
    system = args[2].lower()
    choose_config(app,system)
