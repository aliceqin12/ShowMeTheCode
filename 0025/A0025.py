import wave
import json
import pyaudio
import base64
import requests
import webbrowser
from record import record_wave

APP_ID = '10117231'
API_KEY = 'qNdkGGqEtGd3jLXePVArnrPk'
SECRET_KEY = 'eyHwvBwbWS8r1OHbGzlQ5ppoazzTLB0Y'

proxies = {
"http": "web-proxy.oa.com:8080",
  "https": "web-proxy.oa.com:8080",
}

def get_file_content(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def get_access_token():
    url = 'https://openapi.baidu.com/oauth/2.0/token'
    data = {'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': SECRET_KEY}
    r = requests.post(url, data=data, proxies=proxies)
    text = json.loads(r.text)
    return text['access_token']

def speech2Text(filepath, format, rate, channel, cuid, token):
    file_content = get_file_content(filepath)
    speech = base64.b64encode(file_content).decode()
    file_len = len(file_content)

    url = 'http://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    data = {
        'format': format,
        'rate': rate,
        'channel': channel,
        'token': access_token,
        'lan': 'zh',
        'cuid': 'aoyunzhang',
        'len': file_len,
        'speech': speech
    }

    r = requests.post(url=url, json=data, headers=headers, proxies=proxies)
    result_json = json.loads(r.text)
    print(result_json)
    err_msg = result_json['err_msg']
    result = ''
    if err_msg == 'success.':
        result = result_json['result'][0]

    return err_msg, result

if __name__ == '__main__':
    wave_file_name = 'record.wav'
    # record_wave(wave_file_name)
    access_token = get_access_token()
    err_msg, result = speech2Text(wave_file_name, 'wav', 8000, 1, 'aoyunzhang', access_token)
    if err_msg == 'success.':
        if 'baidu' in result:
            webbrowser.open_new('www.baidu.com')