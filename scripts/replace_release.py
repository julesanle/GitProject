#! /usr/bin/env
#coding=utf-8

#说明: only package release-pack


import sys, shutil, os, string

#Jenkins config file
jenkins_path = '/Users/rts/.jenkins/jenkins_config'
workspace = os.getenv("WORKSPACE")

#lst config file
app_path = os.path.join(workspace,"app/src/main/assets")
app_path_ios_liang =os.path.join(workspace,"TrainApp/Common")

#yxyl config file
#app_path_yxyl =os.path.join(workspace,"phone/MainApp/src/main/assets")
#app_path_ios_yxyl =os.path.join(workspace,"YanXiuStudentApp/Common")

#new yxyl config file
app_path_yxyl =os.path.join(workspace,"phone/app/src/main/assets")
app_path_ios_yxyl =os.path.join(workspace,"YanXiuStudentApp/Common")

#sanke config file
app_path_sanke =app_path
app_path_ios_sanke =os.path.join(workspace,"SanKeApp/Common")

#配置文件名称
#lst
#app -config
app_ios_lst ='env_config.json'
app_android_lst ='env_config.json'
#jenkins-config
ios_release_lst ='config_rel.json'
android_release_lst = 'config_rel.json'

#yxyl
#app -config
app_ios_yxyl ='env_config.json'
app_android_yxyl ='env_config.json'
#jenkins-config
ios_release_yxyl ='config_rel.json'
android_release_yxyl = 'config_rel.json'

#sanke
#app -config
app_ios_sanke ='env_config.json'
app_android_sanke ='config.json'
#jenkins-config
ios_test_sanke = 'config_test.json'
ios_release_sanke ='config_rel.json'
android_test_sanke ='config_test.json'
android_release_sanke = 'config_rel.json'


def copy_file(app_ios_config,ios_release_file,app_file_path):
    if not os.path.exists(app_ios_config):
        shutil.copy(ios_release_file,app_file_path)
    else:
        shutil.copy(ios_release_file,app_ios_config) #新文件，旧文件


def choose_config(app,system,package):
    jenkins_file_path = jenkins_path+'/'+app+'/'+system

    if app =='lst':
        if system == 'ios' and package == 'release':
            ios_release_file = jenkins_file_path+'/'+ios_release_lst
            app_ios_config = app_path_ios_liang+'/'+app_ios_lst
            copy_file(app_ios_config, ios_release_file, app_path_ios_liang)
            #shutil.copy(ios_release_file,app_ios_config)
        elif system == 'android' and package == 'release':
            android_release_file = jenkins_file_path+'/'+android_release_lst
            app_android_config = app_path+'/'+app_android_lst
            copy_file(app_android_config, android_release_file, app_path)
            #shutil.copy(android_release_file,app_android_config)
    elif app =='yxyl':
        if system == 'ios' and package == 'release':
            ios_release_file = jenkins_file_path+'/'+ios_release_yxyl
            app_ios_config = app_path_ios_yxyl+'/'+app_ios_yxyl
            copy_file(app_ios_config, ios_release_file, app_path_ios_yxyl)
            #shutil.copy(ios_release_file,app_ios_config)
        elif system == 'android' and package == 'release':
            android_release_file = jenkins_file_path+'/'+android_release_yxyl
            app_android_config = app_path_yxyl+'/'+app_android_yxyl
            copy_file(app_android_config, android_release_file, app_path_yxyl)
            #shutil.copy(android_release_file,app_android_config)

    elif app =='sanke':
        if system == 'ios' and package == 'test':
            ios_test_file = jenkins_file_path+'/'+ios_test_sanke
            app_ios_config = app_path_ios_sanke+'/'+app_ios_sanke
            copy_file(app_ios_config, ios_test_file, app_path_ios_sanke)
        #shutil.copy(ios_test_file,app_ios_config) #新文件，旧文件
        elif system == 'ios' and package == 'release':
            ios_release_file = jenkins_file_path+'/'+ios_release_sanke
            app_ios_config = app_path_ios_sanke+'/'+app_ios_sanke
            copy_file(app_ios_config, ios_release_file, app_path_ios_sanke)
    #shutil.copy(ios_release_file,app_ios_config)
        elif system == 'android'and package == 'test':
            android_test_file = jenkins_file_path+'/'+android_test_sanke
            app_android_config = app_path_sanke + '/'+app_android_sanke
            copy_file(app_android_config, android_test_file, app_path)
        #shutil.copy(android_test_file,app_android_config)
        elif system == 'android' and package == 'release':
            android_release_file = jenkins_file_path+'/'+android_release_sanke
            app_android_config = app_path_sanke+'/'+app_android_sanke
            copy_file(app_android_config, android_release_file, app_path)
#shutil.copy(android_release_file,app_android_config)

if __name__ == '__main__':  #定义主函数

    args = sys.argv
    #get app system package &&translate to lower
    app = args[1].lower()
    system = args[2].lower()
    package = args[3].lower()
    print(system,package)
    choose_config(app,system,package)
