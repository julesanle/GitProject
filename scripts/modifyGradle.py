import sys
import os

baseLine = "apply plugin: 'com.android.application'\n"
jacocoLine = "apply plugin: 'jacoco'"


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
        }'''


buildTypes = '''
buildTypes {
        debug {
        
            buildConfigField "boolean", "LOG_DEBUG", "true"
            testCoverageEnabled true
            minifyEnabled false
            zipAlignEnabled true
            shrinkResources false
            signingConfig signingConfigs.debug
        }
            release {
            
            signingConfig signingConfigs.release


                        }


        }'''


productFlavor = '''
productFlavors {
yanxiu_com{
 manifestPlaceholders = [INSTALL_CHANNEL_VALUE: "yanxiu_com"]
}
}
'''

jacocoTestReport = '''
def coverageSourceDirs = [
        '../app/src/main/java'
]

task jacocoTestReport(type: JacocoReport) {
    group = "Reporting"
    description = "Generate Jacoco coverage reports after running tests."
    reports {
        xml.enabled = true
        html.enabled = true
    }
    classDirectories = fileTree(
            dir: './build/intermediates/classes/yanxiu_com/debug',
            excludes: ['**/R*.class',
                       '**/*$InjectAdapter.class',
                       '**/*$ModuleAdapter.class',
                       '**/*$ViewInjector*.class'
            ])
    sourceDirectories = files(coverageSourceDirs)
    executionData = files("$buildDir/outputs/code-coverage/connected/flavors/coverage.ec")

    doFirst {
        new File("$buildDir/intermediates/classes/yanxiu_com/").eachFileRecurse { file ->
            if (file.name.contains('$$')) {
                file.renameTo(file.path.replace('$$', '$'))
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


def getDependencies(gradleFile):
    dependencies = "dependencies {"
    return getPartFromGradle(gradleFile, dependencies)


def getDefaultConfig(gradleFile):
    defaultConfig = "defaultConfig {"
    return getPartFromGradle(gradleFile, defaultConfig)

def getBuildToolConfig(gradleFile):
    results = ""
    with open(gradleFile,'r') as file:
        contents = file.readlines()
        for line in contents:
            if line.strip().startswith("compileSdkVersion") or line.strip().startswith("buildToolsVersion"):
                results += line
    return results

def getPartFromGradle(gradleFile, text):
    result = ""
    count = 0
    
    with open(gradleFile, 'r') as file:
        contents = file.readlines()
        i = 0
        i_row = 0
        for line in contents:
            
            if line.strip().startswith(text):
                i_row = i
            
            if (i_row > 0 and not contents[i].strip().find("}")>=0):
                if contents[i].find("{")>=0:
                    count = count + 1
                result = result + contents[i]
            elif (i_row > 0 and contents[i].strip().find("}")>=0):
                
                if count == 1:
                    break
                count = count -1
                result = result + contents[i]
                                
            i = i + 1
    return result + "\n}"


def updatefile(filename):
    
    print filename
    
    with(open(filename,"r")) as file:
        content = file.readlines();
        i=0
        for c in content:
            if(c.startswith("android {")):
                c = c.replace("android {",'android {\nlintOptions {\nabortOnError false\n}\n\
    signingConfigs { \n\
	myConfig{\n\
	storeFile file("yanxiuandroid.keystore")\n\
	storePassword "yanxiusrt1qaz@wsx"\n\
	keyAlias "android.keystore"\n\
	keyPassword "yanxiusrt1qaz@wsx"\n\
	}\n\
}\n\
\
	buildTypes{\n\
	release {\n\
	signingConfig signingConfigs.myConfig\n\
	} \n\
  } \n \
')
                content[i]=c
            i=i+1
        
        fout = open(filename,"w+")
        fout.writelines(content)
    
    
def copyKeyFile():
    filename =  os.path.join(jenkinsHome,"scripts/yanxiuandroid.keystore")
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ os.path.join(workspace,"app")
    print cmd_copy
    print os.popen(cmd_copy).read()
    
if __name__ == '__main__':
    workspace = os.getenv("WORKSPACE")
    jenkinsHome = os.getenv("JENKINS_HOME")
    filename = os.path.join(workspace,"universalvideoview/build.gradle")
    updatefile(filename)
    filename = os.path.join(workspace,"androidlib/build.gradle")
    updatefile(filename)

    filename = os.path.join(workspace,"network/build.gradle")
    updatefile(filename)
    copyKeyFile()
    fielOfBuildGradle = os.getenv("WORKSPACE") + "/app/build.gradle"
    defaultConfig = getDefaultConfig(fielOfBuildGradle)
    print 'default config',defaultConfig
    dependencies = getDependencies(fielOfBuildGradle)
    buildToolConfig = getBuildToolConfig(fielOfBuildGradle)
    buildGradle = [baseLine,jacocoLine, "\nandroid {", buildToolConfig, defaultConfig, lint , dexOption,signingConfig,buildTypes, productFlavor,"\n}\n", dependencies,jacocoTestReport]
                              #buildGradle = [baseLine, "\nandroid {", buildToolConfig, defaultConfig, lint , dexOption,signingConfig,buildTypes, productFlavor,"\n}\n", dependencies,configurationAll]
    print fielOfBuildGradle
    with open(fielOfBuildGradle, "w") as file:
        for item in buildGradle:
            print item
            file.writelines(item)
