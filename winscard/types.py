from ctypes import *
from ctypes.wintypes import *

SCARDCONTEXT = LONG
SCARDHANDLE = LONG
BYTE = c_ubyte


class SCARD_IO_REQUEST(Structure):
    _fields_ = [
        ('dwProtocol', DWORD),
        ('cbPciLength', DWORD)
    ]


class SCARD_READERSTATE(Structure):
    _fields_ = [
        ('szReader', LPCSTR),
        ('pvUserData', LPVOID),
        ('dwCurrentState', DWORD),
        ('dwEventState', DWORD),
        ('cbAtr', DWORD),
        ('rgbAtr', BYTE * 36)
    ]