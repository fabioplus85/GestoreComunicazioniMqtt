import time

import paho.mqtt.client as mqtt

class comunicatoreAllarme():
    broker = "192.168.1.101"
    porta = 1883
    client = None

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True  # set flag
            print("connected OK")
        else:
            print("Connessione fallita codice :", rc)

    def on_publish(self, client, userdata, result):
        print("dati pubblicati")

    def on_disconnect(client, userdata, rc):
        print("Client disconnesso")

    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        print("Messaggio ricevuto  ", msg)
        self.inviaMsg()

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscrive")

    def __init__(self):
        #self.client = mqtt.Client("Allarme")

        #self.client.on_connect = self.on_connect
        #self.client.on_disconnect = self.on_disconnect
        #self.client.on_message = self.on_message

        #self.client.connect(self.broker, self.porta)
        #self.client.subscribe("richiesta/luci")
        #self.client.loop_forever()

        self.inviaMsg()

    def inviaMsg(self):
        client1 = mqtt.Client("Allarme")

        client1.on_connect = self.on_connect
        client1.on_disconnect = self.on_disconnect
        client1.on_message = self.on_message

        client1.connect(self.broker, self.porta)

        i = 0
        while i < 10:
            time.sleep(1)
            client1.publish("casa/cucina/luce/1", "Accese " + str(i), qos=1)
            print("Invio " + str(i))
            i = i + 1

    def attesaRisposta(self, msg):
        return msg