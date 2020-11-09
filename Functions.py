"""
Imports
"""
# noinspection PyUnresolvedReferences
from Config import *
from Functions import *
import requests
import subprocess
import json
import sys
import platform
import Extras
import time


"""
This is the file where all functions get stored to keep "Main.py" clean
"""


# noinspection SpellCheckingInspection
def getchannelinfo(channel_url):
    # Call livestreamer function to get data in json about the stream
    try:
        response = subprocess.Popen(
            ["streamlink", "--http-header", "Client-ID=ewvlchtxgqq88ru9gmfp1gmyt6h2b93", channel_url, "-j"], stdout=subprocess.PIPE).communicate()[0]
    except OSError:
        print("[Error] Livestreamer package not detected.")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    #######################################################################################################

    try:
        channel_url = json.loads(response)['streams']['audio']['url']
    except Exception as e:
        print(e)
    try:
        url = channel_url
    except Exception as e:
        print(e)
        sys.exit(1)

    return url


def ping(host):

    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '1', '-w', str(config.Ping_Timeout), '-n', '1', host]
    return subprocess.call(command, stdout=subprocess.PIPE) == 0


def check_proxies(filename):
    filename = str(filename)
    f = open(filename)
    lines = 0
    for _ in f:
        lines = lines + 1
    f.close()

    EstimatedTime = lines * config.Ping_Timeout
    print(f"{bcolors.Blue}Checking proxies... this will take at max {bcolors.OKGREEN}{EstimatedTime / 1000}{bcolors.Blue} seconds{bcolors.ENDC}")

    with open(filename) as f:
        workingProxies = []
        LineNum = 0
        for line in f.readlines():
            line = line.strip("\n").strip('\r')
            line = line.split(":")
            line_port = line[1]
            line_ip = line[0]
            if LineNum == 50:
                if config.extras.Proxy_Joke.Proxy_Joke_Extra:
                    print_dad_joke()
                else:
                    pass
            LineNum = LineNum + 1
            if ping(line_ip):
                workingProxies = workingProxies + [f"{line_ip}:{line_port}"]
            else:
                pass
        if len(workingProxies) == 0:
            print("Error, no working proxies were detected, are you connected to the internet?")
    return workingProxies


def get_file_lines():
    InputProxies = 0
    with open(config.Proxy_File) as G:
        for _ in G.readlines():
            InputProxies = InputProxies + 1
    return InputProxies


def open_url(url, proxy):

    print()
    while True:
        try:
            with requests.Session() as s:
                response = s.head(url, proxies=proxy, headers=advancedConfig.headers)
                if response:
                    pass
                print(f'Sent head request with {proxy["http"]}')
                time.sleep(20)

        except requests.exceptions.Timeout:
            print(f'  Timeout error for {proxy["http"]}')
        except requests.exceptions.ConnectionError:
            print(f'  Connection error for {proxy["http"]}')
        except Exception as e:
            print(e)


def print_dad_joke():
    print()
    print()
    print(f"{bcolors.Magenta}Hows it going, wanna hear a joke?{bcolors.ENDC}")
    print(f"{bcolors.Magenta}Well I don't really care, your reading this joke!{bcolors.ENDC}")
    print(f"{bcolors.Magenta}-------------------------------------------------{bcolors.ENDC}")
    print(Extras.get_dad_joke())
    print(f"{bcolors.Magenta}-------------------------------------------------{bcolors.ENDC}")
    print()
    print()
