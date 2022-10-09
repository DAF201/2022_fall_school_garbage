import requests
import base64
import json


# 读取文件
def open_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data


# 将文件转换为base64编码，上传文件必须将文件以base64格式上传
def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    print(data_b64)
    return data_b64


# 上传文件
def upload_file(file_data):
    print(file_data)
    file_name = "test.txt"  # 文件名
    token = "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"
    # 用户名、库名、路径
    url = "https://api.github.com/repos/daf201/image_bed/contents/"+file_name
    headers = {"Authorization": "token " + token}
    content = file_base64(file_data)
    data = {
        "message": "message",
        "committer": {
            "name": "daf201",
            "email": "1641853573@qq.com"
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers).text
    print(req)
    # print(re_data['content']['sha'])
    # print("https://cdn.jsdelivr.net/gh/[user]/[repo]/[path]"+file_name)
# 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':
    fdata = open_file('./test.txt')
    print(fdata)
    upload_file(fdata)
