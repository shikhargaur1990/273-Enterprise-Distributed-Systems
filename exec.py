from __future__ import print_function
import subprocess
import re

host_list = ['us-east-1  [54.152.63.252]', 'us-east-2 [18.216.0.253]', 'us-west-1  [13.52.0.2]',
             'us-west-2  [34.208.63.251]', 'ca-central-1  [35.182.0.251]', 'sa-east-1  [18.231.0.252]',
             'eu-west-1  [34.240.0.253]', 'eu-central-1  [18.194.0.252]', 'eu-west-2  [35.176.0.252]',
             'eu-west-3  [35.180.0.253]', 'ap-northeast-1  [13.112.63.251]', 'ap-northeast-2  [13.124.63.251]',
             'ap-southeast-1  [13.228.0.251]', 'ap-southeast-2  [13.54.63.252]', 'ap-south-1  [13.126.0.252]']
result=[]

for i in range(len(host_list)):

    regex_ip = "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*"
    match = re.findall(regex_ip, host_list[i])

    ping = subprocess.Popen(
        ["ping", "-c", "3", match[0]],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
    out, error = ping.communicate()
    s = str(out, 'utf-8')

    regex = "mdev = [0-9]*[\.]?[0-9]*\/([0-9]*[\.]?[0-9]*)\/"
    match = re.findall(regex, s)
    if match:
        result.append(round(float(match[0])))
result.sort()

# print the result

for i in range(len(host_list)):
    print(str(i+1) + ". " + host_list[i] + " - " + str(result[i]) + " ms")