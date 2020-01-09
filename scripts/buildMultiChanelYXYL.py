import os
import time

#/Users/rts/.jenkins/scripts/packageApks.py
baseLine = "apply plugin: 'com.android.application'"
comonContent = '''
        compileSdkVersion 25
        buildToolsVersion "25.0.0"
'''

signingConfig = '''
        signingConfigs {
        debug {
                   
               }
        
            release{
                storeFile file("android.keystore")
                storePassword "yanxiusrt1qaz@wsx"
                keyAlias "zuoyebaoandroid.keystore"
                keyPassword "yanxiusrt1qaz@wsx"
                }
        }

'''
lint = '''
        lintOptions {
            abortOnError false
            }
dexOptions 
{
jumboMode true
}
'''

buildTypes = '''
buildTypes {
        debug {
            
            buildConfigField "boolean", "LOG_DEBUG", "true"
            versionNameSuffix "-debug"
            minifyEnabled false
            zipAlignEnabled false
            shrinkResources false
            signingConfig signingConfigs.debug
            //
            manifestPlaceholders = [
                GETUI_APP_ID    : "VKUOZXhFCB7GevG6yfQXE1", //APP_ID
                GETUI_APP_KEY   : "xSFRKbsdKmALW38Bvvx0U6",   //APP_KEY
                GETUI_APP_SECRET: "ulxmindW6P7FjCx0xhVSz1",   //APPSECRET
            ]

        }

        release {
            buildConfigField "boolean", "LOG_DEBUG", "false"
                    minifyEnabled false
            zipAlignEnabled true
            shrinkResources false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release
            
            manifestPlaceholders = [
                //realse
                GETUI_APP_ID    : "xy6JNNaUzP66bUOgoTqom", //APP_ID
                GETUI_APP_KEY   : "oMgcaCRKRp8secHbF5zveA",   //APP_KEY
                GETUI_APP_SECRET: "tstl2Ge5Rw76WzOL0vxWz2",   //APPSECRET
            ]


                    applicationVariants.all { variant ->
                        variant.outputs.each { output ->def outputFile= output.outputFile
                            if (outputFile != null && outputFile.name.endsWith('.apk')) {
                               
                                        def fileName="sanrenxing_xuesheng_${versionName}-${variant.productFlavors[0].name}.apk"
                                output.outputFile =new File(outputFile.parent, fileName)
                                }
                            }
                        }
            }
    }
'''
sourceSets ='''
sourceSets {
    main {
        jniLibs.srcDir(['libs'])
            manifest.srcFile 'src/main/AndroidManifest.xml'
            java.srcDirs = ['src/main/java', 'src/main/aidl']
            resources.srcDirs = ['src/main/java', 'src/main/aidl']
            aidl.srcDirs = ['src/main/aidl']
            res.srcDirs = ['src/main/res']
            assets.srcDirs = ['src/main/assets']
    }
}
'''
ext='''
ext {
    permissionsDispatcherVersion = '2.1.2'
}
'''


def updatefile(filename):
    
    print filename
    
    with(open(filename,"r")) as file:
        content = file.readlines();
        i=0
        for c in content:
            if(c.startswith("android {")):
                c = c.replace("android {",'android {\nlintOptions {\nabortOnError false\n}')
                content[i]=c
            i=i+1
        
        fout = open(filename,"w+")
        fout.writelines(content)

def productFlavorConfig(configFile):
    line = ""
    with open(configFile,"rU") as file:
        chanels = file.readlines()
        
        for chanel in chanels:

            line = line + '%s{\n manifestPlaceholders = [INSTALL_CHANNEL_VALUE: "%s"]\n}\n'%(chanel.strip('\r\n') ,chanel.strip('\r\n') )
        #print line
    productFlavor = "productFlavors {\n" + line + "\n}\n"+'''productFlavors.all { flavor ->
      flavor.manifestPlaceholders = [INSTALL_CHANNEL_VALUE: name]
  }
'''
        
    return  productFlavor 
    
def getDependencies(gradleFile):
    dependencies = "dependencies {"
    return getPartFromGradle(gradleFile,dependencies)
 
def getDefaultConfig(gradleFile):
    defaultConfig = "defaultConfig {"
    return getPartFromGradle(gradleFile,defaultConfig)


def getSigningConfig(gradleFile):
    return getPartFromGradle(gradleFile,"signingConfigs")

def getBuildType(gradleFile):
    return getPartFromGradle(gradleFile,"buildTypes")

def getVersionFromGradle(gradle_path):
    print 'find version from build gradle file:',gradle_path
    with open(gradle_path,'r') as f:
        for line in f.readlines():
            if line.find('versionName')>=0:
                versionName = line.strip(' \n').split(' ')[0]
                if versionName != 'versionName':
                    continue
                versionName = line.strip(' \n').split(' ')[1].strip('"')
    return versionName


def getPartFromGradle(gradleFile,text):
    result = ""
    count = 0

    with open(gradleFile, 'r') as file:
        contents = file.readlines()
        i = 0
        i_row = 0
        for line in contents:

            if line.strip().startswith(text):
                i_row = i

            if (i_row > 0 and not contents[i].strip().startswith("}")):
                if contents[i].find("{") >= 0:
                    count = count + 1
                result = result + contents[i]
            elif (i_row > 0 and contents[i].strip().startswith("}")):

                if count == 1:
                    break
                count = count - 1
                result = result + contents[i]

            i = i + 1
    return result + "\n}"

def delBlock(gradleFile,blockName):
    result = ""
    count = 0

    with open(gradleFile, 'r') as file:
        contents = file.readlines()
        i = 0
        i_row = 0
        for line in contents:

            if line.strip().startswith(blockName):
                i_row = i

            if (i_row > 0 and not contents[i].strip().startswith("}")):
                if contents[i].find("{") >= 0:
                    count = count + 1
                result = result + contents[i]
                contents[i]=""
            elif (i_row > 0 and contents[i].strip().startswith("}")):

                if count == 1:
                    contents[i] = ""
                    break
                count = count - 1
                result = result + contents[i]
                contents[i]=""

            i = i + 1

        with open(gradleFile, "w+") as file:
            file.writelines(contents)



#read chanel config from the config file
def getChanelConfig(configFile):
    print "start to get chanel config from the config file"
    global chanels
    with open(configFile,"r") as file:
         chanels = file.readlines()
      
    print "end to get chanel config from the config file"
    
    
# modify the android main manifest, add the chanel into it
def modifyManifest(manifestFile):
    matchText = "</application>"
   
   


    str = '<meta-data android:name="UMENG_CHANNEL" android:value="${INSTALL_CHANNEL_VALUE}"/>\n'
                   

                  
    replaceText = str+matchText           
    #print chanelContent
    modifyFile(manifestFile,matchText,replaceText)            
   
        
def modifyGradle(gradleFile):
    matchText = "android {"
    replaceText = matchText+' \n lintOptions {\n\
        abortOnError false\n\
    }\n\
    dexOptions {\n\
        incremental true\n\
    }\n\
    signingConfigs {\n\
	 release{\n\
		storeFile file("android.keystore")\n\
		storePassword "yanxiusrt1qaz@wsx"\n\
		keyAlias "zuoyebaoandroid.keystore"\n\
		keyPassword "yanxiusrt1qaz@wsx"\n\
		}\n\
}\n'
    modifyFile(gradleFile,matchText,replaceText)
    matchText = "release {"
    replaceText = matchText + '\n buildConfigField "boolean", "LOG_DEBUG", "false"\n\
    zipAlignEnabled true\n\
    shrinkResources false\n\
    signingConfig signingConfigs.release\n\
    applicationVariants.all { variant ->\n\
     variant.outputs.each { output ->\n\
    def outputFile = output.outputFile\n\
    if (outputFile != null && outputFile.name.endsWith(\'.apk\')) {\n\
    def fileName = "YXTrain_Android_v${defaultConfig.versionName}_${releaseTime()}_${variant.productFlavors[0].name}.apk"\n\
    output.outputFile = new File(outputFile.parent, fileName)\n\
    }\n\
    }\n\
    }\n\
    '
    modifyFile(gradleFile,matchText,replaceText)
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
            #print content
        
            with open(filename,"w+") as file:
                file.writelines(content)
            print "end to modify file:"+filename



def copyKeyFile():
    jenkinsHome = os.getenv("JENKINS_HOME")
    workspace = os.getenv("WORKSPACE")
    filename =  os.path.join(jenkinsHome,"scripts/android.keystore")
    print "-----------------"+workspace
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ os.path.join(workspace,"/Users/rts/.jenkins/workspace/Rxt_Android_release/phone/app")
    print cmd_copy
    print os.popen(cmd_copy).read()


if __name__ == '__main__':
                                                       #    nowTime=time.strftime('%Y%m%d')
    workspace = os.getenv("WORKSPACE")
    gradle_path = os.getenv("WORKSPACE") + '/phone/app/build.gradle'
    versionName =getVersionFromGradle(gradle_path)

    fileOfChanelConfig = os.getenv("JENKINS_HOME")+"/scripts/chanelConfig"
    fileofManifest = os.getenv("WORKSPACE")+"/phone/app/src/main/AndroidManifest.xml"
    fielOfBuildGradle = os.getenv("WORKSPACE")+"/phone/app/build.gradle"
    updatefile(fielOfBuildGradle)
    delBlock(fielOfBuildGradle,'signingConfigs')
    delBlock(fielOfBuildGradle,'buildTypes')
    productFlavor = productFlavorConfig(fileOfChanelConfig)
    # signingconfig should be before buildTypes
    print 'buildTypes is ',buildTypes
    modifyFile(fielOfBuildGradle, 'defaultConfig {', 'defaultConfig {\n' + signingConfig +'\n' +buildTypes +'\n'+ productFlavor)


    '''
    defaultConfig = getDefaultConfig(fielOfBuildGradle)
    print defaultConfig
    productFlavor = productFlavorConfig(fileOfChanelConfig)
    print productFlavor
    dependencies = getDependencies(fielOfBuildGradle)
    #print dependencies
    print dependencies
    '''
    filename = os.path.join(workspace,"phone/libs/EXueELianRefreshLibrary/build.gradle")
    updatefile(filename)
    filename = os.path.join(workspace,"phone/libs/EXueELianNetwork/build.gradle")
    updatefile(filename)
    '''
    buildGradle = [baseLine,"\nandroid {",comonContent,defaultConfig,"}\n",sourceSets,lint,signingConfig,buildTypes,productFlavor,ext,dependencies,"\n}\n","\n}\n"]
    print fielOfBuildGradle
    with open(fielOfBuildGradle,"w") as file:
        for item in buildGradle:
            #print item
            file.writelines(item)
    '''
    copyKeyFile()
                                                       
    filename1 = os.path.join(workspace,"phone/build.gradle")
    matchText1 = "classpath 'com.android.tools.build:gradle:3.0.0'"
    replaceText1 = "classpath 'com.android.tools.build:gradle:2.3.3'"
    modifyFile(filename1,matchText1,replaceText1)
