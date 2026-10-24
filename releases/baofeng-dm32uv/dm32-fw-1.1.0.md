---
version: 1.1.0
channel: final
stock: v1.01.048
published: 2026-10-22
summary: Talk-group keys that step through the RX group list, the PTT contact on screen, a star-key timeslot swap with a TS1/TS2 badge, a timeslot from a talk-group name suffix, and the mod version in Device Info.
verify: Settings > Device Info > Versions shows "mm9pdy-1.1.0" under DM32.01.L01.048.
---

The 1.1.0 release of the DM-32UV firmware mods. It applies to stock firmware **v1.01.048** only. It is about DMR: change who you're talking to and which timeslot you're on from the front panel. Everything in 1.0.0 is also in this build.

The codeplug format is unchanged, so the official CPS and Codeplug Studio read and write the radio as before, and the radio keeps its channels and settings across the update.

**How far it has been checked:** every feature passes the emulator test suite, and the release was checked on the owner's radio before it shipped. The full on-air checklist (which slot actually goes out, for example) is still open.

**What's new since 1.0.0**

- **Talk groups without reprogramming:** assign two keys to **Previous Record** and **Next Record** in the CPS (the radio lists them as **TG Prev** and **TG Next**). On a digital channel with an RX group list they step through its members, and PTT calls the one you picked. Nothing is saved: power off and every channel is back to its own contact.
- **See who you're calling:** on a digital channel, the line under the channel name shows the contact PTT will call instead of the frequency.
- **Star-key timeslot swap:** a short press of `*` on a digital repeater channel swaps between TS1 and TS2 until you change channel, step talk group or power off. On analogue channels `*` still toggles NOAA weather.
- **Timeslot badge:** `TS1` or `TS2` next to the `DIG` badge, showing the slot the radio is actually using.
- **Timeslot from a talk-group name:** a contact named, for example, `Scotland TS2` switches to that slot when you step to it. The name is shown without the suffix.
- **Mod version:** `mm9pdy-1.1.0` at the bottom of the boot screen and under Settings > Device Info > Versions.

**Known limits**

- While scanning, the second line shows the frequency, not a talk-group name.
- After a channel change, the frequency can flash for a moment before the contact name appears.
- A contact name that happens to end in `ts1` or `ts2` sets the slot; there is no switch to turn that off.
- In dual watch with both sides on the same channel, a star-key swap can sometimes outlive a channel change on one side.

**Checking it worked:** Settings > Device Info > Versions shows `mm9pdy-1.1.0` under Baofeng's `DM32.01.L01.048`.

**Going back to stock:** flash stock v1.01.048 from this page, or use the official CPS.
