import requests

class ExecutorRequest:
    def  get_requset(self):
        pass
    def post_requset(self):
        url = 'https://api.3ren.cn/course-center/media/publish'
        data ={"title":"撒旦法","allowDownload":true,"allowReply":true,"viewInProgress":false,"assetType":"classroom-test","courseId":"4633319631258624000","segmentType":"file","fileTag":"沙发","materialIds":["4498868428836364288"],"parentSegmentId":""}
        header ={'Authorization': 'Basic c2FucmVuLXRlYWNoZXItcGM6MjZlZEV0WmlObTJ3NzZwbFhT',
        'ontent - Type': 'application / json',
        'X - DT - accessToken': '24598c8b - da64 - 4a65 - 945c - 79cbcfd11df1',
        'X - DT - clientId': 'sanren - teacher - pc'}
        res = requests.post(url, headers=header,json=data)
