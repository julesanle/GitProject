import os


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
   
    chanelContent = ""
    for chanel in chanels:
        temp = chanel.split(":")
        name = temp[0]
        value = temp[1].strip()

        str = '<meta-data android:name="%s" android:value="%s"/>\n'%(name,value)
                   
        chanelContent = chanelContent + str
                  
    replaceText = chanelContent+matchText           
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
    if (outputFile != null && outputFile.name.endsWith('.apk')) {\n\
    def fileName = "YXTrain_Android_v${defaultConfig.versionName}_${releaseTime()}_${variant.productFlavors[0].name}.apk"\n\
    output.outputFile = new File(outputFile.parent, fileName)\n\
    }\n\
    }\n\
    }\n\
    }\n\
    }\n\
'
    modifyFile(gradleFile,matchText,replaceText)
    print replaceText+"WWWWWWWWWWWWWW"
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
            
    

if __name__ == '__main__':
    fileOfChanelConfig = os.getenv("JENKINS_HOME")+"/scripts/chanelConfig"
    fileofManifest = os.getenv("WORKSPACE")+"/app/src/main/AndroidManifest.xml"
    fielOfBuildGradle = os.getenv("WORKSPACE")+"/app/build.gradle"
    getChanelConfig(fileOfChanelConfig)
    modifyManifest(fileofManifest)
    modifyGradle(fielOfBuildGradle)