from __future__ import print_function

import json
import subprocess

def parser():
    cmd = '''curl --user admin:test localhost/Api/EasyIoT/Config/Module/List'''
    args = cmd.split()
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    #jsondata = json.dumps(stdout.text)
    jsonToDict = json.loads(stdout)
    #print (jsonToDict)
    modules = jsonToDict["Modules"]
    #print (modules)

    for module in modules:
        #print('Module: ', module)
        #print(module["Domain"])
        if module['Domain'] == "Esp8266":
            #print(module["Domain"])
            for property in module['Properties']:
                if property['Name'] != 'Status.Connection':
                    print('Module address: ', module["Address"])
                    print('Name: ', property['Name'])
                    print('Time: ', property['UpdateTime'])
                    print('Value: ', property['Value'])


if __name__ == "__main__":
    parser()
