---
version: 1.0.0
channel: final
stock: v1.01.048
published: 2026-10-20
summary: Zone scan on channels without a scan list, a quick menu with light mode, position-report retry, a GPS padding fix and menu text fixes.
verify: Press Scan on a channel with no scan list: a zone scan should start. Device information still reads DM32.01.L01.048; that is expected.
---

The first full release of the DM-32UV firmware mods. It applies to stock firmware **v1.01.048** only.

Everything not listed here behaves exactly as stock. The codeplug format is unchanged, so the official CPS and Codeplug
Studio read and write the radio as before, and the radio keeps its channels and settings across the update.

**What's in it**

- **Zone scan:** pressing Scan on a channel with no scan list scans the whole current zone (up to 64 channels) instead
  of refusing. While it walks, the screen shows the zone name and `Scanning...`. It resumes about 5 s after a signal
  ends. Channels with a scan list scan it exactly as stock. Tested on the radio.
- **Quick menu and light mode:** assign the stock **Flashlight** key function to a free programmable key (SK1, SK2 or
  P1; avoid P2). It opens a small menu with one row, **Light mode**, which inverts the screen for easier reading in
  daylight. The choice is saved across power-off. Tested on the radio.
- **Position report retry:** a timed position report now waits for a GPS fix instead of being skipped until the next
  interval, so a 300 s interval actually sends. Tested on the radio.
- **GPS position padding fix:** Fixed Beacon position reports keep leading zeros in latitude and longitude, so APRS
  gateways can read them. A community fix (IU2VTP). Emulator and byte checks only.
- **Text fixes:** eleven English typos and wording fixes in menus and pop-ups, for example "VerSions" → "Versions" and
  "Nonsupport" → "Unsupported". Checked byte for byte; not every screen has been looked at on the radio.

**Known limits:** nuisance delete during a zone scan is untested, and the zone-scan hang time is fixed at about 5 s.

**Checking it worked:** the radio does not show the mod's version yet. Device information still reads
`DM32.01.L01.048`. Check that Scan on a channel with no scan list starts a zone scan.

**Going back to stock:** flash stock v1.01.048 from this page, or use the official CPS.
