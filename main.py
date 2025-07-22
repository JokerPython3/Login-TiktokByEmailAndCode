import requests,SignerPy,json,secrets,uuid,binascii,os,time,random
url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
cog = secrets.token_hex(6*2+4)
def xor(string):
  return "".join([hex(ord(c) ^ 5)[2:] for c in string])
params={
  "": "",
  "request_tag_from": "h5",
  "fixed_mix_mode": "1",
  "mix_mode": "1",
  "account_param": xor(input("enter email :")),
  "scene": "4",
  "device_platform": "android",
  "os": "android",
  "ssmix": "a",
  '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
  'cdid': str(uuid.uuid4()),
  "channel": "googleplay",
  "aid": "1233",
  "app_name": "musical_ly",
  "version_code": "370805",
  "version_name": "37.8.5",
  "manifest_version_code": "2023708050",
  "update_version_code": "2023708050",
  "ab_version": "37.8.5",
  "resolution": "900*1600",
  "dpi": "300",
  "device_type": "G011A",
  "device_brand": "google",
  "language": "en",
  "os_api": "28",
  "os_version": "9",
  "ac": "wifi",
  "is_pad": "0",
  "current_region": "IQ",
  "app_type": "normal",
  "sys_region": "US",
  "last_install_time": "1752856167",
  "mcc_mnc": "41805",
  "timezone_name": "Asia/Shanghai",
  "residence": "IQ",
  "app_language": "en",
  "carrier_region": "IQ",
  "timezone_offset": "28800",
  "host_abi": "arm64-v8a",
  "locale": "en-GB",
  "ac2": "wifi",
  "uoo": "0",
  "op_region": "IQ",
  "build_number": "37.8.5",
  "region": "GB",
  'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
  'iid': str(random.randint(1, 10**19)),
  'device_id': str(random.randint(1, 10**19)),
  'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
  "support_webview": "1",
  "okhttp_version": "4.2.210.6-tiktok",
  "use_store_region_cookie": "1",
  "app_version":"37.8.5"
}
cookies={
  "store-idc": "alisg",
  "store-country-code": "iq",
  "store-country-code-src": "did",
  "store-country-sign": "MEIEDLeEK_cONptaosCixAQg5kOgozbqp-KCBg0OD5H9lk6kFUsnhLAIjAOEurGB52oEEK1IESIfzZeMzgqLA6denHg",
  "install_id": params["iid"],
  "ttreq": "1$ec4bb57aa77b1b98cdbbadd7bb9005108fed7e94",
  "odin_tt": "609e0b09c64907b11b9888f543fbe43c76e9b497f351a53a96a7030d66a88d66103a858283bd8ed51577848f4173baf707d1492fe813b01e4d8f18d16720bd0d227fb7fff4487f30eddd4f7bcdf80d76",
  "passport_csrf_token": cog,
  "passport_csrf_token_default": cog,
  "msToken": "p4XhlOoh4S7THTMLr_uwS2gs52Fx9s3bd5CFQuQ0xf6Q5AiYlguQKIgj9lQkckJYwAUNq3GGB1N-yXvFyZXUDzKZFnJUVPns8ZUvOgN-qhg=",
  "myCookie": "rap",
  "tt-target-idc": "useast1a"
}
client=requests.session()
client.cookies.update(cookies)
m=SignerPy.sign(params=params,cookie=cookies)

headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub':m['x-ss-stub'],
  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
  'x-tt-pba-enable': "1",
  'x-tt-dm-status': "login=0;ct=1;rt=7",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'x-tt-passport-csrf-token': cog,
  'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'content-type': "application/x-www-form-urlencoded",
  'content-length': m['content-length'],
 
}

response = client.post(url, headers=headers,params=params)

# print(response.text)
passport_ticket=response.json()["data"]["accounts"][0]["passport_ticket"]



url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
params={
  "": "",
  "request_tag_from": "h5",
  "passport_ticket":passport_ticket,
  "device_platform": "android",
  "os": "android",
  "ssmix": "a",
  "_rticket": params["_rticket"],
  "cdid": params["cdid"],
  "channel": "googleplay",
  "aid": "1233",
  "app_name": "musical_ly",
  "version_code": "370805",
  "version_name": "37.8.5",
  "manifest_version_code": "2023708050",
  "update_version_code": "2023708050",
  "ab_version": "37.8.5",
  "resolution": "900*1600",
  "dpi": "300",
  "device_type": "G011A",
  "device_brand": "google",
  "language": "en",
  "os_api": "28",
  "os_version": "9",
  "ac": "wifi",
  "is_pad": "0",
  "current_region": "IQ",
  "app_type": "normal",
  "sys_region": "US",
  "last_install_time": "1752856167",
  "mcc_mnc": "41805",
  "timezone_name": "Asia/Shanghai",
  "residence": "IQ",
  "app_language": "en",
  "carrier_region": "IQ",
  "timezone_offset": "28800",
  "host_abi": "arm64-v8a",
  "locale": "en-GB",
  "ac2": "wifi",
  "uoo": "0",
  "op_region": "IQ",
  "build_number": "37.8.5",
  "region": "GB",
  "ts": params["ts"],
  "iid": params["iid"],
  "device_id": params["device_id"],
  "openudid": params["openudid"],
  "support_webview": "1",
  "okhttp_version": "4.2.210.6-tiktok",
  "use_store_region_cookie": "1",
  "app_version":"37.8.5"
}

m=SignerPy.sign(params=params,cookie=cookies)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
  'x-tt-pba-enable': "1",
  'x-tt-dm-status': "login=0;ct=1;rt=7",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],
  'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'content-type': "application/x-www-form-urlencoded",
  'content-length': m['content-length'],

}

response = client.post(url, headers=headers,params=params)

# print(response.text)
# print(response.headers)
data = response.headers['X-Tt-Verify-Idv-Decision-Conf']
loads = json.loads(data)
# print(loads)
passport_ticket2 = loads["passport_ticket"]
pseudo_id = loads["extra"][0]["pseudo_id"]
# print(passport_ticket2)
# print(pseudo_id)

url = "https://api16-normal-c-alisg.tiktokv.com/passport/aaas/authenticate/"
params={
  "": "",
  "request_tag_from": "h5",
  "challenge_type": "2",
  "fixed_mix_mode": "0",
  "skip_handler": "error_handler",
  "pseudo_id": pseudo_id,
  "mix_mode": "0",
  "passport_ticket": passport_ticket2,
  "action": "3",
  "device_platform": "android",
  "os": "android",
  "ssmix": "a",
  "_rticket": params["_rticket"],
  "cdid": params["cdid"],
  "channel": "googleplay",
  "aid": "1233",
  "app_name": "musical_ly",
  "version_code": "370805",
  "version_name": "37.8.5",
  "manifest_version_code": "2023708050",
  "update_version_code": "2023708050",
  "ab_version": "37.8.5",
  "resolution": "900*1600",
  "dpi": "300",
  "device_type": "G011A",
  "device_brand": "google",
  "language": "en",
  "os_api": "28",
  "os_version": "9",
  "ac": "wifi",
  "is_pad": "0",
  "current_region": "IQ",
  "app_type": "normal",
  "sys_region": "US",
  "last_install_time": "1752856167",
  "mcc_mnc": "41805",
  "timezone_name": "Asia/Shanghai",
  "residence": "IQ",
  "app_language": "en",
  "carrier_region": "IQ",
  "timezone_offset": "28800",
  "host_abi": "arm64-v8a",
  "locale": "en-GB",
  "ac2": "wifi",
  "uoo": "0",
  "op_region": "IQ",
  "build_number": "37.8.5",
  "region": "GB",
  "ts":params["ts"],
  "iid": params["iid"],
  "device_id": params["device_id"],
  "openudid": params["openudid"],
  "support_webview": "1",
  "okhttp_version": "4.2.210.6-tiktok",
  "use_store_region_cookie": "1",
  "app_version":"37.8.5"
}


payload = {
  'mix_mode': "0",
  'pseudo_id': pseudo_id,
  'challenge_type': "2",
  'action': "3",
  'passport_ticket': passport_ticket2,
  'skip_handler': "error_handler",
  'fixed_mix_mode': "0"
}
m=SignerPy.sign(params=params,cookie=cookies,payload=payload)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/idv_core/verification",
  'x-tt-pba-enable': "1",
  'x-tt-dm-status': "login=0;ct=1;rt=7",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],
  'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],

}

response = client.post(url, data=payload, headers=headers,params=params)

# print(response.text)
# print(response.headers)

#########################
code = input("enter code:")


url = "https://api16-normal-c-alisg.tiktokv.com/passport/aaas/authenticate/"
params = {
    "request_tag_from": "h5",
    "challenge_type": "2",
    "fixed_mix_mode": "1",
    "code": xor(code),
    "skip_handler": "error_handler",
    "pseudo_id": pseudo_id,
    "mix_mode": "1",
    "passport_ticket": passport_ticket2,
    "action": "4",
    "iid":params["iid"],
    "device_id": params["device_id"],
    "ac": "WIFI",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "device_platform": "android",
    "os": "android",
    "ab_version": "37.8.5",
    "ssmix": "a",
    "device_type":params["device_type"],
    "device_brand": params["device_brand"],
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "openudid": params["openudid"],
    "manifest_version_code": "2023708050",
    "resolution": "1600*900",
    "dpi": "240",
    "update_version_code": "2023708050",
    "_rticket": params["_rticket"],
    "is_pad": "0",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "466",
    "app_language": "en",
    "carrier_region": params["carrier_region"],
    "ac2": "wifi",
    "uoo": "0",
    "op_region":  params["carrier_region"],
    "timezone_offset": "10800",
    "build_number": "37.8.5",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "region": "GB",
    "ts": params["ts"],
    "cdid": params["cdid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5"
}


payload = {
  'mix_mode': "1",
  'code': xor(code),
  'pseudo_id': pseudo_id,
  'challenge_type': "2",
  'action': "4",
  'passport_ticket': passport_ticket2,
  'skip_handler': "error_handler",
  'fixed_mix_mode': "1"
}
m=SignerPy.sign(params=params,cookie=cookies,payload=payload)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_US; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-pba-enable': "1",
  'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
  'tt-ticket-guard-iteration-version': "0",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'sdk-version': "2",
  'x-tt-dm-status': "login=0;ct=1;rt=6",
  'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],
  'passport-sdk-version': "6031990",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  
}

response = client.post(url, data=payload, headers=headers,params=params)

# print(response.text)
# print(response.headers)
#################################33

url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
params = {
    "request_tag_from": "h5",
    "passport_ticket":passport_ticket,
    "iid": params["iid"],
    "device_id": params["device_id"],
    "ac": "WIFI",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "device_platform": "android",
    "os": "android",
    "ab_version": "37.8.5",
    "ssmix": "a",
    "device_type": params["device_type"],
    "device_brand": params["device_brand"],
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "openudid": params["openudid"],
    "manifest_version_code": "2023708050",
    "resolution": "1600*900",
    "dpi": "240",
    "update_version_code": "2023708050",
    "_rticket": params["_rticket"],
    "is_pad": "0",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "466",
    "app_language": "en",
    "carrier_region": "TW",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "TW",
    "timezone_offset": "10800",
    "build_number": "37.8.5",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "region": "GB",
    "ts": params["ts"],
    "cdid": params["cdid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5",
   
}
m=SignerPy.sign(params=params,cookie=cookies)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_US; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-pba-enable': "1",
  'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
  'tt-ticket-guard-iteration-version': "0",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'sdk-version': "2",
  'x-tt-dm-status': "login=0;ct=1;rt=6",
  'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],
  'passport-sdk-version': "6031990",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'content-type': "application/x-www-form-urlencoded",
  'content-length': m['content-length'],
  
}

response = client.post(url, headers=headers,params=params)
# print(response.headers)
# print(response.text)
# print(response.cookies)
try:
  sessionid=response.json()["data"]["session_key"]
  print(f"Sessionid : {sessionid} | username : {response.json()["data"]["username"]}")
except:
  print("error login")
# return "ksj"
# code write : s1 
#response => {
#   "data": {
#     "accounts": [
#       {
#         "username": "******",
#         "avatar_url": "",
#         "passport_ticket": "PPTSGOUGKJQV5FDUD9N4QF22HMHSKJK9VDMDQP",
#         "oauth_login_only": false,
#         "faq_type": 3
#       }
#     ]
#   },
#   "message": "success"
# }

#response => {
#   "data": {
#     "captcha": "",
#     "desc_url": "",
#     "description": "",
#     "error_code": 2135
#   },
#   "message": "error"
# }


#response => {
#   "data": null,
#   "message": "success"
# }

#response => 
# {
#   "data": null,
#   "message": "success"
# }
