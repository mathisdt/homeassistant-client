#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import datetime
import os.path
import requests
import time
import re

if not os.path.isfile("config.ini"):
    print(
        "config.ini not found - maybe you didn't copy (and customize) the file config-template.ini to config.ini yet?")
    exit(1)

config = configparser.ConfigParser()
config.read("config.ini")


def entity(entity_id):
    return requests.get(f'{config["HA"]["url"]}/api/states/{entity_id}',
                        headers={"Authorization": f'Bearer {config["HA"]["token"]}'}).json()


def calculate_delta(timestamp, tz) -> datetime.timedelta:
    modified_timestamp = re.sub(r'(Z|\+00:00)', 'UTC', re.sub(r'\.\d{1,6}', '', timestamp))
    given_timestamp = datetime.datetime.strptime(modified_timestamp, '%Y-%m-%dT%H:%M:%S%Z')
    given_timestamp = given_timestamp.replace(tzinfo=tz)
    now_timestamp = datetime.datetime.now(tz=given_timestamp.tzinfo)
    return now_timestamp - given_timestamp


def age_minutes(timestamp: str, tz: datetime.tzinfo = None):
    try:
        delta = calculate_delta(timestamp, tz)
        return f"{delta / datetime.timedelta(minutes=1):.0f}"
    except:
        return "?"


def age_hours(timestamp: str, decimal_separator: str = ".", tz: datetime.tzinfo = None):
    try:
        delta = calculate_delta(timestamp, tz)
        return f"{delta / datetime.timedelta(hours=1):.1f}".replace('.', decimal_separator)
    except:
        return "?"


# default values
now = time.localtime()
year = time.strftime("%Y", now)
month = time.strftime("%m", now)
day = time.strftime("%d", now)
hour = time.strftime("%H", now)
minute = time.strftime("%M", now)
second = time.strftime("%S", now)
# Home Assistant values
for req in config['REQUEST']:
    locals()[req] = eval(config['REQUEST'][req])

pattern = config['OUTPUT']['str']
print(eval(f"""f'''{pattern}'''"""))
