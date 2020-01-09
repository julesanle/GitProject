# -*- coding: utf-8-*-

import requests
import json

from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

BASEURL = "http://newjira.yanxiu.com"

class Project:
    def __init__(self,projectKey):
        self.projectKey = projectKey
        self.projectUrl = "/rest/api/2/project/" + projectKey
        url = BASEURL + self.projectUrl
        response = json.loads(ApiUtils.doGet(url))

        self.projectId = response["id"]
        #print ("project id is:"+self.projectId)
        componentsList = response["components"]
        versionsList = response["versions"]
        self.components = []
        self.versions = {}
        for c in componentsList:
            self.components.append(c["name"])
        for v in versionsList:
            self.versions[v["id"]] = v["name"]



    def getVersionId(self,versionName):
        for key,value in self.versions.items():
            if value == versionName:
                return key

    def getAllVersions(self):
        url = BASEURL + "/rest/api/2/project/"+self.projectKey
        response = json.loads(ApiUtils.doGet(url))
        return [version["name"] for version in response["versions"]]

    def getTestCycle(self,versionName):
        versionId = self.getVersionId(versionName)
        payload = {'projectId': self.projectId, 'versionId': versionId}
        url = BASEURL + "/rest/zapi/latest/cycle"
        response = json.loads(ApiUtils.doGet(url,params=payload))
        print (response)
        cycleDetail = []
        for key,value in response.items():
            print (key,value)
            if key == "recordsCount" or key == "-1":
                continue
            cycleItem = {}
            cycleName = value["name"]



            startDate = dateFormat(value["startDate"]) if len(value["startDate"])>0 else ""
            endDate = dateFormat(value["endDate"]) if len(value["endDate"]) else ""



            print (cycleName,startDate,endDate)
            cycleId = key
            payload = {'projectId': self.projectId, 'versionId': versionId,"cycleId":cycleId}
            url = BASEURL + "/rest/zapi/latest/execution"
            cycleList = json.loads(ApiUtils.doGet(url,params=payload))
            executions = cycleList["executions"]
            statusCount = {"1":0,"2":0,"3":0,"4":0,"-1":0}

            componentCount = {}
            for component in self.components:
                componentCount[component] = {"1":0,"2":0,"3":0,"4":0,"-1":0,"bug":0}
            for execution in executions:
                statusCount[execution["executionStatus"]] += 1
                componentCount[execution["component"]][execution["executionStatus"]] += 1
                componentCount[execution["component"]]["bug"] += execution["totalDefectCount"]
            print (statusCount)
            print (componentCount)

            cycleItem["cyclename"] = cycleName
            cycleItem["startdate"] = startDate
            cycleItem["enddate"] = endDate

            cycleItem["execution"] = componentCount
            cycleDetail.append(cycleItem)
        cycleDetail.sort(key=lambda x:x["startdate"])

        return cycleDetail

class ApiUtils:
    headers = {"Content-Type": "application/json", "Authorization": "Basic d2FuZ3hpYW9jdWk6d2FuZ3hpYW9jdWk=",
               "Connection": "close"}
    @staticmethod
    def doPost(self):
        pass
    @staticmethod
    def doGet(url,params=None):
        return requests.get(url,params,headers = ApiUtils.headers ).text

def dateFormat(jiradate):
    (day,month,year) = jiradate.split("/")

    monthMap = {u"一月":"01",u"二月":"02",u"三月":"03",u"四月":"04",u"五月":"05",u"六月":"06",u"七月":"07",u"八月":"08",u"九月":"09",u"十月":"10",u"十一月":"11",u"十二月":"12"}
    temp = "20"+year+"/"+monthMap[month]+"/"+day

    return datetime.strptime(temp, "%Y/%m/%d")

def getVersions(projectKey):
    url = BASEURL + "/rest/api/2/project/" + projectKey
    response = json.loads(ApiUtils.doGet(url))
    versions = ""
    for version in response["versions"]:
        #ssprint version
        if version["name"]!=u"已删除":
            versions+=version["name"]+"\n"

    return versions

if __name__ =='__main__':
    projectKey = "TCLST"


    project = Project(projectKey)

    if len(sys.argv) == 2:
        projectKey = sys.argv[1]
    print getVersions(projectKey)
  
