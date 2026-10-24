# MM9PDY modded firmware

Small, carefully tested changes to the stock firmware of two DMR handhelds. Each one is the manufacturer's own
firmware with a few features added: independent talk groups, a star-key timeslot swap, zone scan, quick menus and more.
Everything else behaves as stock, and the codeplug format is unchanged.

| Radio | Stock base | User guide | Releases |
|---|---|---|---|
| AnyTone AT-D890UV | V1.05 (20260521) | [docs/anytone-at-d890uv](docs/anytone-at-d890uv/README.md) | [releases/anytone-at-d890uv](releases/anytone-at-d890uv) |
| Baofeng DM-32UV | v1.01.048 | [docs/baofeng-dm32uv](docs/baofeng-dm32uv/README.md) | [releases/baofeng-dm32uv](releases/baofeng-dm32uv) |

## Installing

Use the firmware flasher in [Codeplug Studio](https://codeplug.mm9pdy.net) (**Tools > Firmware flasher**, in Chrome
or Edge on a desktop computer). It lists every release published here, shows the release notes, checks your stock
firmware, builds the modded firmware on your computer and writes it to the radio. Step by step:
[AT-D890UV](docs/anytone-at-d890uv/install.md), [DM-32UV](docs/baofeng-dm32uv/install.md).

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
may not have been checked on a radio yet. Codeplug Studio lists them only when you ask it to.

## Reporting problems and asking for features

Open an issue: [bug report](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=bug.yml) or
[feature request](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=feature.yml). Never attach a radio
backup or a codeplug: they hold your radio's calibration, your DMR ID and possibly encryption keys.

The firmware is developed in private repositories. This repository is published from them on each release, so pull
requests that change `docs/` or `releases/` cannot be merged here; please open an issue instead.
