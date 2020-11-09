import requests, subprocess, json, sys, platform, Extras
from Config import *
from Functions import *

# Print out the settings assigned in Config.py
ConfigStartup = config.start()

# Check every proxy in your proxy file,
working_proxies = check_proxies(config.Proxy_File)

# Gets number of proxies that work.
number_of_proxies = len(working_proxies)

# Gets number of lines in proxy file to print out how many are working.
InputProxies = get_file_lines()
print(f"{bcolors.OKGREEN}{number_of_proxies}{bcolors.ENDC} proxies working out of {bcolors.OKGREEN}{InputProxies}{bcolors.ENDC}.")

# Gets Json data about the livestream
X = getchannelinfo(config.Channel_URL)
