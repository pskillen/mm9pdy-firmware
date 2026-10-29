# MM9PDY modded firmware

Small, carefully tested changes to the stock firmware of two DMR handhelds and the Retevis RT95 mobile. Each one is the
manufacturer's own firmware with a few features added: independent talk groups, a star-key timeslot swap, zone scan,
quick menus, named zones and channel descriptions on the RT95, and more. Everything else behaves as stock, and the
codeplug format is unchanged.

| Radio | Stock base | User guide | Releases |
|---|---|---|---|
| AnyTone AT-D890UV | V1.05 (20260521) | [docs/anytone-at-d890uv](docs/anytone-at-d890uv/README.md) | [releases/anytone-at-d890uv](releases/anytone-at-d890uv) |
| Baofeng DM-32UV | v1.01.048 | [docs/baofeng-dm32uv](docs/baofeng-dm32uv/README.md) | [releases/baofeng-dm32uv](releases/baofeng-dm32uv) |
| Retevis RT95 front panel (LCD) | LCD V1.41 (20231202) | [docs/retevis-rt95-head](docs/retevis-rt95-head/README.md) | [releases/retevis-rt95-head](releases/retevis-rt95-head) |

**Retevis RT95** (also sold as the AnyTone AT-778UV): latest 1.1.1. It changes the front panel only; the radio board's
firmware stays as the maker made it. Features: up to 32 named zones, written with Codeplug Studio's *Retevis RT95 VOX
(MM9PDY modded firmware)* target and opened with a key set to DIR (the radio shows ZON), and 12-character channel
descriptions shown under the channel name in single watch. Read the revision and serial-number notes in the
[user guide](docs/retevis-rt95-head/README.md) before you flash.

## Installing

Use the firmware flasher in [Codeplug Studio](https://codeplug.mm9pdy.net) (**Tools > Firmware flasher**, in Chrome
or Edge on a desktop computer). It lists every release published here, shows the release notes, checks your stock
firmware, builds the modded firmware on your computer and writes it to the radio. Step by step:
[AT-D890UV](docs/anytone-at-d890uv/install.md), [DM-32UV](docs/baofeng-dm32uv/install.md),
[RT95](docs/retevis-rt95-head/install.md).

**Flashing firmware can brick a radio.** Everything here is at your own risk, with no warranty of any kind. Read your
radio's docs, especially going back to stock and recovery, before your first write.

## What is in this repository

| Path | What it is |
|---|---|
| [releases/](releases) | One folder per radio. Each release is a `.patch.json` and a `.md` file with the same name: the release notes, with a short header (version, channel, stock version, date, summary, how to check it worked) |
| [releases.json](releases.json) | Index of every release, generated from `releases/`. This is what Codeplug Studio reads |
| [docs/](docs) | The user guide for each radio |
| [tools/release_index.py](tools/release_index.py) | Builds and checks the index, and publishes a release |

**No manufacturer firmware is published here.** A release is a patch: you download the stock firmware from the
manufacturer yourself, and the patch turns it into the modded firmware. The patch records the SHA-256 of the stock
files it needs and of the result, so it cannot be applied to anything else, and the result is checked before anything
reaches the radio.

**Release candidates** (versions ending `-rc.N`) are test builds. They have passed the project's emulator tests, but
may not have been checked on a radio yet. Codeplug Studio lists them only when you ask it to. While a release candidate
is in testing, its docs are in `docs/rc/<radio>/`; `docs/<radio>/` always describes the current release.

## Reporting problems and asking for features

Open an issue: [bug report](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=bug.yml) or
[feature request](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=feature.yml). Never attach a radio
backup or a codeplug: they hold your radio's calibration, your DMR ID and possibly encryption keys.

The firmware is developed in private repositories. This repository is published from them on each release, so pull
requests that change `docs/` or `releases/` cannot be merged here; please open an issue instead.

## Licence

Docs and release notes: CC BY-SA 4.0. Release patches: free to use and redistribute unmodified. Tools: MIT. No
warranty of any kind. Details in [LICENSE.md](LICENSE.md).
