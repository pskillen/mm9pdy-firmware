---
version: 1.1.0
channel: final
stock: v0.27 (NRF)
base: nrf-v0.27
published: 2026-11-18
summary: MM9PDY 1.1.0 for the UV-5R Mini, hardware V1.7, NRF with firmware V0.27 or NRFB with firmware V0.04. Zone scan lists and order, nuisance delete, a programmable centre button, Quick Access and three watch modes.
verify: After the radio restarts, Menu > Radio Info shows "MM9PDY mod" then "v0.27-NRF-1.1.0" (on a V0.04 radio, "v0.04-NRFB-1.1.0").
---

There are two files. `v0.27-NRF-1.1.0` is for radios that show `5RMINI NRF` on the hold-8 power-on screen and `Firmware:V0.27` and `Hardware:V1.7` in Radio Info. `v0.04-NRFB-1.1.0` is for radios that show `5RMINI NRFB`, `Firmware:V0.04` and `Hardware:V1.7`. Both files do the same things. Codeplug Studio 2.14.0 or later is needed to install it.

**What's new**

- **Each zone scans its own channels:** the channels marked **Scan in this zone** in Codeplug Studio. With an older codeplug, a zone scans its channels with SCAN ADD on, as before.
- **Zones keep their order:** Up, Down, scan and choosing a zone follow the channel order set for the zone in Studio, not channel-number order.
- **Nuisance delete:** while a scan is stopped on a channel, hold the side key (SK1) to skip that channel until the radio is switched off.
- **Centre button:** a tap and a hold of the blue button each do something you choose (Radio Set > PRESS SK2 and HOLD SK2). Out of the box, a tap switches the flashlight and a hold starts Seek. The flashlight now switches on and off and no longer flashes.
- **Quick Access:** the last item of the menu, and an option for the centre button. It lists Scan, Light, Monitor and the watch mode. The list stays open after Light and the watch mode; Scan and Monitor close it.
- **Watch modes:** Radio Set > Watch Mode replaces Dual Watch. **Single** shows one channel, with its frequency in big digits, and both PTT buttons transmit on it. **Dual Watch** and **Dual Monitor** are the maker's Dual Watch OFF and ON.
- **Safer updates:** when the radio refuses a file meant for the other firmware version, it keeps its settings, and it refuses an image too large for it without erasing anything.
- **V0.27 radios:** the power-on screen and Radio Info show the `MM9PDY mod` line above the build name, as V0.04 radios already do.
- **Simpler first install:** on a stock radio, Studio asks only the suffix and the Hardware line, no longer the Firmware line.

**How far it has been checked:** everything passes in an emulator, on both firmware versions. On a radio, its release candidate was installed through Codeplug Studio 2.14.0 over earlier MM9PDY builds, on a V0.04 and a V0.27 radio, and its features were used on both, including the watch modes and Quick Access staying open. Earlier test builds were checked on a radio for zone order, nuisance delete, the centre button and flashlight, and Quick Access. Not checked on a radio with this release: installing over stock firmware, back to stock and recovery.

**Checking it worked:** after the radio restarts, Menu > Radio Info shows `MM9PDY mod` then `v0.27-NRF-1.1.0` (on a V0.04 radio, `v0.04-NRFB-1.1.0`). The Firmware and Hardware rows are unchanged.

**Going back to stock:** use **Back to stock** in Codeplug Studio's firmware flasher, with the to-stock file published with this release and your stock firmware file. It is meant for emergencies.
