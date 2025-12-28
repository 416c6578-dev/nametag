#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import lednamebadge  # Aus paste.txt

# EXAKT wie im Original-Code
text = "BESINNLICHE TAGE!"
creator = lednamebadge.SimpleTextAndIcons()
bitmap, length = creator.bitmap_text(text)
buf = lednamebadge.array('B')
buf.extend(lednamebadge.LedNameBadge.header([length], [4], [0], [0], [0]))
buf.extend(bitmap)

# HID senden (wie im Original)
import hid
devs = hid.enumerate(0x0416, 0x5020)
if devs:
    d = hid.device()
    d.open_path(devs[0]['path'])
    for i in range(0, len(buf), 64):
        report = lednamebadge.array('B', [0] + list(buf[i:i+64]))
        d.write(report)
    print(f'✅ Original "HELLO WORLD!" ({length} Spalten) gesendet!')
    d.close()
else:
    print('❌ Badge nicht gefunden')
