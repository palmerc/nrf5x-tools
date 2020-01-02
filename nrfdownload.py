#curl -H 'Host: www.nordicsemi.com' -H 'Cookie: ASP.NET_SessionId=hgdauwnvhqa0tqud5hv4vtxm; SC_ANALYTICS_GLOBAL_COOKIE=6d2e178f8aeb48c3bf769c9a9e948337|True' -H 'content-type: application/json; charset=utf-8' -H 'accept: */*' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-gb' -H 'origin: https://www.nordicsemi.com' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15' -H 'referer: https://www.nordicsemi.com/Software-and-tools/Software/nRF5-SDK/Download' --data-binary "" --compressed 'https://www.nordicsemi.com/api/sitecore/Products/GetAllSdkVersions?productItemId={21C26716-5F2C-4E2D-9514-C9B87B711114}'

import os
import re
import requests

dload_dir_elements = ['.', 'developer.nordicsemi.com', 'nRF5_SDK']
base_url = 'https://www.nordicsemi.com'
all_sdks_url = base_url + '/api/sitecore/Products/GetAllSdkVersions?productItemId={21C26716-5F2C-4E2D-9514-C9B87B711114}'
softdevice_matrix_url = 'https://www.nordicsemi.com/api/sitecore/Products/GetCompatibleSoftDevicesForSDK?sdkVersionItemId='

title_re = re.compile(r'(?P<sdk>nRF5\d?)_?SDK_?(?P<major>\d+)\.?(?P<minor>\d)\.?(?P<update>\d)_?(?P<hash>[0-9a-f]{7}).*(\.zip)?$')

r = requests.post(all_sdks_url)
product_dict = r.json()
sdks = product_dict['data']['SDKs']
for sdk in sdks:
    id = sdk['Id']
    sdk_title = sdk['Binary']['Title']
    sdk_dload_url = sdk['Binary']['DownloadUrl']

    matches = title_re.search(sdk_title)
    sdk_name = matches['sdk']
    sdk_major = matches['major']
    sdk_minor = matches['minor']
    sdk_update = matches['update']
    sdk_hash = matches['hash']

    download_path = dload_dir_elements.copy()
    download_path.append('{}_SDK_v{}.x.x'.format(sdk_name, sdk_major))
    download_dir = os.path.sep.join(download_path)
    print('Create directory {}'.format(download_dir))
    os.makedirs(os.path.join(download_dir), exist_ok=True)

    sdk_zip = '{}_SDK_{}.{}.{}_{}.zip'.format(sdk_name, sdk_major, sdk_minor, sdk_update, sdk_hash)
    print('Downloading {} to {}'.format(sdk_title, sdk_zip))
    r = requests.get(base_url + sdk_dload_url, allow_redirects=True)
    open(os.path.join(download_dir, sdk_zip), 'wb').write(r.content)
    r = requests.post(softdevice_matrix_url + id)
    softdevice_dict = r.json()
    softdevices = softdevice_dict['data']['SoftDevices']
    for softdevice in softdevices:
        if softdevice['DownloadDisabled']:
            continue

        sd_title = softdevice['Binary']['Title']
        sd_dload_url = softdevice['Binary']['DownloadUrl']
        # r = requests.get(base_url + sd_dload_url, allow_redirects=True)
        # open(os.path.join(download_dir, sd_title), 'wb').write(r.content)
        print('\t {}'.format(sd_title))