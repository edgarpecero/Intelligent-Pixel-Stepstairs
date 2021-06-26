import webrepl

# Define a do_connect to initialize WiFi Conection using static IP Adress
def do_connect(ssid, pwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #static IP adress for the Board
        sta_if.ifconfig(('192.168.1.101','255.255.255.0','192.168.1.254','192.168.1.254'))
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect('INFINITUM7bsj', 'd061436793')

# Starts WebREPL
webrepl.start()

