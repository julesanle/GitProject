import sys
import os,shutil



def updatefile(filename):
    
    print filename
    
    with(open(filename,"r")) as file:
        content = file.readlines();
        i=0
        for c in content:
            if(c.startswith("android {")):
                c = c.replace("android {",'android {\nlintOptions {\nabortOnError false\n}\ndexOptions {\njumboMode true\n}')
                content[i]=c
            i=i+1
        
        fout = open(filename,"w+")
        fout.writelines(content)

                              
def modifyFile(filename,matchText,replaceText):
    print "start to modify file:" + filename
    with open(filename,'r') as file:
        content = file.readlines()
        i = 0
        for line in content:
                              
            if line.strip().startswith(matchText):
                text = line.replace(matchText,replaceText)
                content[i] = text
                break
            i = i+1
        print content
                              
        with open(filename,"w+") as file:
            file.writelines(content)
        print "end to modify file:"+filename
                              
def copyKeyFile1():
    filename =  os.path.join(jenkinsHome,"EXueELian/android.keystore")
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ os.path.join(workspace,"phone/app")
    print cmd_copy
    print os.popen(cmd_copy).read()

                
def copyKeyFile():
    jenkinsHome = os.getenv("JENKINS_HOME")
    workspace = os.getenv("WORKSPACE")
    filename =  os.path.join(jenkinsHome,"scripts/android.keystore")
    print "-----------------"+workspace
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ os.path.join(workspace,"phone/app")
    print cmd_copy
    print os.popen(cmd_copy).read()
                
if __name__ == '__main__':
    workspace = os.getenv("WORKSPACE")
    jenkinsHome = os.getenv("JENKINS_HOME")
    copyKeyFile()
    filename = os.path.join(workspace,"phone/app/build.gradle")
    updatefile(filename)
    filename1 = os.path.join(workspace,"phone/build.gradle")
    matchText1 = "classpath 'com.android.tools.build:gradle:3.0.0'"
    replaceText1 = "classpath 'com.android.tools.build:gradle:2.3.3'"
    modifyFile(filename1,matchText1,replaceText1)
    filename = os.path.join(workspace,"phone/libs/EXueELianNetwork/build.gradle")
    updatefile(filename)
    filename = os.path.join(workspace,"phone/libs/EXueELianRefreshLibrary/build.gradle")
    updatefile(filename)
    filename = os.path.join(workspace,"phone/app/build.gradle")
    matchText = "signingConfigs {"
    replaceText = '''
        signingConfigs {
            release{
            storeFile file("android.keystore")
            storePassword "yanxiusrt1qaz@wsx"
            keyAlias "zuoyebaoandroid.keystore"
            keyPassword "yanxiusrt1qaz@wsx"
            }
        '''
    modifyFile(filename,matchText,replaceText)
    matchText = "release {"
    replaceText = "release {\n signingConfig signingConfigs.release"
    modifyFile(filename,matchText,replaceText)
  
