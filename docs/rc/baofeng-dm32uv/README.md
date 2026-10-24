# Baofeng DM-32UV: MM9PDY modded firmware

> **Release candidate docs: 1.2.0-rc.1** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../baofeng-dm32uv/README.md).

Small, carefully tested changes to Baofeng's own firmware **v1.01.048** for the DM-32UV dual-band DMR handheld: zone
scan, a quick menu with light mode, independent talk groups, a star-key timeslot swap and more. It is not a new
firmware: everything not listed in [features.md](features.md) behaves as stock v1.01.048.

> **This folder is published from the project's private repository on each release.** Edits made here are overwritten.
> To report a problem or ask for a feature, open an issue on the
> [public repository](https://github.com/pskillen/mm9pdy-firmware/issues).

## Pages

| Page | What it covers |
|---|---|
| [features.md](features.md) | What each feature does, how to use it, and its known limits |
| [install.md](install.md) | Putting a release on the radio with Codeplug Studio, and checking it worked |
| [back-to-stock.md](back-to-stock.md) | Putting stock v1.01.048 back |
| [recovery.md](recovery.md) | What to do when a write fails, and what never to do |

What each release contains, and its known limits, is in its release notes, in the
[releases folder](https://github.com/pskillen/mm9pdy-firmware/tree/main/releases/baofeng-dm32uv) of the public
repository. Codeplug Studio shows the same notes when you pick a release.

## Read this first

- **Flashing firmware can brick a radio.** Everything here is at your own risk, with no warranty of any kind. This is
  a hobby project tested on one radio.
- **Stock v1.01.048 only.** A release applies to Baofeng's v1.01.048 image (the radio shows it as `DM32.01.L01.048`)
  and nothing else. Codeplug Studio checks your stock file by SHA-256 and refuses any other version.
- **No Baofeng firmware is published here.** A release is a patch: you download the stock image from Baofeng yourself,
  and Codeplug Studio turns it into the modded firmware on your own computer.
- **A firmware write does not touch your codeplug.** The radio keeps your codeplug, a per-radio calibration page and a
  factory sector apart from the firmware, and the update does not write them. No firmware file can restore the
  calibration or the factory sector, so read [recovery.md](recovery.md#what-never-to-do) before you start.
- **Keep a way back.** Keep the stock zip. As long as the radio enters update mode, stock can be put back with
  Codeplug Studio or Baofeng's CPS ([back-to-stock.md](back-to-stock.md)).
- **Release candidates** (versions ending `-rc.N`) are for testing. They have passed the project's emulator tests but
  may not have been checked on a radio yet. Use a final release unless you want to help test.

## What you need

| Item | Why |
|---|---|
| A DM-32UV on stock v1.01.048, or on an earlier release of these mods | The radio |
| A desktop computer with Chrome or Edge | Codeplug Studio flashes over Web Serial, which those browsers support |
| The USB programming cable, plugged straight into the computer (no hub) | The write takes about two minutes and must not be interrupted |
| A full battery | Same reason |
| Baofeng's v1.01.048 zip | The patch is applied to it, and it is your way back |
| Baofeng's DMR CPS (Windows), optional | To save your codeplug, and as a second way back to stock |

## Getting help

Open an issue on the [public repository](https://github.com/pskillen/mm9pdy-firmware/issues/new/choose). Say which
release you used, what the screen and the LED showed, and what Codeplug Studio said. Do not attach a radio backup or a
codeplug: they hold your radio's calibration, your DMR ID and possibly encryption keys.
