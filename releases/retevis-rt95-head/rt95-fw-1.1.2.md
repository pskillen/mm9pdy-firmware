---
version: 1.1.2
channel: final
stock: LCD V1.41 (20231202)
published: 2026-10-30
summary: Carrier scan now waits the Scan Pause Time after the signal goes before it moves on.
verify: The bottom of the power-on screen shows "MM9PDY-1.1.2".
---

Release 1.1.2 of the Retevis RT95 front-panel modification. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only, and leaves the radio board's firmware alone. Everything in 1.1.1 is unchanged apart from the change below.

**How far it has been checked:** this build has been checked in an emulator. A test build of the same change was written to a radio with Codeplug Studio and carrier scan was timed on it with the 5 second Scan Pause Time: it waited about 5 seconds. The 10 and 15 second settings and VFO scan have not been timed on a radio. There was no separate release candidate.

**What's new**

- **Carrier scan waits the Scan Pause Time.** With the scan type set to CO, the scan holds while a signal is there. On the stock firmware it then moved on after about a quarter of a second; now it waits the Scan Pause Time you set in the menu (5, 10 or 15 seconds), and starts that wait again if the signal comes back. Time-operated and search scan work as before. Nothing new appears in the menu, and your codeplug is unchanged.

**Known issues** (still open, to be fixed in a later release)

- In the zone selector, some zone names run past the end of the box and leave a few pixels on the screen near the P6 label. Some names flicker and are not drawn.
- Switching zone stays on the current channel if it also belongs to the new zone, instead of going to the channel you last used in that zone.
- The channel number shown is the radio's own number, not the channel's place in the zone.

**Known limits**

- Screen flip stays in the radio's FUNC menu (DIR). A key set to DIR opens zones instead.
- A description is hidden once the channel has been changed on the radio or with another programming tool. Write again from Studio to bring it back.
- Without zone data from Studio, the radio behaves as before, with all channels.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.1.2`.

**Going back:** write release 1.1.1, or the maker's stock front-panel firmware (LCD V1.41), with Codeplug Studio.
