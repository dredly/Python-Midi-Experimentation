import mido
import time
from main import port


def play_chord(notes, on_time, off_time, volume):
    messages = {"start": [], "end": []}
    for channel, note in enumerate(notes):
        start_msg = mido.Message("note_on", channel=channel, note=note, velocity=volume)
        end_msg = mido.Message("note_off", channel=channel, note=note, velocity=volume)
        messages["start"].append(start_msg)
        messages["end"].append(end_msg)
    for s_msg in messages["start"]:
        port.send(s_msg)
    time.sleep(on_time)
    for e_msg in messages["end"]:
        port.send(e_msg)
    time.sleep(off_time)


def still_dre():
    for _ in range(4):
        for _ in range(8):
            play_chord([60, 64, 69], 0.1, 0.2, 100)
        for _ in range(3):
            play_chord([59, 64, 69], 0.1, 0.2, 100)
        for _ in range(5):
            play_chord([59, 64, 67], 0.1, 0.2, 100)
