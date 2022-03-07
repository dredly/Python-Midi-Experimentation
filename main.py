import mido


def display_message(msg):
    strng = ""
    for byte in msg.bytes():
        strng += hex(byte) + " "
    print(msg)
    print(msg.bytes())
    print(strng)


print(mido.get_output_names()[0])
try:
    port = mido.open_output(mido.get_output_names()[1])
except:
    port = mido.open_output(mido.get_output_names()[0])

from testing import still_dre

still_dre()
