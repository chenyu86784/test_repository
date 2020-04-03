print('       ___                        ___ _                                        ')
print('      / __\__  _ __ _ __ ___     / __\ |__   ___ _ __   __ _ _   _ _   _  ___  ')
print('''     / _\/ _ \| '__| '_ ` _ \   / /  | '_ \ / _ \ '_ \ / _` | | | | | | |/ _ \     ''')
print('    / / | (_) | |  | | | | | | / /___| | | |  __/ | | | (_| | |_| | |_| |  __/ ')
print('    \/   \___/|_|  |_| |_| |_| \____/|_| |_|\___|_| |_|\__, |\__, |\__,_|\___| ')
print('                                                       |___/ |___/             ')
import requests

place=input('请输入所在地点，可精确到区县:')
url='https://free-api.heweather.net/s6/weather/forecast?location='+place+'&key=04e8effac2cf46ad9cfddd3e3330ae32'
res=requests.get(url).json()
status=res['HeWeather6'][0]['status']
while status!='ok':
    place = input('输入地点无法找到，请重新输入:')
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + place + '&key=04e8effac2cf46ad9cfddd3e3330ae32'
    res = requests.get(url).json()
    status = res['HeWeather6'][0]['status']
#地区相关
admin_area=res['HeWeather6'][0]['basic']['admin_area']  #获取到的省级
city=res['HeWeather6'][0]['basic']['parent_city'] #获取到的市级
stay=res['HeWeather6'][0]['basic']['location']   #获取到的区县级
update=res['HeWeather6'][0]['update']['loc']   #获取数据的当日时间，精确到分钟
tz=res['HeWeather6'][0]['basic']['tz']  #当地的时区
#温度相关
tmp_max=res['HeWeather6'][0]['daily_forecast'][0]['tmp_max']      #当天最高气温
tmp_max_2=res['HeWeather6'][0]['daily_forecast'][1]['tmp_max']   #第二天最高气温
tmp_max_3=res['HeWeather6'][0]['daily_forecast'][2]['tmp_max']   #第三天最高气温
tmp_min=res['HeWeather6'][0]['daily_forecast'][0]['tmp_min']        #当天最低气温
tmp_m_2=res['HeWeather6'][0]['daily_forecast'][1]['tmp_min']          #第二天最低气温
tmp_min_3=res['HeWeather6'][0]['daily_forecast'][2]['tmp_min']       #第三天最低气温
#天气状况描述
cond_txt_d=res['HeWeather6'][0]['daily_forecast'][0]['cond_txt_d']    #当天日间天气状况描述


pop=res['HeWeather6'][0]['daily_forecast'][0]['pop']    #当天降水概率




print('最近一次获取数据时间为:'+update+'\n您所在的地区为：'+admin_area+'省'+city+'市'+stay+'区（县）'+'\n时区是:东'+tz[1]+'区')
print('今天最高气温为：'+tmp_max+'度'+'\n最低气温为：'+tmp_min+'度')
print('天气状况为：'+cond_txt_d+'\n降水概率为'+pop+'%')

input('输入任意键退出')