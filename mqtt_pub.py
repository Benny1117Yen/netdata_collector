#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Publish some messages to queue
"""
import time
import paho.mqtt.publish as publish
import requests


URL = 'http://10.144.49.142:19999/api/v1/allmetrics?format=json'
HOST = 'localhost'


def user_cpu_usage(cpu_used, cpu_sum):
    """
    :function
    :param cpu_used:
    :param cpu_sum:
    :return: user_cpu_usage
    """
    return cpu_used / cpu_sum


def system_cpu_usage(cpu_used, cpu_sum):
    """
    :function
    :param cpu_used:
    :param cpu_sum:
    :return: system_cpu_usage
    """
    return cpu_used / cpu_sum


def soft_cpu_usage(cpu_used, cpu_sum):
    """
    :function
    :param cpu_used:
    :param cpu_sum:
    :return: softirq_cpu_usage
    """
    return cpu_used / cpu_sum


def ram_usage(ram_used, ram_sum):
    """
    :function
    :param ram_used:
    :param ram_sum:
    :return: ram_usage
    """
    return ram_used / ram_sum * 100


def disk_home_usage(disk_used, dick_sum):
    """
    :function
    :param disk_used:
    :param dick_sum:
    :return: disk_home_usage
    """
    return disk_used / dick_sum * 100


def refresh_data():
    """
    :function
    :return: msgs_payloads
    """
    data0 = requests.get(URL)
    data = data0.json()
    cpu = data["system.cpu"]
    used0 = cpu['dimensions']['user']['value']
    used4 = cpu['dimensions']['system']['value']
    used5 = cpu['dimensions']['softirq']['value']
    sum1 = 1
    ram = data["system.ram"]
    used1 = ram['dimensions']['used']['value']
    sum2 = sum(f['value'] for f in ram['dimensions'].values() if f)
    disk = data['disk_space._']
    used2 = disk['dimensions']['used']['value']
    sum3 = sum(g['value'] for g in disk['dimensions'].values() if g)
    msgs = [{'topic': "USER CPU used", 'payload': user_cpu_usage(used0, sum1)},
            {'topic': "SYSTEM CPU used", 'payload': system_cpu_usage(used4, sum1)},
            {'topic': "SOFT CPU used", 'payload': soft_cpu_usage(used5, sum1)},
            {'topic': "RAM used", 'payload': ram_usage(used1, sum2)},
            {'topic': "HOME DISK used", 'payload': disk_home_usage(used2, sum3)}]
    return msgs


if __name__ == '__main__':
    while True:
        publish.multiple(msgs=refresh_data(), hostname=HOST)
        time.sleep(1)
