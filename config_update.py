#!/usr/bin/env python3

import urllib.request
import re

# Download the file
url = "https://raw.githubusercontent.com/crdroidandroid/android_frameworks_base/14.0/core/java/com/android/internal/util/crdroid/PixelPropsUtils.java"
response = urllib.request.urlopen(url)
content = response.read().decode()

# Find the spoofBuildGms function
spoof_build_gms = re.search(r'private static void spoofBuildGms\(\) \{(.+?)\}', content, re.DOTALL).group(1)

# Extract the FINGERPRINT and DEVICE values
fingerprint = re.search(r'setPropValue\("FINGERPRINT", "(.+?)"\);', spoof_build_gms).group(1)
device = re.search(r'setPropValue\("DEVICE", "(.+?)"\);', spoof_build_gms).group(1)

# Update the ih8sn.conf file
with open('system/etc/ih8sn.conf', 'r') as file:
    config = file.read()

config = re.sub(r'(?<=BUILD_FINGERPRINT=).*', fingerprint, config)
config = re.sub(r'(?<=PRODUCT_NAME=).*', device, config)

with open('system/etc/ih8sn.conf', 'w') as file:
    file.write(config)

# Copy the file
with open(f'system/etc/configs/ih8sn.conf.{device}', 'w') as file:
    file.write(config)
