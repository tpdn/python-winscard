from winscard import *


def CTL_CODE(t, f, m, a):
    return (t << 16) | (a << 14) | (f << 2) | m


def SCARD_CTL_CODE(code):
    return CTL_CODE(FILE_DEVICE_SMARTCARD, code, METHOD_BUFFERED, FILE_ANY_ACCESS)


def create_bytearray(byte_list):
    return (BYTE * len(byte_list))(*byte_list)
