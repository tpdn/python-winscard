from winscard import *

SCARD_S_SUCCESS = 0x0
SCARD_ALL_READERS = None

SCARD_AUTOALLOCATE = -1

SCARD_PROTOCOL_T0 = 0x0001
SCARD_PROTOCOL_T1 = 0x0002
SCARD_PROTOCOL_RAW = 0x0004

SCARD_SHARE_SHARED = 2

MAXIMUM_ATTR_STRING_LENGTH = 32

SCARD_SCOPE_USER = 0
SCARD_SCOPE_TERMINAL = 1
SCARD_SCOPE_SYSTEM = 2

FILE_DEVICE_SMARTCARD = 0x00000031
METHOD_BUFFERED = 0
FILE_ANY_ACCESS = 0

g_rgSCardT0Pci = SCARD_IO_REQUEST(SCARD_PROTOCOL_T0, 8)
g_rgSCardT1Pci = SCARD_IO_REQUEST(SCARD_PROTOCOL_T1, 8)
g_rgSCardRawPci = SCARD_IO_REQUEST(SCARD_PROTOCOL_RAW, 8)

SCARD_PCI_T0 = pointer(g_rgSCardT0Pci)
SCARD_PCI_T1 = pointer(g_rgSCardT1Pci)
SCARD_PCI_RAW = pointer(g_rgSCardRawPci)

SCARD_UNKNOWN = 0x00000000
SCARD_ABSENT = 0x00000001
SCARD_PRESENT = 0x00000002
SCARD_SWALLOWED = 0x00000003
SCARD_POWERED = 0x00000004
SCARD_NEGOTIABLE = 0x00000005
SCARD_SPECIFICMODE = 0x00000006

SCARD_LEAVE_CARD = 0x0000
SCARD_RESET_CARD = 0x0001
SCARD_UNPOWER_CARD = 0x0002
SCARD_EJECT_CARD = 0x0003