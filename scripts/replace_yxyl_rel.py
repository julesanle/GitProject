#! /usr/bin/env
#coding=utf-8

#说明: 现在测试良师通的安卓和iOS没有问题,需要确定所要替换的文件路径和文件名  另外,易学易练的路径没有写,用的话,需要写上~~~~


import sys, shutil, os, string

#Jenkins config file
jenkins_path = '/Users/rts/.jenkins/jenkins_config'
workspace = os.getenv("WORKSPACE")


#yxyl config file

#app_path_ios_yxyl = '/Users/rts/.jenkins/workspace/Rxt_IOS_release/YanXiuStudentApp/Common'
app_path_ios_yxyl = os.path.join(workspace,"YanXiuStudentApp/YanXiuStudentApp")
#配置文件名称

#yxyl
#app -config
app_ios_yxyl ='env_config.json'

#jenkins-config
ios_release_yxyl ='config_rel.json'

def copy_file(app_ios_config,ios_release_file,app_file_path):
    if not os.path.exists(app_ios_config):
        shutil.copy(ios_release_file,app_file_path)
    else:
        shutil.copy(ios_release_file,app_ios_config) #新文件，旧文件


def choose_config(app,system,package):
    jenkins_file_path = jenkins_path+'/'+app+'/'+system

    if app =='yxyl':
       if system == 'ios' and package == 'release':
            ios_release_file = jenkins_file_path+'/'+ios_release_yxyl
            app_ios_config = app_path_ios_yxyl+'/'+app_ios_yxyl
            copy_file(app_ios_config, ios_release_file, app_path_ios_yxyl)
if __name__ == '__main__':  #定义主函数

    args = sys.argv
    #get app system package &&translate to lower
    app = args[1].lower()
    system = args[2].lower()
    package = args[3].lower()
    print(system,package)
    choose_config(app,system,package)
