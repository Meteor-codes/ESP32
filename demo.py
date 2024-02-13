from microdot import Microdot,send_file
from machine import Pin

class MyMicrodotApp: 
    def __init__(self):
        self.app = Microdot()
        self.led = Pin(2,Pin.OUT)

        @self.app.route('/')
        def index(request):
            return 'Hello, world!'

        @self.app.route('/control')
        def control(request):
            return send_file('/templates/index.html')

        @self.app.route('/control/open')
        def open(request):
            self.led.value(1)
            return send_file('/templates/open.html')

        @self.app.route('/control/close')
        def close(request):
            self.led.value(0)
            return send_file('/templates/close.html')
    
    def run(self, host='192.168.2.5', port=5000, debug=True, ssl=None):
        self.app.run(host=host, port=port, debug=debug, ssl=ssl)
        
# 创建应用实例
app_instance = MyMicrodotApp()
