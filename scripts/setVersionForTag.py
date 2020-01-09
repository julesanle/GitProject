#! /usr/bin/env
#coding=utf-8

#read the current version number to the version.properties file for tag the version

import zipfile, plistlib, sys, re,os
from biplist import *

def analyze_ipa_with_plistlib(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = readPlistFromString(plist_data)

    print_ipa_info (plist_root)

def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

def print_ipa_info(plist_root):

    print ('Version: %s' % plist_root['CFBundleShortVersionString'])
    version = plist_root['CFBundleShortVersionString']
    with open('version.properties','w') as f:
        f.write('version=v'+version)


def getVersionFromGradle(gradle_path):
    print 'find version from build gradle file:',gradle_path
    with open(gradle_path,'r') as f:
        for line in f.readlines():
            print line
            if line.find('versionName')>=0:
                versionName = line.strip(' \n').split(' ')[0]
                if versionName != 'versionName':
                    continue
                version = line.strip(' \n').split(' ')[1].strip('"')
                print 'version is',version
                with open('version.properties', 'w') as f:
                    f.write('version=' + version)

                break

if __name__ == '__main__':
    workspace = os.getenv("WORKSPACE")
    #workspace = '/Users/rts/.jenkins/workspace/BuildAndroidApkForLiang'
    if len(sys.argv) == 2:
        AppPath = sys.argv[1]
        ipa_path = workspace+'/'+AppPath+'/build/app.ipa'
        if os.path.exists(ipa_path):
            analyze_ipa_with_plistlib(ipa_path)
            sys.exit(0)
    gradle_path = workspace + '/app/build.gradle'
    if os.path.exists(gradle_path):
        getVersionFromGradle(gradle_path)
    else:#for EXEL
        gradle_path = workspace + '/phone/app/build.gradle'
        if os.path.exists(gradle_path):
            getVersionFromGradle(gradle_path)



