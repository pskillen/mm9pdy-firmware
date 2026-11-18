# MM9PDY modded firmware

New features for radios you already own. Each release is the manufacturer's own firmware with a few carefully tested
features added. Everything else behaves as stock. You install it from the browser with
[Codeplug Studio](https://codeplug.mm9pdy.net), and you can put stock back the same way. It is free.

| Radio | Stock firmware a release fits | User guide | Releases |
|---|---|---|---|
| AnyTone AT-D890UV | V1.05 (20260521) | [docs/anytone-at-d890uv](docs/anytone-at-d890uv/README.md) | [releases/anytone-at-d890uv](releases/anytone-at-d890uv) |
| Baofeng DM-32UV | v1.01.048 | [docs/baofeng-dm32uv](docs/baofeng-dm32uv/README.md) | [releases/baofeng-dm32uv](releases/baofeng-dm32uv) |
| Baofeng UV-5R Mini | V0.27 (NRF) or V0.04 (NRFB), Hardware V1.7 | [docs/baofeng-uv5rmini](docs/baofeng-uv5rmini/README.md) | [releases/baofeng-uv5rmini](releases/baofeng-uv5rmini) |
| Retevis RT95 front panel (LCD) | LCD V1.41 (20231202) | [docs/retevis-rt95-head](docs/retevis-rt95-head/README.md) | [releases/retevis-rt95-head](releases/retevis-rt95-head) |
| Retevis RT95 main board (RF CPU), for the audio level meter | MAIN V1.61 (20231202) | [docs/retevis-rt95-head](docs/retevis-rt95-head/install.md) | [releases/retevis-rt95-main](releases/retevis-rt95-main) |

A release fits only the stock firmware in the table. Codeplug Studio checks your stock firmware file and stops before
writing anything that does not match. Each user guide says how to read your radio's version.

## What you get

### AnyTone AT-D890UV

DMR handheld. Pick who you talk to without reprogramming.

- **[Independent talk groups](docs/anytone-at-d890uv/features.md#2-independent-talk-groups):** program a repeater
  once, step through its talk groups with two keys, and answer a call with **Reply**.
- **[Star-key timeslot](docs/anytone-at-d890uv/features.md#3-star-key-timeslot-toggle) and
  [zone scan](docs/anytone-at-d890uv/features.md#4-zone-scan):** a short `*` swaps TS1 and TS2; scan walks the zone
  you are in, with a popup that lets you switch to the talk group you just heard.
- **[S-meter](docs/anytone-at-d890uv/features.md#10-s-meter) and
  [quick filters](docs/anytone-at-d890uv/features.md#5-quick-filters-menu):** a signal bar, a signal screen, a
  spectrum and a signal history; receive filters one key press away.
- **[FM squelch keys](docs/anytone-at-d890uv/features.md#fm-squelch-on-the-same-keys),
  [Bluetooth headset volume](docs/anytone-at-d890uv/features.md#9-bluetooth-headset-volume-and-microphone) and
  [NXDN](docs/anytone-at-d890uv/nxdn.md)** (open beta): the radio's own NXDN mode, which AnyTone has not released.

### Baofeng DM-32UV

DMR handheld. Zones and talk groups from the front panel.

- **[Zone scan](docs/baofeng-dm32uv/features.md#1-zone-scan):** scan on a channel with no scan list walks its whole
  zone, up to 64 channels.
- **[Independent talk groups](docs/baofeng-dm32uv/features.md#6-independent-talk-groups):** two keys step through the
  channel's RX group list, and the screen shows who PTT will call.
- **[Star-key timeslot](docs/baofeng-dm32uv/features.md#7-star-key-timeslot):** a short `*` swaps TS1 and TS2, with
  a [TS1 / TS2 badge](docs/baofeng-dm32uv/features.md#8-timeslot-indicator) next to `DIG`.
- **[Light mode](docs/baofeng-dm32uv/features.md#2-quick-menu-and-light-mode):** a quick menu on a key turns the screen
  light with dark text, easier to read in daylight.

### Baofeng UV-5R Mini

Small analogue handheld. Zones, and a centre button that does what you choose. Each feature has its own page, listed
under [what it does](docs/baofeng-uv5rmini/README.md#what-it-does).

- **Zones:** up to 24 named zones, one per side. Up and Down follow the zone's own channel order, and each zone scans
  its own channels.
- **Nuisance delete:** hold the side key while a scan is stopped to skip that channel.
- **Centre button:** choose what a tap and a hold do. The flashlight now switches on and off.
- **Quick Access and watch modes:** scan, light, monitor and the watch mode in one short list; Single watch shows one
  channel in big digits.
- **[First install from a stock radio](docs/baofeng-uv5rmini/install.md)** in Codeplug Studio, with the radio's
  programming cable.

### Retevis RT95 (also sold as the AnyTone AT-778UV)

Mobile radio. The mods change the front panel; an optional radio board (RF CPU) update adds the audio level meter.

- **[Zones](docs/retevis-rt95-head/features.md#zones):** up to 32 named zones, picked with a key. The knob, the mic's
  Up and Down and scan follow the zone's own channel order, each zone can have its own scan set, and switching zone
  returns to the channel you last used there.
- **[Channel descriptions](docs/retevis-rt95-head/features.md#channel-descriptions):** in single watch, a
  12-character description under the channel name, with the zone above it.
- **[Nuisance delete](docs/retevis-rt95-head/features.md#nuisance-delete-in-scan) and
  [Scan Pause Time](docs/retevis-rt95-head/features.md#co-scan-and-scan-pause-time):** hold SCN to skip a busy
  channel until you switch off; carrier scan waits the pause time after the signal goes.
- **[Audio level meter](docs/retevis-rt95-head/features.md#audio-level-meter):** received audio and your microphone
  level as nine segments in single watch; needs the radio board update.

Each user guide says what every feature does, its limits, and how far it has been checked on a radio.

## Installing

Use the firmware flasher in [Codeplug Studio](https://codeplug.mm9pdy.net) (**Tools > Firmware flasher**, in Chrome
or Edge on a desktop computer). It lists every release published here, shows the release notes, checks your stock
firmware, builds the modded firmware on your computer and writes it to the radio. Step by step:
[AT-D890UV](docs/anytone-at-d890uv/install.md), [DM-32UV](docs/baofeng-dm32uv/install.md),
[UV-5R Mini](docs/baofeng-uv5rmini/install.md), [RT95](docs/retevis-rt95-head/install.md).

**Flashing firmware can brick a radio.** Everything here is at your own risk, with no warranty of any kind. Read your
radio's docs, especially going back to stock and recovery, before your first write.

## What is in this repository

| Path | What it is |
|---|---|
| [releases/](releases) | One folder per radio. Each release is a `.patch.json` and a `.md` file with the same name: the release notes, with a short header (version, channel, stock version, date, summary, how to check it worked). A radio whose builds depend on the exact stock firmware has one release per stock base, with the base in the file name |
| `releases/<radio>/to-stock/` | For such a radio, the patch back to each stock base, one per base and version, listed alongside its release when available |
| [releases.json](releases.json) | Index of every release, generated from `releases/`. This is what Codeplug Studio reads |
| [docs/](docs) | The user guide for each radio |
| [tools/release_index.py](tools/release_index.py) | Builds and checks the index, and publishes a release |

**No manufacturer firmware is published here.** A release is a patch: you supply the stock firmware yourself, and the
patch turns it into the modded firmware. Baofeng does not publish the Mini's stock file; Codeplug Studio links an
unofficial third-party copy and checks it. The patch records the SHA-256 of the stock files it needs and of the result,
so it cannot be applied to anything else, and the result is checked before anything reaches the radio.

**Release candidates** (versions ending `-rc.N`) are test builds. They have passed the project's emulator tests, but
may not have been checked on a radio yet. Codeplug Studio lists them only when you ask it to. While a release candidate
is in testing, its docs are in `docs/rc/<radio>/`; `docs/<radio>/` always describes the current release.

## Release index format

`releases.json` has `format: 1` and a `releases` array. Each row has `radioId`, `version`, `channel`, `patchName`,
`patchFile`, `patchPath`, `patchSha256`, `stockVersion`, `publishedOn`, `summary`, `verifyHint`, `resultSha256`
(result hashes by file role), `notesPath` and `notes`. Radios with stock bases also have `layout` and `base`.
When a matching patch back to stock exists, the row has `toStock`, an object with its repository-relative `path`
and the `sha256` of its file bytes. Paths are relative to the repository root.

## Reporting problems and asking for features

Open an issue: [bug report](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=bug.yml) or
[feature request](https://github.com/pskillen/mm9pdy-firmware/issues/new?template=feature.yml). Never attach a radio
backup or a codeplug: they hold your radio's calibration, your DMR ID and possibly encryption keys.

The firmware is developed in private repositories. This repository is published from them on each release, so pull
requests that change `docs/` or `releases/` cannot be merged here; please open an issue instead.

## Licence

Docs and release notes: CC BY-SA 4.0. Release patches: free to use and redistribute unmodified. Tools: MIT. No
warranty of any kind. Details in [LICENSE.md](LICENSE.md).
