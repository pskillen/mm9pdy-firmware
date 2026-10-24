---
version: 1.2.0-rc.1
channel: rc
stock: v1.01.048
published: 2026-10-23
summary: A 1.2.0 release candidate: a timeslot per RX group list member, quick-menu RX match and TS filter rows, and the distance to the channel's site from positions Codeplug Studio writes. Emulator-checked only.
verify: Settings > Device Info > Versions shows "mm9pdy-1.2.0-rc.1" under DM32.01.L01.048.
---

A release candidate for 1.2.0, for testing. It applies to stock firmware **v1.01.048** only. Everything in 1.1.0 is also in this build.

**Not yet tried on a radio:** the new items below are checked in an emulator only.

**What's new since 1.1.0**

- **Channel distance:** the zone-name row shows how far away the current memory channel's site is, and in which direction, from the radio's GPS position, for example `4.3km NE`. It needs channel positions written by Codeplug Studio's **MM9PDY** target, GNSS on and a recent fix. Power-cycle the radio after the write: it reads the positions at power-on. VFO, zone scan and channels with no position show nothing.
- **A timeslot per RX group list member:** Codeplug Studio's MM9PDY target can store a slot for each member of an RX group list. Step to that talk group with TG Prev / TG Next and the radio uses that slot. It wins over a `TS1` / `TS2` name suffix; the star key still overrides both.
- **Quick menu rows RX match and TS filter,** under Light mode. **RX match** (TG / RGL / Any) sets which group calls you hear; RGL is stock. **TS filter** (On / Off): Off also listens on the other timeslot when both are quiet; On is stock.

**Known limits**

- A 16-character zone name leaves no room for the distance, so none is shown.
- If you change an RX group list's members in another tool, such as the official CPS, the radio ignores that list's stored slots until Studio writes them again.
- TS filter Off is a test feature: PTT always goes out on the channel's own slot.
- RX match TG applies from the next call after a talk-group step. The Monitor key still opens the radio to every call.

**Checking it worked:** Settings > Device Info > Versions shows `mm9pdy-1.2.0-rc.1` under Baofeng's `DM32.01.L01.048`.

**Going back to stock:** flash stock v1.01.048 from this page, or use the official CPS.
