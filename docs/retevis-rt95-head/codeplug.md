# Your codeplug and zones

Zones are part of what Codeplug Studio's MM9PDY target writes to the radio, next to your channels. This page says what that
means for the programs you already use.

| | |
|---|---|
| The key | In the official CPS the key function still says **DIR**. With this firmware the radio shows it as **ZON** (soft key) and **ZONE** (popup). The screen flip stays in the radio's own FUNC MENU, under DIR |
| Writing zones | Zones are written by Codeplug Studio's MM9PDY target. The official CPS and CHIRP never write them and never remove them |
| Zone order | Zones keep the order you give their channels in Codeplug Studio. Different zones can order the same channels differently. Switching to a zone starts on its first channel in that order, unless you used another of its channels last. Not yet checked on a radio |
| Reading and writing with the CPS or CHIRP | A read and a write of your channels works as before and leaves the zones alone |
| Editing channels | Zones follow channel numbers. If you move, retune or delete a channel with another program, check your zones in Codeplug Studio afterwards, and write again from Studio |
| A full reset of the radio | Removes your channels, so the zones are empty (all channels) until you write them again |
| An older firmware | A radio with the maker's firmware keeps the zone data but does not use it. A previous release of this firmware keeps its zones too, ignores the scan sets and order Studio writes, and scans and steps in channel-number order as it did |
| Scan in this zone | Codeplug Studio's MM9PDY target gives each member of a zone *Scan in this zone* (include or skip; include by default). The radio scans a zone by that set |
| Scan in All channels | Each channel's own scan flag. Studio, the official CPS and CHIRP all set it, and the radio's menu does. It is used only in All channels. The official CPS and CHIRP see only this setting |
| Zones from an older Codeplug Studio | They have no scan sets or zone order, so they scan by *Scan in All channels* and step in channel-number order, as before. Zone order is not yet checked on a radio. Write again from a Studio with scan sets to change that |

**Writing from Codeplug Studio.** Studio writes the zones after your channels. When the write ends the radio loads them
by itself, without switching off. If you write again straight away, Studio waits and retries for a few seconds; that is
normal.
