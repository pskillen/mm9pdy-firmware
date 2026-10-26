# Going back to stock

> **Release candidate docs: 1.2.0-rc.4** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../anytone-at-d890uv/back-to-stock.md).

How to put AnyTone's stock V1.05 firmware back on the radio. You need the stock V1.05 zip
([install.md](install.md#1-get-the-stock-v105-package)).

Going back to stock changes only the firmware. Your codeplug and settings stay on the radio.

## 1. With Codeplug Studio

In [Codeplug Studio](https://codeplug.mm9pdy.net), **Tools > Firmware flasher**, pick the AT-D890UV, then
**Stock firmware** instead of a release. Drop the stock zip, and follow the same steps as an install
([install.md](install.md#3-flash-with-codeplug-studio)): update mode with **PTT and PF3**, then flash.

## 2. With the official CPS (Windows)

This route has worked on the test radio: a stock V1.05 write finished in under a minute and kept the codeplug and
settings.

1. Unpack the stock zip on the Windows machine. Keep the three files (`D890UV_V1.05_20260521.CDD`, `.CDI`, `.spi`)
   together, with their names unchanged.
2. Put the radio in update mode: switch off, hold **PTT and PF3**, switch on. The red LED blinks and the screen stays
   blank. Plug in the cable.
3. In the CPS, open **Tool > Firmware and Icon Update**, open the stock `.spi`, choose the COM port, tick **Duplex**,
   and start the update.
4. When it has finished, switch the radio off and on normally if it has not restarted by itself.

## 3. Check it worked

- The power-on screen no longer shows a release name.
- **Menu > Settings > Device Info** has no "Mod Ver:" item; "Firmware Ver:" shows "Ver 1.05".
- The radio reaches the channel screen with your channels and settings.

## 4. Your codeplug on stock firmware

The codeplug format is not changed by the mods, so your codeplug works on stock. Keys you set to Record Switch, Record
or Priority Zone for the mods do the stock functions again; you may want to reassign them.

The quick filters menu's own settings stay in a spare area of the settings memory that stock firmware ignores. If you
install a release again later, the mods should find them there (expected, not yet tried on the radio). More detail is
in [codeplug.md](codeplug.md).

## 5. If it goes wrong

See [recovery.md](recovery.md).
