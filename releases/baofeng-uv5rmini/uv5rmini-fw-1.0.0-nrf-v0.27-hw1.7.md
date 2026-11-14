---
version: 1.0.0
channel: final
stock: v0.27 (NRF)
base: nrf-v0.27
published: 2026-11-14
summary: MM9PDY 1.0.0 for the UV-5R Mini, NRF, firmware V0.27, hardware V1.7. Zones, zone scan and the build name in Radio Info.
verify: After the radio restarts, Menu > Radio Info shows "mm9pdy-L2-1.0.0" on its fourth row.
---

The first release of the MM9PDY firmware for the UV-5R Mini. It is only for radios that show `5RMINI NRF` on the hold-8 power-on screen and `Firmware:V0.27` and `Hardware:V1.7` in Radio Info. A radio with any other combination is not supported, and Codeplug Studio writes nothing to it.

**What's new**

- **Zones:** up to 24 named groups of channels, written with the codeplug. Each side chooses its own zone from the menu (MENU, then UP to **Zones A** or **Zones B**), and Up and Down then step only through that zone's channels. Typing a channel number still reaches any channel.
- **Zone line:** in NAME display mode, the idle screen shows each side's zone in small letters under the channel name.
- **Zone scan:** a scan in a zone visits only that zone's channels: those with SCAN ADD on, or all of them when none has it.
- **Build name:** the power-on screen and the fourth row of Radio Info show the build name.
- A codeplug with no zones works exactly as the stock firmware does.

**How far it has been checked:** the release candidate was installed through Codeplug Studio once. On a radio, both sides kept their zones and channels over a power cycle; the zone line and zone scan were checked. Carrier scan resumed almost always after 5 seconds. Studio stopped for unsupported radio answers. A full read matched that radio's calibration reference; no writes followed that read during the sitting. Other zone checks, back to stock, recovery and writing the same build again were not checked at the sitting.

**Checking it worked:** after the radio restarts, Menu > Radio Info shows `mm9pdy-L2-1.0.0` on its fourth row. The Firmware and Hardware rows are unchanged.

**Going back to stock:** use **Back to stock** in Codeplug Studio's firmware flasher, with the to-stock file published with this release and your stock firmware file. It is meant for emergencies.
