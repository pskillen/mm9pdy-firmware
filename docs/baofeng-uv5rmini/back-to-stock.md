# Back to stock

<!-- variant-status:start -->
> **Availability by radio:** NRF, Firmware V0.27, Hardware V1.7: latest release 1.0.0. NRFB, Firmware V0.04, Hardware V1.7: latest release 1.0.0.
<!-- variant-status:end -->

Steps marked *Not yet checked on a radio* are a plan, not a record. Steps marked *Checked on a radio with the
1.0.0 release* were performed on a radio with that release.

Going back puts the maker's own firmware (Firmware `V0.27` or `V0.04`, as the radio came) back on the radio. It is there for emergencies, for
example if a release has a fault you can't live with. It leaves your channels and settings alone.

Each release is published with a **to-stock file** for the radios it supports. Use the one from the release your radio
runs, together with your stock firmware file (see [install.md](install.md#what-you-need)). Codeplug Studio's
**Back to stock** is the only way back this project supports.

## With Codeplug Studio

1. **Checked on a radio with the 1.0.0 release.**
   Open [Codeplug Studio](https://codeplug.mm9pdy.net), go to the *Firmware flasher*,
   pick the UV-5R Mini, and choose **Back to stock**.
2. **Checked on a radio with the 1.0.0 release.**
   Studio offers the published to-stock file for your stock version; you can pick a file instead. Give Studio
   your stock firmware file. Studio checks both and refuses files it does not know.
3. **Checked on a radio with the 1.0.0 release.**
   Let Studio read the radio in normal mode. A radio running an MM9PDY build tells
   Studio which build it has.
4. **Checked on a radio with the 1.0.0 release.**
   Put the radio into update mode (switch off, hold **PTT-A** and **=**, switch on,
   let go at the computer picture and `UPDATE...`), then press **Connect and flash**, as in
   [install.md](install.md#2-write-it-with-codeplug-studio). It takes about 3 minutes. Keep the cable in and leave the
   battery alone until the radio shows its normal screen.

## Check it worked

1. **Checked on a radio with the 1.0.0 release.**
   The power-on screen no longer shows `MM9PDY mod` or an MM9PDY build name.
2. **Checked on a radio with the 1.0.0 release.**
   Radio Info shows `Firmware:V0.27` (or `Firmware:V0.04`) and `Hardware:V1.7`, with no fourth line.
3. **Checked on a radio with the 1.0.0 release.**
   The menu has no Zones item, and Up and Down step through every channel.

If the update stops part way, or the radio does not start, see [recovery.md](recovery.md).
