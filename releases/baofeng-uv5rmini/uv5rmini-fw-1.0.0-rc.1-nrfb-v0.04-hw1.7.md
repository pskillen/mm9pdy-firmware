---
version: 1.0.0-rc.1
channel: rc
stock: v0.04 (NRFB)
base: nrfb-v0.04
published: 2026-11-15
summary: A 1.0.0 release candidate, the first MM9PDY build for the UV-5R Mini. Zones for each side, the zone under the channel name, scanning inside a zone, and the build name in Radio Info.
verify: After the radio restarts, Menu > Radio Info shows "mm9pdy-L2-1.0.0-rc.1" on its fourth row (on a V0.04 radio, "MM9PDY mod" then "v0.04-NRFB-1.0.0-rc.1").
---

A release candidate for 1.0.0, for testing. The V0.27 file is only for UV-5R Mini radios that show `5RMINI NRF` on the hold-8 power-on screen and `Firmware:V0.27` and `Hardware:V1.7` in Radio Info. A radio with any other combination is not supported, and Codeplug Studio writes nothing to it.

**V0.04 radios:** a second file, `v0.04-NRFB-1.0.0-rc.1`, is for radios that show `5RMINI NRFB`, `Firmware:V0.04` and `Hardware:V1.7`. It works the same, except that the power-on screen and Radio Info show a fixed `MM9PDY mod` line above the build name. It passes in an emulator and has not yet been checked on a radio.

**What's new**

- **Zones:** up to 24 named groups of channels, written with the codeplug. Each side chooses its own zone from the menu (MENU, then UP to **Zones A** or **Zones B**), and Up and Down then step only through that zone's channels. Typing a channel number still reaches any channel.
- **Zone line:** in NAME display mode, the idle screen shows each side's zone in small letters under the channel name.
- **Zone scan:** a scan in a zone visits only that zone's channels: those with SCAN ADD on, or all of them when none has it.
- **Build name:** the power-on screen and the fourth row of Radio Info show the build name.
- A codeplug with no zones works exactly as the stock firmware does.

**How far it has been checked:** everything in this build passes in an emulator. On a radio, once, with test builds that differ only in the build name: the install from Codeplug Studio, the build name on the power-on screen and in Radio Info, and zones on both sides. Going back to stock, carrying on after a cut update, and writing the same build again have not been tried on a radio yet.

**Checking it worked:** after the radio restarts, Menu > Radio Info shows `mm9pdy-L2-1.0.0-rc.1` on its fourth row. The Firmware and Hardware rows are unchanged.

**Going back to stock:** use **Back to stock** in Codeplug Studio's firmware flasher, with the to-stock file published with this release and your stock firmware file. It is meant for emergencies.
