---
version: 1.1.0
channel: final
stock: LCD V1.41 (20231202)
published: 2026-10-29
summary: Zones, channel descriptions and a tidier single-watch screen.
verify: The bottom of the power-on screen shows "MM9PDY-1.1.0".
---

Release 1.1.0 of the Retevis RT95 front-panel modification. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only, and leaves the radio board's firmware alone.

**How far it has been checked:** this build has been checked in an emulator. A test build of the same code (it differs only in the version line) was written to a radio with Codeplug Studio and used with zones and descriptions before this release was made. There was no separate release candidate.

**What's new**

- **Zones:** group your channels into up to 32 named zones in Codeplug Studio, with the *Retevis RT95 VOX (MM9PDY modded firmware)* target. A programmable key set to DIR shows `ZON` and opens the zone selector. The knob, the microphone's Up and Down keys and scan stay inside the zone. Each side keeps its own zone, and the radio remembers it when switched off. Studio can set the key for you ("Put Zone on a P-key").
- **Channel descriptions:** a short description per channel (up to 12 characters, from the channel's Name in Studio) shows under the channel name in single watch.
- **Single-watch screen:** the main side is drawn where it sits in dual watch, so the zone name (sky blue) and the description (amber) fit underneath. Dual watch is unchanged.

**Known issues** (to be fixed in 1.1.1)

- In the zone selector, some zone names run past the end of the box and leave a few pixels on the screen near the P6 label. Some names flicker and are not drawn.
- Switching zone stays on the current channel if it also belongs to the new zone, instead of going to the channel you last used in that zone.
- The channel number shown is the radio's own number, not the channel's place in the zone.

**Known limits**

- Screen flip stays in the radio's FUNC menu (DIR). A key set to DIR opens zones instead.
- A description is hidden once the channel has been changed on the radio or with another programming tool. Write again from Studio to bring it back.
- Without zone data from Studio, the radio behaves as before, with all channels.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.1.0`.

**Going back:** write release 1.0.0-rc.2, or the maker's stock front-panel firmware (LCD V1.41), with Codeplug Studio.
