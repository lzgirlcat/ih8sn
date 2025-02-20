#!/usr/bin/env python3

import urllib.request
import json
import re

# Download the file
url = "https://raw.githubusercontent.com/crdroidandroid/android_vendor_certification/refs/heads/15.0/gms_certified_props.json"
response = urllib.request.urlopen(url)
content = json.loads(response.read())


# Update the ih8sn.conf file
with open('system/etc/ih8sn.conf', 'r') as file:
    config = file.read()

config = re.sub(r'(?<=BUILD_FINGERPRINT=).*', content["FINGERPRINT"], config)
config = re.sub(r'(?<=PRODUCT_NAME=).*', content["DEVICE"], config)

with open('system/etc/ih8sn.conf', 'w') as file:
    file.write(config)

# Copy the file
with open(f'system/etc/configs/ih8sn.conf.{content["DEVICE"]}', 'w') as file:
    file.write(config)
