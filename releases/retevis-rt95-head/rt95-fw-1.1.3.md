---
version: 1.1.3
channel: final
stock: LCD V1.41 (20231202)
published: 2026-11-04
summary: Hold SCN while a scan is stopped on a channel to skip that channel until the next scan.
verify: The bottom of the power-on screen shows "MM9PDY-1.1.3".
---

Release 1.1.3 of the Retevis RT95 front-panel modification. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only, and leaves the radio board's firmware alone. Everything in 1.1.2 is unchanged apart from the change below.

**How far it has been checked:** both changes have been checked in an emulator and tried once on a radio, with a test build that differs from this release only in the version line. On the radio, skipping a channel worked, and long zone names showed cut to fit inside the box, with nothing left beside it and no blank box.

**What's new**

- **Nuisance delete in scan.** While a scan is stopped on a channel, hold SCN for about a second to skip that channel until you start the next scan. The SCN key on the screen reads NUI while the scan is stopped on a channel. Nothing in your codeplug changes.

- **Long zone names fit.** The zone selector shows the zone name by itself, without `ZONE:`, so more of it fits. A name still too wide for the box is cut to fit (a twelve-character name of wide letters shows its first seven), instead of running past the box, leaving marks by the P6 label, or flickering and not being drawn. The zone line on the single-watch screen is cut the same way when a name is too wide for it. Zone names can be up to 12 characters.

**Known issues** (still open, to be fixed in a later release)

- Switching zone stays on the current channel if it also belongs to the new zone, instead of going to the channel you last used in that zone.
- The channel number shown is the radio's own number, not the channel's place in the zone.

**Known limits**

- Screen flip stays in the radio's FUNC menu (DIR). A key set to DIR opens zones instead.
- A description is hidden once the channel has been changed on the radio or with another programming tool. Write again from Studio to bring it back.
- Without zone data from Studio, the radio behaves as before, with all channels.
- Skipping a channel works from the front-panel SCN key only, not from a microphone key.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.1.3`.

**Going back:** write release 1.1.2, or the maker's stock front-panel firmware (LCD V1.41), with Codeplug Studio.
