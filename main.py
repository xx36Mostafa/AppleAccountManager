import random
import threading
import requests
import json
from faker import Faker
from bs4 import BeautifulSoup
import os , sys
from getmac import get_mac_address as g 
from colorama import Fore,Style,init
from rich import print as printf
from rich.panel import Panel
import configparser
from faker import Faker
import secrets
import string

config = configparser.ConfigParser()
config.read('config.ini')

init(strip=not sys.stdout.isatty())
RESET = Fore.RESET
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MANGETA = Fore.MAGENTA
BLUE =  Fore.BLUE
WORK = 0
BAD = 0
LOCKED = 0
NACTIVE = 0
NOTACTIVE = 0


class apple:
    def __init__(self,index,account):
        self.session = requests.Session()
        self.saccount = account
        self.fake = Faker()

        self.index = index + 1
        if ':' in account:
            account = account.split(":")
        elif ';' in account:
            account = account.split(";")
        elif '\t' in account:
            account = account.strip(" ").split('\t')
        else:
            account = account.split(",")
        try:
            self.email , self.password , self.birthday, self.q1 , self.q2 , self.q3 = account[0:6]
        except:
            self.email , self.password , self.q1 , self.q2 , self.q3 = account[0:5]

    def preparing(self):
        signInURL = "https://appleid.apple.com/sign-in"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36"}
        self.session.headers.update(headers)
        try:
            R0 = self.session.get(signInURL)
            self.aidsp = R0.cookies.get('aidsp')
            URL_Auth = "https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4&skVersion=7&iframeId=auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4&client_id=af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3&redirect_uri=https://appleid.apple.com&response_type=code&response_mode=web_message&state=auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4&authVersion=latest"
            R1 = self.session.get(URL_Auth)
            self.scnt = R1.headers.get('scnt')
            self.aasp = R1.headers.get('aasp')
            self.attributes = R1.headers.get('X-Apple-Auth-Attributes')
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://appleid.apple.com',
                'Pragma': 'no-cache',
                'Referer': 'https://appleid.apple.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":".ta44j1e3NlY5BNlY5BSs5uQ32SCVgecFW16f1ZkQei.uJtHoqvynx9MsFyxY25BcQs1eNk4ugHbSI_Fe2iwAwcMsNUTlWY5BNlYJNNlY5QB4bVNjMk.Bn3"}',
                'X-Apple-I-Request-Context': 'ca',
                'X-Apple-I-TimeZone': 'Africa/Cairo',
                'scnt': self.scnt,
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
            
            json_data = {
                'message': 'sign-in',
                'title': 'ROUTE CHANGED',
                'type': 'INFO',
                'messageMap': {
                    'ACTION': 'FE_INFO',
                },
                'details': '{}',
            }

            logURL_appleid = "https://appleid.apple.com/jslog"
            sendLogRC = self.session.post(logURL_appleid, cookies=self.session.cookies.get_dict(), headers=headers, json=json_data)
            self.aid = sendLogRC.cookies.get('aid')
            
            json_data = {
                'type': 'INFO',
                'title': 'AppleAuthPerf-s-y',
                'message': 'APPLE ID : TTI {"data":{"initApp":{"startTime":2324},"loadAuthComponent":{"startTime":2470},"startAppToTTI":{"duration":146}},"order":["initApp","loadAuthComponent","startAppToTTI"]}',
                'iframeId': 'auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4',
                'details': '{"pageVisibilityState":"visible"}',
            }

            logURL_idmsa = "https://idmsa.apple.com/appleauth/jslog"
            sendLogAAP = self.session.post(logURL_idmsa, headers=headers, json=json_data)
            self.aa = sendLogAAP.cookies.get('aa')
            json_data = {
                'title': 'Hashcash generation',
                'type': 'INFO',
                'message': 'APPLE ID : Performace - 0.029 s',
                'details': '{"pageVisibilityState":"visible"}',
            }
            sendLogHG = self.session.post(logURL_idmsa, cookies=self.session.cookies.get_dict(), headers=headers, json=json_data)
            self.aa = sendLogHG.cookies.get('aa')
            return True
        except Exception as e:
            self.preparing()

    def login(self):
        headers = {
            "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-I-Fd-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"kla44j1e3NlY5BNlY5BSs5uQ32SCVgeYHaJQcuaCSKk6Hb9LarUqUdHz16rgNNlejV9dY.MelqDub9WJ6SubsKEmey855BNlY5CGWY5BOgkLT0XxU..5aC"}',
            "X-Apple-Oauth-Redirect-Uri": "https://appleid.apple.com",
            "Accept-Language": "en-US",
            "X-Apple-Oauth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-Oauth-Client-Type": "firstPartyAuth",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "X-Apple-Auth-Attributes": self.attributes,
            "X-Apple-Oauth-Response-Type": "code",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
            "X-Apple-Oauth-Response-Mode": "web_message",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Apple-Domain-Id": "1",
            "Origin": "https://idmsa.apple.com",
            "Referer": "https://idmsa.apple.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Scnt": self.scnt}
        json_data = {
                "m1":"0KnmfS4OGD0MkSrA+kTcrdHs+dMUlTRzrvbps8yZ4gQ=",
                "c":"d-101-ff403090-7258-11ef-8a51-83dd68c029cf:PRN",
                "m2":"q+ZV/u3wyCx8m+E3IjFpvkUieHEwXGWDoeQUZeoO8R0=",
                'accountName': self.email,
                'rememberMe': False,
                "password": self.password,
            }
        loginURL = "https://idmsa.apple.com/appleauth/auth/signin/complete"
        try:
            sendLogin = self.session.post(loginURL,cookies=self.session.cookies.get_dict(),headers=headers,json=json_data)
            response_data = sendLogin.json()
            if 'serviceErrors' in response_data:
                error_code = response_data['serviceErrors'][0]['code']
                error_message = response_data['serviceErrors'][0]['message']
                if error_code == '-20101':
                    print(f"[{RED}{self.index}/{accounts_len}{RESET}] {RED}Your Apple ID or Password was incorrect.{RESET} [ {RED}{self.email}{RESET} ]")
                    with open(f"{file_name}-wrong.csv",'a+') as f:
                        f.write(f'{self.saccount}\n')
                    return False
                elif error_code == '-20209':
                    print(f"[{RED}{self.index}/{accounts_len}{RESET}] {RED}Apple ID  Locked.{RESET} [ {RED}{self.email}{RESET} ]")
                    with open(f"{file_name}-locked.csv",'a+') as f:
                        f.write(f'{self.saccount}\n')
                    return False
                elif error_code == '-20751':
                    print(f"[{RED}{self.index}/{accounts_len}{RESET}] {RED}Apple ID  NotActive.{RESET} [ {RED}{self.email}{RESET} ]")
                    with open(f"{file_name}-not.csv",'a+') as f:
                        f.write(f'{self.saccount}\n')
                    return False
            else:
                self.scnt = sendLogin.headers.get('scnt')
                self.auth_attributes = sendLogin.headers.get('X-Apple-Auth-Attributes')
                self.aasp = self.session.cookies.get('aasp')
                self.aa = self.session.cookies.get('aa')
                return True
        except:
            self.login()

    def getQuestions(self):
        headers = {
            'Accept': 'text/html',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Pragma': 'no-cache',
            'Referer': 'https://idmsa.apple.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Apple-Domain-Id': '1',
            'X-Apple-Frame-Id': 'auth-70vi3a3g-oxhi-00oq-9y5s-4wu7ywtp',
            'X-Apple-Auth-Attributes':self.auth_attributes,
            'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ32SCVgecJxVeI947Qei.uJtHoqvynx9MsFyxY25CCw0KBN1xL8IidmcK0rTdyLKyLMsZNNlY5BNp55BNlan0Os5Apw.DMu"}',
            'X-Apple-ID-Session-Id': self.aasp,
            'X-Apple-OAuth-Client-Id': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Apple-OAuth-Client-Type': 'firstPartyAuth',
            'X-Apple-OAuth-Redirect-URI': 'https://appleid.apple.com',
            'X-Apple-OAuth-Response-Mode': 'web_message',
            'X-Apple-OAuth-Response-Type': 'code',
            'X-Apple-OAuth-State': 'auth-70vi3a3g-oxhi-00oq-9y5s-4wu7ywtp',
            'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Requested-With': 'XMLHttpRequest',
            'scnt': self.scnt,
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        authIdmsa = "https://idmsa.apple.com/appleauth/auth"
        try:
            getQUS = self.session.get(authIdmsa, cookies=self.session.cookies.get_dict(), headers=headers)
            if getQUS.status_code == 200:
                response_content = getQUS.content
                soup = BeautifulSoup(response_content, 'html.parser')
                script_tag = soup.find('script', class_='boot_args')
                json_content = script_tag.string
                data = json.loads(json_content)
                try:
                    self.questions = data["direct"]["twoSV"]["securityQuestions"]["questions"]
                    return True
                except:
                    trustedPhoneNumbers = data["direct"]["twoSV"]['phoneNumberVerification']['trustedPhoneNumbers']
                    return False
        except:
            self.getQuestions()
        
    def updateFile(self):
        ACCSUPDATE.remove(self.saccount)
        with open(f'{file_name}.csv', 'w') as f:
            for acs in ACCSUPDATE:
                f.write(f'{acs}\n')
        
    def sendAnswers(self):
        if self.questions[0]['id'] in range(130,136):
            v1 = self.q1
        elif self.questions[0]['id'] in range(136,142):
            v1 = self.q2
        elif self.questions[0]['id'] in range(142,148):
            v1 = self.q3

        if self.questions[1]['id'] in range(130,136):
            v2 = self.q1
        elif self.questions[1]['id'] in range(136,142):
            v2 = self.q2
        elif self.questions[1]['id'] in range(142,148):
            v2 = self.q3

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://idmsa.apple.com',
            'Pragma': 'no-cache',
            'Referer': 'https://idmsa.apple.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Apple-App-Id': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Apple-Auth-Attributes': self.auth_attributes,
            'X-Apple-Domain-Id': '1',
            'X-Apple-Frame-Id': 'auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4',
            'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":".ta44j1e3NlY5BNlY5BSs5uQ32SCVgecFdv4_J36LufVD_DJhCizgzH_y3EjNklY9ey.eaB0Tf3drJtJ9VvjJz10yKMjNklY5BNleBBNlYCa1nkBMfs.ACL"}',
            'X-Apple-ID-Session-Id': self.aasp,
            'X-Apple-OAuth-Client-Id': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Apple-OAuth-Client-Type': 'firstPartyAuth',
            'X-Apple-OAuth-Redirect-URI': 'https://appleid.apple.com',
            'X-Apple-OAuth-Response-Mode': 'web_message',
            'X-Apple-OAuth-Response-Type': 'code',
            'X-Apple-OAuth-State': 'auth-9snr64uy-nzj0-853u-xkfj-ovrsnmu4',
            'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'scnt': self.scnt,
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'questions': [
                {
                    'question': self.questions[0]['question'],
                    'answer': v1,
                    'id': self.questions[0]['id'],
                    'number': self.questions[0]['number'],
                },
                {
                    'question': self.questions[1]['question'],
                    'answer': v2,
                    'id': self.questions[1]['id'],
                    'number': self.questions[1]['number'],
                },
            ],
        }
        verifyQURL = "https://idmsa.apple.com/appleauth/auth/verify/questions"
        try:
            sendQuestions = self.session.post(verifyQURL,headers=headers,json=json_data)
            if sendQuestions.status_code==412:
                repair_token = sendQuestions.headers.get('X-Apple-Repair-Session-Token')
                headers = {
                    'Accept': 'application/json;charset=utf-8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    'Origin': 'https://idmsa.apple.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://idmsa.apple.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-GPC': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    'X-Apple-Auth-Attributes': self.auth_attributes,
                    'X-Apple-Domain-Id': '1',
                    'X-Apple-Frame-Id': 'auth-km1opkz7-4rld-51cu-miyj-05sqksom',
                    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ32SCVgecFWHOEMfpurKR0odm_dhrxbuJjkWxv55BPfs1eNk4ugHbSI_Fe2ixAwrKyQfvqBBNlY5BPY25BNnOVgw24uy.0IB"}',
                    'X-Apple-ID-Session-Id': self.aasp,
                    'X-Apple-OAuth-Client-Id': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
                    'X-Apple-OAuth-Client-Type': 'firstPartyAuth',
                    'X-Apple-OAuth-Redirect-URI': 'https://appleid.apple.com',
                    'X-Apple-OAuth-Response-Mode': 'web_message',
                    'X-Apple-OAuth-Response-Type': 'code',
                    'X-Apple-OAuth-State': 'auth-km1opkz7-4rld-51cu-miyj-05sqksom',
                    'X-Apple-Repair-Session-Token': repair_token,
                    'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
                    'X-Requested-With': 'XMLHttpRequest',
                    'scnt': self.scnt,
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                repairURL = "https://idmsa.apple.com/appleauth/auth/repair/complete"
                repairAction = self.session.post(repairURL,headers=headers)

                self.myacinfo = repairAction.cookies.get('myacinfo')
                self.scnt = repairAction.headers.get('scnt')
                self.auth_attributes = repairAction.headers.get('X-Apple-Auth-Attributes')

                headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    'Pragma': 'no-cache',
                    'Referer': 'https://appleid.apple.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-GPC': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ32SCVgecFW2A2p9ffSKk6Hb9LarUqUdHz16rgNNlejV9dY.Mel9SpDK1cDvkjmxMuijjNklY5BNleBBNlYCa1nkBMfs.7wM"}',
                    'X-Apple-I-Request-Context': 'ca',
                    'X-Apple-I-TimeZone': 'Africa/Cairo',
                    'scnt': self.scnt,
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                tokenURL = "https://appleid.apple.com/account/manage/gs/ws/token"
                sendMyacinfo = self.session.get(tokenURL, cookies=self.session.cookies.get_dict(), headers=headers)

                self.aidsp = sendMyacinfo.cookies.get('aidsp')
                self.awat = sendMyacinfo.cookies.get('awat')
                self.caw = sendMyacinfo.cookies.get('caw')
                self.caw_at = sendMyacinfo.cookies.get('caw-at')
                self.scnt = sendMyacinfo.headers.get('scnt')

                manageURL = "https://appleid.apple.com/account/manage"
                getManage = self.session.get(manageURL, cookies=self.session.cookies.get_dict(), headers=headers)
                names = getManage.json()['name']
                self.FNAME , self.LNAME = names['firstName'] , names['lastName']

                self.dat = getManage.cookies.get('dat')
                self.awat = getManage.cookies.get('awat')
                self.caw_at = getManage.cookies.get('caw-at')
                params = {
                    'localeChange': 'true',
                }
                usaURL = "https://appleid.apple.com/us/"
                gotoUSA = self.session.get(usaURL, params=params, cookies=self.session.cookies.get_dict(), headers=headers)
                self.headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    'Origin': 'https://appleid.apple.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://appleid.apple.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-GPC': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    'X-Apple-Api-Key': 'cbf64fd6843ee630b463f358ea0b707b',
                    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":".ta44j1e3NlY5BNlY5BSs5uQ32SCVgecOJVv.1J8Qei.uJtHoqvynx9MsFyxY25CKw0KBN1xL8IXeDK1cDvmjpSbuVz3Y25BNlY5cklY5BqNAE.lTjV.096"}',
                    'X-Apple-I-Request-Context': 'ca',
                    'X-Apple-I-TimeZone': 'Africa/Cairo',
                    'scnt': self.scnt,
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                return True
            else:
                return False
        except:
            self.sendAnswers()

    def generate_password(self):
        letters = string.ascii_letters  
        digits = string.digits
        special_chars = '@!#'
        all_chars = letters + digits + special_chars
        password = ''.join(secrets.choice(all_chars) for _ in range(12))
        return password

    def start(self):
        self.preparing()
        logged = self.login()
        if logged:
            response = self.getQuestions()
            if response:
                final = self.sendAnswers()
                if final:
                    print(f"[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.LIGHTCYAN_EX} Success Login .. {RESET}[ {MANGETA}{self.email}{RESET} ]")
                    askPassword = config.getboolean('settings', 'change_password')
                    askQuestions = config.getboolean('settings', 'change_questions')
                    askRegion = config.getboolean('settings', 'change_region')
                    self.accinfo = self.session.cookies.get_dict()['myacinfo']
                    self.aidsp = self.session.cookies.get_dict()['aidsp']
                    self.caw = self.session.cookies.get_dict()['caw']
                    self.dat = self.session.cookies.get_dict()['dat']
                    self.caw_at = self.session.cookies.get_dict()['caw-at']
                    self.awat = self.session.cookies.get_dict()['awat']
                    self.aid = self.session.cookies.get_dict()['aid']
                    if askRegion:
                        self.changeRegion()
                    if askPassword:
                        self.changePassword()
                    if askQuestions:
                        self.changeQuestion()
                    try:
                        self.account = f'{self.email},{self.password},{self.birthday},{self.q1},{self.q2},{self.q3}'
                    except:
                        self.account = f'{self.email},{self.password},{self.q1},{self.q2},{self.q3}'
                    with open(f'{file_name}-changed.csv','a') as f:
                        f.write(f'{self.account}\n')
                    self.updateFile()
                    return True
                else:
                    print('There Are Problem in Questions')
                    with open(f'{file_name}-wrong.csv','a') as f:
                        f.write(f'{self.saccount}\n')
            else:
                print('There Are Problem To Get Questions')

    def changePassword(self):
        try:
            ranPSW = config.getboolean('password', 'password_random')
            if ranPSW:
                self.newPassword = self.generate_password()
            else:
                self.newPassword = config.get('password', 'password').strip()

            URL = 'https://appleid.apple.com/account/manage/validate/password'
            headers = {
                "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                "scnt": self.scnt,
                "x-apple-i-fd-client-info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"7ta44j1e3NlY5BNlY5BSs5uQ32SCVgeV.BdHirKHQei.uJtHoqvynx9MsFyxY25CKw0KBN1xLDllTdmcK0rTKIxBfy6hvqBBNlY5BPY25BNnOVgw24uy.2eV"}',
                "x-apple-i-request-context": "ca",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "x-apple-i-timezone": "Africa/Cairo",
                "x-apple-api-key": "cbf64fd6843ee630b463f358ea0b707b",
                "sec-ch-ua-platform": '"Windows"',
                "origin": "https://account.apple.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://account.apple.com/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                # Add the cookie if necessary:
                "cookie": f"dslang=US-EN; site=USA; geo=EG; idclient=web; myacinfo={self.accinfo}; caw={self.caw}; aidsp={self.aidsp}; dat={self.dat}; caw-at={self.caw_at}; awat={self.awat}; itspod=39; pltvcid=undefined; aid={self.aid}"
            }
            payload = {
                "password": self.newPassword,
                "updating": True
                }
            response = self.session.post(URL,headers=headers,json=payload)
            URL = 'https://appleid.apple.com/account/manage/security/password'
            payload = {
                "currentPassword": self.password,
                "newPassword": self.newPassword
                }
            response = self.session.put(URL,headers=headers,json=payload)
            self.password = self.newPassword
            if response.status_code == 200:
                if 'lastPasswordChangedDate' in response.text:
                    print(f"{Fore.YELLOW}[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.GREEN} Success Change Password .. {RESET}")
                else:
                    print(f"{Fore.YELLOW}[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.RED} Failed Change Password .. {RESET}")
        except:
            self.changePassword()

    def changeQuestion(self):
        try:
            randomQues = config.getboolean('questions', 'qusetions_random')
            if randomQues:
                self.q1 = 'qwe'
                self.q2 = 'qre'
                self.q3 = 'das'
            else:
                self.q1 , self.q2 , self.q3 = config.get('questions', 'qusetions').split(',')
            qURL = 'https://appleid.apple.com/account/manage/security/questions'
            accinfo = self.session.cookies.get_dict()['myacinfo']
            aidsp = self.session.cookies.get_dict()['aidsp']
            caw = self.session.cookies.get_dict()['caw']
            dat = self.session.cookies.get_dict()['dat']
            caw_at = self.session.cookies.get_dict()['caw-at']
            awat = self.session.cookies.get_dict()['awat']
            aid = self.session.cookies.get_dict()['aid']
            headers = {
                "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                "scnt": self.scnt,
                "x-apple-i-fd-client-info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"7ta44j1e3NlY5BNlY5BSs5uQ32SCVgeV.BdHirKHQei.uJtHoqvynx9MsFyxY25CKw0KBN1xLDllTdmcK0rTKIxBfy6hvqBBNlY5BPY25BNnOVgw24uy.2eV"}',
                "x-apple-i-request-context": "ca",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "x-apple-i-timezone": "Africa/Cairo",
                "x-apple-api-key": "cbf64fd6843ee630b463f358ea0b707b",
                "sec-ch-ua-platform": '"Windows"',
                "origin": "https://account.apple.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://account.apple.com/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                # Add the cookie if necessary:
                "cookie": f"dslang=US-EN; site=USA; geo=EG; idclient=web; myacinfo={accinfo}; caw={caw}; aidsp={aidsp}; dat={dat}; caw-at={caw_at}; awat={awat}; itspod=39; pltvcid=undefined; aid={aid}"
            }
            payload = {
                "questions": [
                    {
                    "answer": f"{self.q1}",
                    "id": "130",
                    "question": "What is the first name of your best friend in high school?"
                    },
                    {
                    "answer": f"{self.q2}",
                    "id": "136",
                    "question": "What is your dream job?"
                    },
                    {
                    "answer": f"{self.q3}",
                    "id": "142",
                    "question": "In what city did your parents meet?"
                    }
                ]
                }
            response = self.session.put(qURL,headers=headers,json=payload)
            if 'formattedAccountName' in response.text:
                URL = 'https://appleid.apple.com/authenticate/password'
                response = self.session.post(URL,headers=headers,json={"password": self.password})
                response = self.session.put(qURL,headers=headers,json=payload)
                if 'What is your dream' in response.text:
                    print(f"{Fore.YELLOW}[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.LIGHTGREEN_EX} Success Change Questions .. {RESET}")
                else:
                    print(f"{Fore.YELLOW}[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.RED} Problem in Change Questions .. {RESET}")
                    try:
                        self.account = f'{self.email},{self.password},{self.birthday},{self.q1},{self.q2},{self.q3}'
                    except:
                        self.account = f'{self.email},{self.password},{self.q1},{self.q2},{self.q3}'
                    with open('notsucces.csv','a') as f:
                        f.write(f'{self.account}\n')
        except:
            self.changeQuestion()

    def changeRegion(self):
        URL = 'https://appleid.apple.com/account/manage/payment/method/none/1'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            f"idclient=web; dslang=US-EN; site=USA; geo=IL; aid={self.aid}; dat={self.dat}; myacinfo={self.myacinfo}; awat={self.awat}; caw={self.caw}; caw-at={self.caw_at}; aidsp={self.aidsp}"
            'Referer': 'https://appleid.apple.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ32SCVgecFW2A2p9ffSKk6Hb9LarUqUdHz16rgNNlejV9dY.Mel9SpDK1cDvkjmxMuijjNklY5BNleBBNlYCa1nkBMfs.7wM"}',
            'X-Apple-I-Request-Context': 'ca',
            'X-Apple-I-TimeZone': 'Africa/Cairo',
            'scnt': self.scnt,
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        random_num = f"05{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(100, 999)}"
        payload = {
            "ownerName": {
                "firstName": self.FNAME,
                "lastName": self.LNAME
            },
            "phoneNumber": {
                "areaCode": "",
                "number": f"5{random_num}",
                "countryCode": "1"
            },
            "billingAddress": {
                "line1": "8201 Lomas Blvd NE",
                "line2": "Albuquerque",
                "line3": "",
                "suburb": "",
                "county": "",
                "city": "Albuquerque",
                "countryCode": "USA",
                "postalCode": "87110",
                "stateProvinceName": "NY"
            },
            "id": 1
            }
        response = self.session.put(URL,headers=headers,json=payload)
        URL = 'https://appleid.apple.com/account/manage/address/shipping'
        payload = {
                "line1": "8201 Lomas Blvd NE",
                "line2": "",
                "line3": "",
                "suburb": "",
                "city": "Albuquerque",
                "county": "",
                "postalCode": "87110",
                "stateProvinceName": "NY",
                "countryCode": "USA",
                "company": "",
                "recipientFirstName": "john",
                "recipientLastName": "wick",
                "label": "SHIPPING ADDRESS",
                "type": "shipping"
                }
        response = self.session.post(URL,headers=headers,json=payload)
        print(f"{Fore.YELLOW}[{BLUE}{self.index}/{accounts_len}{RESET}]{Fore.LIGHTGREEN_EX} Success Change Region To USA .. {RESET}")



def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(
        Panel("""[bold red]● [bold yellow]● [bold green]●[bold white]
[bold red]██████╗░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
[bold red]╚════██╗██╔═══╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗
[bold red]░█████╔╝██████╗░██████╦╝██║░░██║██║░░██║███████║
[bold white]░╚═══██╗██╔══██╗██╔══██╗██║░░██║██║░░██║██╔══██║
[bold white]██████╔╝╚█████╔╝██████╦╝╚█████╔╝██████╔╝██║░░██║
[bold white]╚═════╝░░╚════╝░╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝
[underline green]Coded By BoDa - Whatsapp [+201098974486]""", width=55,style="bold bright_white"))
def main():
    global ACCSUPDATE , accounts_len , file_name
    try:
        LOGO()
        browser_num = 1
        ACCS = []
        file_name = input('[!] Enter File Name: ').strip()
        all_list = open(f'{file_name}.csv', 'r').read().splitlines()
        for i in range(0, len(all_list)):
            ACCS.append(all_list[i])
        ACCSUPDATE = ACCS.copy()
        accounts_len = len(ACCS)
        if accounts_len % browser_num == 0:
            enteries_cnt = accounts_len // browser_num
        else:
            enteries_cnt = accounts_len // browser_num + 1
        cnt = 0
        for i in range(enteries_cnt):
            threads = []
            for j in range(browser_num):
                account = ACCS[cnt]
                v = apple(cnt,account,)
                t = threading.Thread(target= v.start, args=())
                t.start()
                threads.append(t)
                cnt += 1
            for t in threads:
                t.join()
        print(Fore.MAGENTA, end='')
        input('PRESS ENTER TO EXIT')
    except Exception as e:
        print(Fore.RED,e, end='')
        input('Error Occurred. Make sure inputs are digits.\nPRESS ENTER TO EXIT')
main()