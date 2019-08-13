#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho


def on_message(mosq, obj, msg):
    """

    :param msg:
    :return:
    """
    print("%16s: %s" % (msg.topic, msg.payload))


if __name__ == '__main__':
    CLIENT = paho.Client()
    CLIENT.on_message = on_message
    CLIENT.connect("127.0.0.1", 1883, 60)
    CLIENT.subscribe("Items")
    CLIENT.subscribe("USER CPU used")
    CLIENT.subscribe("SYSTEM CPU used")
    CLIENT.subscribe("SOFT CPU used")
    CLIENT.subscribe("RAM used")
    CLIENT.subscribe("HOME DISK used")
    while CLIENT.loop() == 0:
        pass
