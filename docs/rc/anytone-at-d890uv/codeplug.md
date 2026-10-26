# Your codeplug and the mods

> **Release candidate docs: 1.2.0-rc.4** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../anytone-at-d890uv/codeplug.md).

What the mods change about your codeplug, what the CPS does and does not see, and what happens if you take the same
codeplug back to stock firmware.

The short version: **the codeplug format is not changed.** The same codeplug works on stock V1.05 and on a release.
Only three key functions (and one optional one) behave differently, and the quick filters menu keeps a few settings of its own outside the
codeplug.

## 1. Reused key functions

The mods take over three stock key functions, and a fourth, optional one: the S-meter screen. The CPS does not know about the mods, so it **keeps the stock names**.
The radio's own menu (Menu > Radio Set > Key Func, English menu language) **shows the new names**.

| CPS key list item | Name in the CPS | With a release on the radio | Name in the radio's Key Func menu |
|---|---|---|---|
| 14 | Record Switch | TG previous | TG Previous |
| 15 | Record | TG next | TG Next |
| 31 | Priority Zone | Opens the quick filters menu | Quick Filters |
| 56 | Satellite Predicting | Opens the S-meter screen (optional) | S-Meter |

The item number is the position in the CPS drop-down, counting "Off" as item 1. The radio counts from "Off" as 0, so
the same ones are numbers 13, 14, 30 and 55 inside the radio. You only need the names.

While a release is on the radio, the stock Record Switch, Record and Priority Zone functions are not available. How to
assign the keys is in [features.md](features.md), section 1.

## 2. The mods' own settings

The quick filters menu's settings (TS filter, CC match, TG slot, Tone match, and RX match TG, and the Scan menu's Scan, Scan popup and Zone scan resume rows) are not in the codeplug. The
radio keeps them in a small record of its own, in a spare part of the radio's settings memory that stock firmware
neither reads nor uses.

| Question | Answer |
|---|---|
| Where is it? | 32 bytes in a spare part of the optional-settings area of the radio's settings memory |
| Does the CPS show it? | No |
| Does the CPS write it? | No. The CPS never writes those bytes |
| Is it kept when the radio saves its settings? | Yes. Every settings save on the radio carries it along |
| What if it is empty or damaged? | The mods use their defaults. An empty record (all `FF`) means defaults |

**Your quick filters settings are kept across a CPS write.** On the test radio (1.0.0-rc.3 check), a codeplug write with the official CPS left them as
they were. A radio reset of the settings clears them, and they come back as the defaults below. Other codeplug editors
have not been checked: after a write with one, open the quick filters menu and check its rows.

Settings that stock already has stay in the codeplug as usual. Digital monitor and the monitor colour code are stock
settings: the CPS shows and writes them, and the RX match, TS filter and CC match rows follow them.

Defaults, so you know what a reset looks like:

| Row | Default |
|---|---|
| RX match | Follows the codeplug's digital monitor setting (RGL or Any). TG is off |
| TS filter | Follows the codeplug's digital monitor setting |
| CC match | Follows the codeplug's monitor colour code setting |
| Scan | Zone |
| TG slot | Auto |
| Tone | Ch |

## 3. The same codeplug on stock firmware

You can write a codeplug set up for the mods to a radio on stock V1.05, or go back to stock with it already on the
radio ([back-to-stock.md](back-to-stock.md)). Nothing breaks.

| You set in the CPS | On a release | On stock firmware |
|---|---|---|
| Record Switch (item 14) | TG previous | Stock Record Switch |
| Record (item 15) | TG next | Stock Record |
| Priority Zone (item 31) | Quick filters menu | Stock Priority Zone |
| Satellite Predicting (item 56) | S-meter screen | Stock Satellite Predicting |

You may want to reassign those keys in the CPS if you stay on stock.

The mods' settings record stays where it is. Stock firmware ignores it, and its own settings saves carry it along. If you
install a release again later, the mods should find your settings there. This is expected from how stock saves
settings, but has not been tried on the radio.

## 4. Other codeplug editors

Only the official CPS has been used with the mods. Another editor that writes the whole settings area may also reset the
quick filters settings, as in section 2.
