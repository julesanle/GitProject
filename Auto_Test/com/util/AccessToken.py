import requests
import json
def get_access_token():
    api_url = 'https://api-dev.3ren.cn/user-center/teacherRegister/defaultInfo/v2'

    res = requests.get(api_url)
    if res.status_code == 200:
        str_res = res.text
        token = (json.loads(str_res)).get('X-DT-accessToken')
    return token

if __name__ == '__main__':
    print(get_access_token())

