# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import time
from machine import Pin
from demo import app_instance

def wifi():
    led = Pin(2,Pin.OUT)
    wlan = network.WLAN(network.STA_IF)  # 定义WLAN
    wlan.active(True)  # True和False控制WIFI的开关
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ChinaNet-A90AF8', 'cuxe7443') #需要手动输入wifi名字和密码
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            time.sleep(1)
            i = i + 1
    print('network config:', wlan.ifconfig()[0])  # 打印出ESP32当前连接网络的IP地址
    led.value(1)
    
if __name__ == '__main__':
    wifi()
    app_instance.run()
