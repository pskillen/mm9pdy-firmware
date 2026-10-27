# AnyTone AT-D890UV: MM9PDY modded firmware

> **Release candidate docs: 1.2.1-rc.1** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../anytone-at-d890uv/README.md).

Small, carefully tested changes to AnyTone's own firmware **V1.05** for the AT-D890UV dual-band DMR handheld:
independent talk groups, a star-key timeslot toggle, zone scan, a quick filters menu and more. It is not a new
firmware: everything not listed in [features.md](features.md) behaves as stock V1.05.

> **This folder is published from the project's private repository on each release.** Edits made here are overwritten.
> To report a problem or ask for a feature, open an issue on the
> [public repository](https://github.com/pskillen/mm9pdy-firmware/issues).

## Pages

| Page | What it covers |
|---|---|
| [features.md](features.md) | What each mod does, how to set it up, and its limits |
| [install.md](install.md) | Putting a release on the radio with Codeplug Studio, and checking it worked |
| [codeplug.md](codeplug.md) | Your codeplug with the mods and on stock: reused key functions, the mods' own settings |
| [back-to-stock.md](back-to-stock.md) | Putting stock V1.05 back |
| [recovery.md](recovery.md) | What to do when a write fails or the radio will not start |

What each release contains, and its known limits, is in its release notes, in the
[releases folder](https://github.com/pskillen/mm9pdy-firmware/tree/main/releases/anytone-at-d890uv) of the public
repository. Codeplug Studio shows the same notes when you pick a release.

## Read this first

- **Flashing firmware can brick a radio.** Everything here is at your own risk, with no warranty of any kind. This is
  a hobby project tested on one radio.
- **Stock V1.05 only.** A release applies to AnyTone's V1.05 package (20260521) and nothing else. Codeplug Studio
  checks your stock files by SHA-256 and refuses any other version.
- **No AnyTone firmware is published here.** A release is a patch: you download the stock package from AnyTone's
  distributor yourself, and Codeplug Studio turns it into the modded firmware on your own computer.
- **A firmware write does not touch your codeplug.** Channels, zones, contacts, settings and the factory calibration
  live in a separate memory chip that a firmware write does not reach. Save your codeplug with the CPS before your
  first write anyway.
- **Keep a way back.** Keep the stock V1.05 zip. As long as the radio enters update mode, stock can be put back with
  Codeplug Studio or the official CPS ([back-to-stock.md](back-to-stock.md)).
- **Release candidates** (versions ending `-rc.N`) are for testing. They have passed the project's emulator tests but
  may not have been checked on a radio yet. Use a final release unless you want to help test.

## What you need

| Item | Why |
|---|---|
| An AT-D890UV on stock V1.05, or on an earlier release of these mods | The radio |
| A desktop computer with Chrome or Edge | Codeplug Studio flashes over Web Serial, which those browsers support |
| A good USB data cable, plugged straight into the computer (no hub) | The write takes under a minute and must not be interrupted |
| A full battery | Same reason |
| The stock V1.05 zip | The patch is applied to it, and it is your way back |
| The official AnyTone CPS (Windows), optional | To assign keys to the mods, save your codeplug, and as a second way back to stock |

## Getting help

Open an issue on the [public repository](https://github.com/pskillen/mm9pdy-firmware/issues/new/choose). Say which
release you used, what the screen and the red LED showed, and what Codeplug Studio said. Do not attach a radio
backup or a codeplug: they hold your radio's serial number, your DMR ID and possibly encryption keys.
