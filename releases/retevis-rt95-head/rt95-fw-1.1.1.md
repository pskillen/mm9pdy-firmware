---
version: 1.1.1
channel: final
stock: LCD V1.41 (20231202)
published: 2026-10-29
summary: Fixes the radio's menus freezing the screen and keys.
verify: The bottom of the power-on screen shows "MM9PDY-1.1.1".
---

Release 1.1.1 of the Retevis RT95 front-panel modification. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only, and leaves the radio board's firmware alone. Everything in 1.1.0 is unchanged apart from the fix below.

**How far it has been checked:** this build has been checked in an emulator, including a new test that opens the FUNC menu and goes into and out of every item. A test build of the same fix was written to a radio with Codeplug Studio and the menus were used on it before this release was made. There was no separate release candidate.

**Fixed**

- **Menus froze the radio.** On 1.1.0, opening the radio's own menus (the FUNC menu, the channel menu and others) and picking an item could freeze the screen and every key, power included, until the battery or DC power was removed. Audio kept working. The menus now work as on the stock firmware.

**Known issues** (still open, to be fixed in a later release)

- In the zone selector, some zone names run past the end of the box and leave a few pixels on the screen near the P6 label. Some names flicker and are not drawn.
- Switching zone stays on the current channel if it also belongs to the new zone, instead of going to the channel you last used in that zone.
- The channel number shown is the radio's own number, not the channel's place in the zone.

**Known limits**

- Screen flip stays in the radio's FUNC menu (DIR). A key set to DIR opens zones instead.
- A description is hidden once the channel has been changed on the radio or with another programming tool. Write again from Studio to bring it back.
- Without zone data from Studio, the radio behaves as before, with all channels.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.1.1`.

**Going back:** write release 1.1.0, or the maker's stock front-panel firmware (LCD V1.41), with Codeplug Studio. Avoid 1.1.0 if you use the radio's menus.
