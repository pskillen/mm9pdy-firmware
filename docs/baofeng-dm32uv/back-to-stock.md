# Going back to stock

How to put Baofeng's stock v1.01.048 back on the radio. You need the stock zip
([install.md](install.md#1-get-the-stock-v101048-image)). Your codeplug stays.

## 1. With Codeplug Studio

In [Codeplug Studio](https://codeplug.mm9pdy.net), **Tools > Firmware flasher**, pick the DM-32UV, then
**Stock firmware** instead of a release. Drop the stock zip, and follow the same steps as an install
([install.md](install.md#3-flash-with-codeplug-studio)), including the update-mode order: radio off, SK1 and PTT at
power-on, green LED, then plug in the cable.

## 2. With Baofeng's CPS (Windows)

1. Unpack `DM32_L01_048_20250821.bin` from the stock zip.
2. Put the radio into update mode ([install.md](install.md#3-flash-with-codeplug-studio), step 6) and plug in the
   cable.
3. In the CPS: **Tool**, **Firmware Upgrade**; choose the `.bin`; start the upgrade. It takes about two minutes.
4. When it finishes, turn the radio off and on again.

## 3. Check it worked

- The radio starts normally with your channels.
- **Settings > Device Info > Versions** shows `DM32.01.L01.048` and no `mm9pdy-` line.

## 4. Your codeplug on stock firmware

The codeplug format is not changed, so your codeplug works on stock. The light-mode setting stays in the codeplug as
one byte that stock firmware ignores, and the stock look returns. If you had the **Flashlight** key function assigned
for the quick menu, it goes back to giving an error tone.

## 5. If it goes wrong

See [recovery.md](recovery.md).
