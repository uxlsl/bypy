# -*- coding:utf-8 -*-

from os.path import expanduser
import os
import time

from constants import (
    OneK,
    OneM,
    OneG,
)

### Auth servers
GaeUrl = 'https://bypyoauth.appspot.com'
OpenShiftUrl = 'https://bypy-tianze.rhcloud.com'
HerokuUrl = 'https://bypyoauth.herokuapp.com'
GaeRedirectUrl = GaeUrl + '/auth'
GaeRefreshUrl = GaeUrl + '/refresh'
OpenShiftRedirectUrl = OpenShiftUrl + '/auth'
OpenShiftRefreshUrl = OpenShiftUrl + '/refresh'
HerokuRedirectUrl = HerokuUrl + '/auth'
HerokuRefreshUrl = HerokuUrl + '/refresh'
AuthServerList = [
	# url, rety?, message
	(OpenShiftRedirectUrl, False, "Authorizing/refreshing with the OpenShift server ..."),
	(HerokuRedirectUrl, True, "OpenShift server failed, authorizing/refreshing with the Heroku server ..."),
	(GaeRedirectUrl, False, "Heroku server failed. Last resort: authorizing/refreshing with the GAE server ..."),
]
RefreshServerList = AuthServerList

#### Baidu PCS constants
# ==== NOTE ====
# I use server auth, because it's the only possible method to protect the SecretKey.
# If you want to perform local authorization using 'Device' method instead, you just need:
# - Paste your own ApiKey and SecretKey. (An non-NONE or non-empty SecretKey means using local auth
# - Change the AppPcsPath to your own App's directory at Baidu PCS
# Then you are good to go
ApiKey = 'q8WE4EpCsau1oS0MplgMKNBn' # replace with your own ApiKey if you use your own appid
SecretKey = '' # replace with your own SecretKey if you use your own appid
# NOTE: no trailing '/'
AppPcsPath = '/apps/bypy' # change this to the App's directory you specified when creating the app
AppPcsPathLen = len(AppPcsPath)

## Baidu PCS URLs etc.
OpenApiUrl = "https://openapi.baidu.com"
OpenApiVersion = "2.0"
OAuthUrl = OpenApiUrl + "/oauth/" + OpenApiVersion
ServerAuthUrl = OAuthUrl + "/authorize"
DeviceAuthUrl = OAuthUrl + "/device/code"
TokenUrl = OAuthUrl + "/token"
PcsDomain = 'pcs.baidu.com'
RestApiPath = '/rest/2.0/pcs/'
PcsUrl = 'https://' + PcsDomain + RestApiPath
CPcsUrl = 'https://c.pcs.baidu.com/rest/2.0/pcs/'
DPcsUrl = 'https://d.pcs.baidu.com/rest/2.0/pcs/'

### ByPy config constants
## directories, for setting, cache, etc
HomeDir = expanduser('~')
# os.path.join() may not handle unicode well
ConfigDir = HomeDir + os.sep + '.bypy'
TokenFileName = 'bypy.json'
TokenFilePath = ConfigDir + os.sep + TokenFileName
SettingFileName= 'bypy.setting.json'
SettingFilePath= ConfigDir + os.sep + SettingFileName
HashCacheFileName = 'bypy.hashcache.json'
HashCachePath = ConfigDir + os.sep + HashCacheFileName
PickleFileName = 'bypy.pickle'
PicklePath = ConfigDir + os.sep + PickleFileName
# ProgressPath saves the MD5s of uploaded slices, for upload resuming
# format:
# {
# 	abspath: [slice_size, [slice1md5, slice2md5, ...]],
# }
#
ProgressFileName = 'bypy.parts.json'
ProgressPath = ConfigDir + os.sep + ProgressFileName
ByPyCertsFileName = 'bypy.cacerts.pem'
ByPyCertsPath = ConfigDir + os.sep + ByPyCertsFileName
# Old setting locations, should be moved to ~/.bypy to be clean
OldTokenFilePath = HomeDir + os.sep + '.bypy.json'
OldPicklePath = HomeDir + os.sep + '.bypy.pickle'
RemoteTempDir = AppPcsPath + '/.bypytemp'
SettingKey_OverwriteRemoteTempDir = 'overwriteRemoteTempDir'

## default config values
# TODO: Does the following User-Agent emulation help?
#UserAgent = None # According to xslidian, User-Agent affects download.
#UserAgent = 'Mozilla/5.0'
#UserAgent = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
UserAgent = 'netdisk;5.2.7.2;PC;PC-Windows;6.2.9200;WindowsBaiduYunGuanJia'
DefaultSliceInMB = 20
# DefaultSliceSize = 20 * OneM
DefaultSliceSize = 0
DefaultDlChunkSize = 20 * OneM
RetryDelayInSec = 10
## global variables
# the previous time stdout was flushed, maybe we just flush every time, or maybe this way performs better
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
last_stdout_flush = time.time()
#last_stdout_flush = 0
PrintFlushPeriodInSec = 5.0
# save cache if more than 10 minutes passed
last_cache_save = time.time()
CacheSavePeriodInSec = 10 * 60.0
# share retries
ShareRapidUploadRetries = 3
## program switches
CleanOptionShort= '-c'
CleanOptionLong= '--clean'
DisableSslCheckOption = '--disable-ssl-check'
CaCertsOption = '--cacerts'

## Baidu PCS constants
MinRapidUploadFileSize = 256 * OneK
MaxSliceSize = 2 * OneG
MaxSlicePieces = 1024


