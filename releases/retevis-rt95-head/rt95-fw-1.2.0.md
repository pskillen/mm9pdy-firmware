---
version: 1.2.0
channel: final
stock: LCD V1.41 (20231202)
published: 2026-11-18
summary: Zones get their own scan sets and channel order, switching zone goes to the channel you last used there, a skipped scan channel stays skipped until switch-off, and an audio level meter (with the radio board update).
verify: The bottom of the power-on screen shows "MM9PDY-1.2.0".
---

Release 1.2.0 of the Retevis RT95 front-panel modification. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only. Everything in 1.1.3 is unchanged apart from the changes below. The audio level meter also needs the radio board (RF CPU) update released alongside this one; without it, the front panel works as below and the meter stays hidden.

**How far it has been checked:** every change has been checked in an emulator and used on a radio, with test builds that differ from this release only in the version line. There was no separate release candidate.

**What's new**

- **Scan sets per zone.** Each zone scans its own set of channels: the ones marked *Scan in this zone* in Codeplug Studio. A channel can be scanned in one zone and skipped in another. The **S** on the channel line follows the zone's scan set.

- **Zones keep your channel order.** The knob, the microphone's Up and Down keys and scan follow the order you gave the zone's channels in Codeplug Studio, not channel-number order. Different zones can order the same channels differently.

- **Switching zone.** The radio goes to the channel you last used in that zone (each side remembers its own, until you switch off), else the zone's first channel in your order. It no longer stays on your channel just because the new zone has it too. Switching to **All channels** keeps your channel.

- **Nuisance delete lasts until switch-off.** A channel you skip with SCN during a scan stays skipped when you stop and restart the scan, change zone or switch between memory and VFO, until you switch the radio off. A skipped channel shows a grey **S**. Editing the channel on the radio drops its skip.

- **Audio level meter.** Off by default: turn it on with **MTR**, the last item in the FUNC MENU. In single watch, the row under the signal bars shows the received audio level while receiving and your microphone level while you transmit, as nine segments. Needs the radio board (RF CPU) update.

**Codeplug Studio:** write your codeplug again with the MM9PDY target to get scan sets and zone order. Zones written by an older Studio have neither, and scan and step as in 1.1.3.

**Known limits**

- Screen flip stays in the radio's FUNC menu (DIR). A key set to DIR opens zones instead.
- A description is hidden once the channel has been changed on the radio or with another programming tool. Write again from Studio to bring it back.
- Without zone data from Studio, the radio behaves as before, with all channels.
- Skipping a channel works from the front-panel SCN key only, not from a microphone key.
- Pressing PTT during a scan transmits on the channel the scan is passing, as the stock radio does.
- For a moment after switching on, writing from Studio or deleting a channel, a zone you have not used yet may start on its lowest channel rather than its first in your order.
- Writing a codeplug with the official programming software turns MTR off.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.2.0`.

**Going back:** write release 1.1.3, or the maker's stock front-panel firmware (LCD V1.41), with Codeplug Studio. With the stock front panel the radio board update does nothing visible; you can leave it, or put the stock radio board firmware back as the user guide's back-to-stock page describes.
