import requests
name=input("请输入你的用户名")
passwd=input("请输入密码")
url='http://wrggka.whvcse.edu.cn/api/M_User/Login?username='+name+'&password='+passwd+'&accessKey=1&secretKey=1'
res = requests.get(url)
print(res.text)