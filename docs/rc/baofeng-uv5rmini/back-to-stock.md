# Back to stock

> **Release candidate docs: 1.0.0-rc.1** These pages describe a release candidate that is still being tested.

Steps marked *Not yet checked on a radio* are a plan, not a record.

Going back puts the maker's own firmware (Firmware `V0.27`) back on the radio. It is there for emergencies, for
example if a release has a fault you can't live with. It leaves your channels and settings alone.

Each release is published with a **to-stock file** for the radios it supports. Use the one from the release your radio
runs, together with your stock firmware file (see [install.md](install.md#what-you-need)). Codeplug Studio's
**Back to stock** is the only way back this project supports.

## With Codeplug Studio

1. **Not yet checked on a radio.** Open [Codeplug Studio](https://codeplug.mm9pdy.net), go to the *Firmware flasher*,
   pick the UV-5R Mini, and choose **Back to stock**.
2. **Not yet checked on a radio.** Give Studio the to-stock file and your stock firmware file. Studio checks both and
   refuses files it does not know.
3. **Not yet checked on a radio.** Let Studio read the radio in normal mode. A radio running an MM9PDY build tells
   Studio which build it has.
4. **Not yet checked on a radio.** Put the radio into update mode (switch off, hold **PTT-A** and **=**, switch on,
   let go at the computer picture and `UPDATE...`), then press **Connect and flash**, as in
   [install.md](install.md#2-write-it-with-codeplug-studio). It takes about 3 minutes. Keep the cable in and leave the
   battery alone until the radio shows its normal screen.

## Check it worked

1. **Not yet checked on a radio.** The power-on screen no longer shows an MM9PDY build name.
2. **Not yet checked on a radio.** Radio Info shows `Firmware:V0.27` and `Hardware:V1.7`, with no fourth line.
3. **Not yet checked on a radio.** The menu has no Zones item, and Up and Down step through every channel.

If the update stops part way, or the radio does not start, see [recovery.md](recovery.md).
