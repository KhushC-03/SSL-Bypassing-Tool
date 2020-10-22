import os, sys, time, json
def connect_adb():
    o = open('config.json')
    data = json.load(o)
    scriptname = data['SSL-SCRIPT_NAME']
    if not str(scriptname):
        print('SSL Script Name Is Non Existent')
        print('Enter The Script Name In The config.json File And Try Again')
        input('Press ENTER to continue')
        menu()
    else:
        time.sleep(1)
        os.system("adb push platform-tools\\frida-server /data/local/tmp")
        time.sleep(0.5)
        os.system("adb shell chmod 777 /data/local/tmp/frida-server")
        time.sleep(0.5)
        os.system("adb push platform-tools\\cacert.der /data/local/tmp/cert-der.crt")
        time.sleep(0.5)
        os.system("adb push platform-tools\\{} /data/local/tmp".format(scriptname))
        time.sleep(0.5)
        os.system("adb shell /data/local/tmp/frida-server &")

def menu():
    connect_adb()

try:    
    menu()
except Exception as exception:
    print(exception)