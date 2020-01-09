import os


baseLine = "apply plugin: 'com.android.application'"


signingConfig = '''
        signingConfigs {
        debug {
                   
               }
        
            release{
                storeFile file("yanxiuandroid.keystore")
                storePassword "yanxiusrt1qaz@wsx"
                keyAlias "android.keystore"
                keyPassword "yanxiusrt1qaz@wsx"
                }
        }

'''
lint = '''
        lintOptions {
            abortOnError false
            }

'''

dexOption = '''
dexOptions{
jumboMode true
javaMaxHeapSize "4g"
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
        }

        release {
            buildConfigField "boolean", "LOG_DEBUG", "false"
                    minifyEnabled false
            zipAlignEnabled true
            shrinkResources false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release

                    applicationVariants.all { variant ->
                        variant.outputs.each { output ->def outputFile= output.outputFile
                            if (outputFile != null && outputFile.name.endsWith('.apk')) {
                               
                                        def fileName="yx_train_v${variant.productFlavors[0].name}.apk"
                                output.outputFile =new File(outputFile.parent, fileName)
                                }
                            }
                        }
            }
    }
'''

configurationAll = '''
    configurations.all {
    resolutionStrategy.eachDependency { DependencyResolveDetails details ->
    def requested = details.requested
    if (requested.group == 'com.android.support') {
    if (!requested.name.startsWith("multidex")) {
    details.useVersion '25.3.1'
    }
    }
    }
    }
    '''

def productFlavorConfig(configFile):
    line = ""
    with open(configFile,"rU") as file:
        chanels = file.readlines()
        
        for chanel in chanels:
            #only build other chanel, use apktool to finish other chanel
            
            if chanel.find("others")>=0:
                
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

def getBuildToolConfig(gradleFile):
    results = ""
    with open(gradleFile,'r') as file:
        contents = file.readlines()
        for line in contents:
            if line.strip().startswith("compileSdkVersion") or line.strip().startswith("buildToolsVersion"):
                results += line
    return results



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
		storeFile file("yanxiuandroid.keystore")\n\
		storePassword "yanxiusrt1qaz@wsx"\n\
		keyAlias "android.keystore"\n\
		keyPassword "yanxiusrt1qaz@wsx"\n\
		}\n\
}\n\
'
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
    filename =  os.path.join(jenkinsHome,"scripts/yanxiuandroid.keystore")
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ os.path.join(workspace,"app")
    print cmd_copy
    print os.popen(cmd_copy).read()


if __name__ == '__main__':
    fileOfChanelConfig = os.getenv("JENKINS_HOME")+"/scripts/chanelConfig"
    fileofManifest = os.getenv("WORKSPACE")+"/app/src/main/AndroidManifest.xml"
    fielOfBuildGradle = os.getenv("WORKSPACE")+"/app/build.gradle"
    #getChanelConfig(fileOfChanelConfig)
    modifyManifest(fileofManifest)
    #modifyGradle(fielOfBuildGradle)
    filename = os.getenv("WORKSPACE")+"/androidlib/build.gradle"
    modifyFile(filename,"android {","android {"+lint)

    filename = os.getenv("WORKSPACE")+"/network/build.gradle"
    modifyFile(filename,"android {","android {"+lint)

    defaultConfig = getDefaultConfig(fielOfBuildGradle)
    ##print defaultConfig
    productFlavor = productFlavorConfig(fileOfChanelConfig)
    #print productFlavor
    dependencies = getDependencies(fielOfBuildGradle)
    #print dependencies
    #print dependencies
    buildToolConfig = getBuildToolConfig(fielOfBuildGradle)
    buildGradle = [baseLine,"\nandroid {",buildToolConfig,defaultConfig,lint,dexOption,signingConfig,buildTypes,productFlavor,"\n}\n",dependencies,configurationAll]
    print fielOfBuildGradle
    with open(fielOfBuildGradle,"w") as file:
        for item in buildGradle:
            #print item
            file.writelines(item)

    copyKeyFile()
