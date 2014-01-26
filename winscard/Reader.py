from ctypes import *
from ctypes.wintypes import *
from winscard import *


class Reader:
    active_protocol = DWORD()

    def __init__(self, reader_name, card, context):
        self.reader_name = reader_name
        self.card = card
        self.context = context

    def __str__(self):
        return str(self.reader_name.value)

    def connect(self):
        result = ULONG(scard_dll.SCardConnectA(self.context, self.reader_name, SCARD_SHARE_SHARED,
                                               SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1, pointer(self.card),
                                               pointer(self.active_protocol)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)

    def control(self, ctl_code, sender):
        send_buffer = create_bytearray(sender)
        send_size = DWORD(sizeof(send_buffer))
        recv_buffer = (BYTE * 64)()
        recv_size = DWORD(64)
        ctl_code = DWORD(SCARD_CTL_CODE(ctl_code))
        result = DWORD(scard_dll.SCardControl(self.card, ctl_code, send_buffer, send_size, recv_buffer,
                                              DWORD(sizeof(recv_buffer)), pointer(recv_size)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)
        return recv_buffer[:recv_size.value]

    def transmit(self, sender, ioSendPci=None, ioRecvPci=None):
        send_buffer = create_bytearray(sender)
        send_size = DWORD(sizeof(send_buffer))
        recv_buffer = (BYTE * 64)()
        recv_size = DWORD(64)
        result = ULONG(scard_dll.SCardTransmit(self.card, ioSendPci, send_buffer, send_size, ioRecvPci, recv_buffer,
                                               pointer(recv_size)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)
        return recv_buffer[:recv_size.value]

    def status(self):
        state = DWORD()
        protocol = DWORD()
        atr = (BYTE * 64)()
        atrlen = DWORD(64)
        result = ULONG(scard_dll.SCardStatusA(
            self.card, self.reader_name, None, pointer(state), pointer(protocol), atr, pointer(atrlen)
        ))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)
        return {'state': state, 'protocol': protocol, 'ATR': atr[:atrlen.value]}

    def disconnect(self, dwDisposition=SCARD_LEAVE_CARD):
        result = ULONG(scard_dll.SCardDisconnect(self.card, DWORD(dwDisposition)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)