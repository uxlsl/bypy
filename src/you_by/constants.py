# -*- coding:utf-8 -*-

OneK = 1024
OneM = OneK * OneK
OneG = OneM * OneK
OneT = OneG * OneK
OneP = OneT * OneK
OneE = OneP * OneK
OneZ = OneE * OneK
OneY = OneZ * OneK
SIPrefixNames = [ '', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y' ]

SIPrefixTimes = {
	'K' : OneK,
	'M' : OneM,
	'G' : OneG,
	'T' : OneT,
	'E' : OneE,
	'Z' : OneZ,
	'Y' : OneY }

### return (error) codes
# they are put at the top because:
# 1. they have zero dependencies
# 2. can be referred in any abort later, e.g. return error on import faliures
ENoError = 0 # plain old OK, fine, no error.
EIncorrectPythonVersion = 1
#EApiNotConfigured = 10 # Deprecated: ApiKey, SecretKey and AppPcsPath not properly configured
EArgument = 10 # invalid program command argument
EAbort = 20 # aborted
EException = 30 # unhandled exception occured
EParameter = 40 # invalid parameter passed to ByPy
EInvalidJson = 50
EHashMismatch = 60 # MD5 hashes of the local file and remote file don't match each other
EFileWrite = 70
EFileTooBig = 80 # file too big to upload
EFailToCreateLocalDir = 90
EFailToCreateLocalFile = 100
EFailToDeleteDir = 110
EFailToDeleteFile = 120
EFileNotFound = 130
EMaxRetry = 140
ERequestFailed = 150 # request failed
ECacheNotLoaded = 160
EMigrationFailed = 170
EDownloadCerts = 180
EUserRejected = 190 # user's decision
EFatal = -1 # No way to continue
# internal errors
IEMD5NotFound = 31079 # File md5 not found, you should use upload API to upload the whole file.
IESuperfileCreationFailed = 31081 # superfile create failed
