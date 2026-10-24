# Features

What the modified firmware does on the radio. The table says which release added each feature; what each release
contains, and how far it was checked, is in its release notes (Codeplug Studio shows them when you pick a release).
Everything not listed here behaves exactly as stock v1.01.048: the codeplug format is unchanged, so the official CPS and
Codeplug Studio read and write the radio as before, and the radio keeps its channels and settings across the update.

| Feature | In short | Tested on a radio? |
|---|---|---|
| [Zone scan](#1-zone-scan) | Scan on a channel with no scan list scans the whole current zone | Yes (rc.1, rc.3): the zone-name display and the 5 s resume were checked on rc.3 |
| [Quick menu and light mode](#2-quick-menu-and-light-mode) | A key opens a small menu; its one row switches the screen to a light (inverted) look, saved across power-off | Yes (rc.1) |
| [Text fixes](#3-text-fixes) | Eleven English typos and wording fixes in menus and pop-ups | Built and checked byte for byte; the screens were not each looked at on the radio |
| [GPS position padding fix](#4-gps-position-padding-fix) | Fixed Beacon position reports keep leading zeros in latitude and longitude | Emulator and byte checks only |
| [Position report retry](#5-position-report-retry) | A timed position report waits for a GPS fix instead of being skipped until the next interval | Yes (rc.2): reports kept going every 300 s |
| [Independent talk groups](#6-independent-talk-groups) (1.1.0) | On a digital channel, the line under the channel name shows the contact PTT calls (not the frequency); two keys step through its RX list and PTT calls the one you stopped on | Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open |
| [Star key timeslot](#7-star-key-timeslot) (1.1.0) | Short `*` swaps a digital repeater channel between TS1 and TS2 until you change channel or power off | Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open |
| [Timeslot indicator](#8-timeslot-indicator) (1.1.0) | `TS1` or `TS2` next to the `DIG` badge on each digital channel, showing the slot it uses | Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open |
| [Timeslot from the talk-group name](#9-timeslot-from-the-talk-group-name) (1.1.0) | A talk group named `... TS1` or `... TS2` puts the channel on that slot while it is selected | Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open |
| [Version display](#10-which-version-is-installed) (1.1.0) | `mm9pdy-<version>` on the boot screen and on Settings > Device Info > Versions, under Baofeng's `DM32.01.L01.048` | Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open |

The known limits of the 1.1.0 features are collected in [section 11](#11-known-limits-in-110).

## 1. Zone scan

**What it does.** On stock firmware, pressing Scan on a channel with no scan list does nothing useful (the radio
refuses). With this firmware it scans **the channel's current zone** instead: every channel in the zone, up to 64,
starting from the current position and wrapping at the end. A stock scan list holds at most 16 entries (in practice
15 named channels), so zone scan is also the way to scan more than 15 channels.

A channel that **has** a scan list scans that list exactly as stock does. Nothing about list scans changed.

**How to use it.**

1. In the CPS or Codeplug Studio, leave the channel's scan list set to none (or simply never set one).
2. Start a scan the usual way: a key programmed with the stock **Scan** function, or the stock menu entry "Scan Switch".
   There is no new key and no new setting.
3. Stop it the same way as a stock scan.

**What the screen shows.** While a zone scan is walking, the big name line
(normally the channel name) shows **the zone name**, and the line under it (normally the zone name) reads
**`Scanning...`**. When the scan stops on a busy channel the screen goes back to the stock hold screen: the busy
channel's name on the big line, the zone name under it, and its `CH n`. When the scan resumes, the zone name and
`Scanning...` come back. List scans keep the stock screen. The channel being visited during the walk is still not shown
by name (planned for a later release).

**How it stops and resumes.** It uses the stock scan engine: it stops on activity and holds the channel like a list scan.
The radio's receive filters still apply to digital channels (timeslot, colour code, group and private call matching), as
for a stock list scan; this was worked out from the firmware but not yet tried with a real DMR signal.

**Known limits.**

- After a stop, zone scan resumes **about 5 seconds** after the signal ends (checked on the radio on rc.3). rc.1 and rc.2
  waited about 25 seconds, because the hang value copied from typical scan lists counts half seconds, not tenths.
- Nuisance delete (the stock key function that skips the held channel) is wired up for zone scan but has never been
  exercised, in the emulator or on the radio. Treat it as untested.
- The hang time after activity is fixed (about 5 s; about 25 s in rc.1 and rc.2); it does not
  follow any menu setting. A stock list scan uses its list's own value, which the CPS shows in tenths of a second but
  the firmware counts in half seconds (a list set to "5.0 s" waits about 25 s). The real step and hang timings have not been measured on the radio.
- Opening a stock scan-list menu while a zone scan runs turns it into a list scan, as stock would.
- Priority channels and revert channels are not used in zone scan.
- The scan list setting on the channel still reads "none" in the radio's menu; that is expected.

**Different from stock:** only for channels with no scan list.

## 2. Quick menu and light mode

**What it does.** A programmable key opens a small **Quick menu** box over the main screen. In this release it has one
row, **Light mode: On/Off**. Light mode inverts the panel so the screen is light with dark text, which is easier to read
in daylight. Your colour choices invert too (yellow becomes blue, and so on), and so does the boot picture. The choice is
**saved** and applied at every power-on, before the first screen is drawn. The default is Off, the stock dark look.

**Setting up the key.** The quick menu reuses the stock key function **Flashlight** (the DM-32UV has no flashlight, so
the stock function did nothing). Assign **Flashlight** to a free programmable key: SK1 or SK2 (the side keys below the
PTT) or P1 or P2 (the front keys either side of the rocker), short or long press. You can do this in the CPS's key
settings or on the radio's own **Key** settings page; on rc.1 the owner set it on the radio, on SK2 short. **Avoid P2**:
the stock firmware treats P2 specially while any menu is open, so P2 is the one key that does not work well with the box.

**Using it.**

| Action | Key |
|---|---|
| Open the box | The key you assigned to Flashlight, from the main (idle) screen. It does not open from inside a stock menu |
| Change the value | **OK** toggles Light mode on and off; the screen changes at once |
| Close | **Back**. The stock menu timeout (Display settings, **Menu Exit Time**) also closes it; with that set to 0 it stays open until Back |
| Transmit | **PTT** works as normal: the box closes and the radio transmits |

The value changes with OK only; the knob and the rocker's left and right do nothing in the box in this release.

**What it writes.** Changing light mode saves one byte in the radio's settings memory, using the firmware's own settings
save. Nothing else is written. A factory reset, or writing a new codeplug from a fresh CPS file, sets it back to Off.
Reading and writing the codeplug with the official CPS keeps it.

**Known limits.**

- One row only. More rows (talk-group and scan options, a version row) are planned for later releases.
- The box text is English only.
- PTT with the box open was checked in the emulator (the transmitter settings are identical to stock); it has not been
  specifically tested on the radio.
- Whether light mode really is easier to read in direct sun is a matter of taste; the earlier always-inverted test build
  was "just readable in low sun at the right tilt, better than stock".

**Different from stock:** the Flashlight key function opens the box instead of giving an error tone; the screen can be
inverted.

### RX match and TS filter rows (not yet in a release)

Builds after 1.1.0 add two rows under Light mode. **Down** and **Up** move between rows; **OK** changes the selected one.

| Row | Values | What it does |
|---|---|---|
| RX match | **TG**, **RGL**, **Any** | Which group calls you hear. **RGL** (the default) is stock: the channel's RX group list plus its own talk group. **TG** plays only the talk group PTT would call: the one picked with the [talk-group keys](#6-independent-talk-groups), or the channel's own contact. **Any** plays every talk group |
| TS filter | **On**, **Off** | **On** (the default) is stock: a repeater channel listens on its own timeslot. **Off** also listens on the other timeslot: a call there is heard when both slots are quiet, and the radio goes back to its own slot afterwards |

**What they write.** RGL and Any are Baofeng's own **GCall Match** setting (Other settings), so that menu row and the CPS
show the same thing. TG and TS filter Off are kept in two spare settings bytes next to the light-mode byte. A factory reset or a fresh CPS file sets them back to RGL and On.

**Known limits.**

- **Nothing here has been on a radio.** The emulator can check what the radio stores, but it can't receive DMR, so
  whether calls are muted or heard is untested.
- **TS filter Off is a test feature.** PTT always goes out on the channel's own slot, even straight after a call heard
  on the other slot.
- **TG after a talk-group step.** TG applies from the next call; a call already in progress may carry on.
- **TG after an on-radio RX-list edit.** Editing the RX list on the radio itself leaves TG inactive until you change
  channel.
- **The Monitor key** still opens the radio to every call, whatever RX match says.

## 3. Text fixes

Same-length text changes in the English menus; the Chinese text is unchanged.

| Stock text | Now | Where it appears |
|---|---|---|
| VerSions | Versions | Device information list |
| Revers | Reverse | Display direction setting |
| dd/mm/yyy | dd/mm/yyyy | Date format setting |
| Date is setted | Date is set | Pop-up after setting the date |
| Digit Encrypt | Digital Encrypt | Channel edit page |
| Digit Monitor | Digital Monitor | Not confirmed which screen |
| keypad unlocked | Keypad unlocked | Pop-up when the keypad is unlocked |
| Succeed! | Succeeded! | Success pop-up |
| NO Contact | No Contact | Pop-up for an empty contact |
| Aprs Data | APRS Data | APRS message type row |
| Nonsupport | Unsupported | "Not supported" pop-up |

Each change was checked against the stock bytes and fits the space of the original string. The screens themselves have
not all been looked at on the radio; report anything that looks wrong.

## 4. GPS position padding fix

**What it does.** When the radio sends its position over DMR (for APRS via BrandMeister) in **Fixed Beacon** mode, the
stock firmware drops leading zeros: a longitude under 100 degrees, or a latitude under 10 degrees, comes out with one or
two characters missing, and the gateway cannot read it. The fix pads the numbers to full width, as other radios do. It
is a community fix (by IU2VTP) for exactly this firmware version, checked again here.

**Limits.**

- It only affects **Fixed Beacon** reports (a typed-in position). Reports from the live GPS copy the receiver's sentence
  as it is and never went through this formatting.
- Whether the reports now appear on APRS-IS has not been tested by this project.

## 5. Position report retry

**What it does.** With timed position reports on (for example every 300 s), the stock firmware restarts its
interval timer *before* it checks for a GPS fix, so if there is no fresh fix at that exact second the report is skipped
and the radio waits a whole interval again. In practice a 300 s interval rarely sent anything, while 60 s worked better.
With this release the timer keeps its place and tries again every second until a report can go out, then starts the next
interval.

Nothing changes in how you set it up: the report interval, channel and destination are the stock settings in the CPS.
Manual sends are unchanged.

**Limits.**

- On the radio (rc.2), reports at a 300 s interval kept going out. The emulator does not model a GPS fix the firmware
  accepts, so the retry itself is shown only by the timer holding its count there.

## 6. Independent talk groups

**What it does.** On a digital memory channel that has an RX group list, you can step through that list and transmit to the member you stopped on. The channel's own stored contact is still there: it is the starting point, and you can step back to it. Receive does not change. The radio still hears the whole list, and Group Call Match still does what it did before.

Nothing is saved. Power off clears every selection. The codeplug is not modified by stepping or by transmitting.

**How to assign the keys.** In the CPS, program the keys you want (usually P1 short and P2 short) as **Previous Record** and **Next Record**. Those are the names the CPS shows. On the radio's own English key list the same two codes are **TG Prev** and **TG Next**. If you do not assign them you cannot step, but the line under the channel name still changes: on a digital channel that has a stored contact it shows that contact's name instead of the frequency (see below).

**What the keys do.**

- **TG Next** (Next Record) steps forward. **TG Prev** (Previous Record) steps back. They wrap around.
- The first step leaves the channel's stored contact. Further steps are the RX-list members, in the order they are stored. Empty slots are skipped. A member that is the same id as the stored contact is not offered twice.
- While you are on a member, the line that usually shows the frequency shows that member's name. If the id has no contact, the line shows the number. The channel name and the zone name stay as they are.
- At the start, before any step, the line shows the channel's stored contact, the one PTT calls. Step back to the start and that name returns. PTT then uses the stored contact, as stock. A selected member and the stored contact look the same on the line.
- If the stored contact's name ends in TS1 or TS2, the line shows it whole. That ending does not change the slot for the stored contact; it only does for a member you step to ([section 9](#9-timeslot-from-the-talk-group-name)).
- A digital channel with no stored contact, an analogue channel and VFO show the frequency, as before. So does a scan, while it runs, even if you had a member selected; the name comes back when the scan stops. (Showing the scanned channel's own talk group is planned for 1.2.0.)
- Right after you change channel the line can show the frequency for a moment before the name appears.
- A channel that was saved with an RX list and no transmit contact can still transmit once you have stepped onto a member. At the start, with nothing selected, it still says no contact.
- The keys do nothing on an analogue channel, on a digital channel with no RX list, in a menu, in VFO, or while scanning.
- If the radio is set to show the frequency as the big line, there is no name. That display is unchanged.

**Tested on a radio?** Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open. The emulator gate covers the step, the name, and the destination the firmware hands to the modem. It does not cover the air.

## 7. Star key timeslot

**What it does.** On the channel screen, a short press of `*` on a digital channel that uses a repeater swaps that channel between timeslot 1 and timeslot 2. The radio shows its own "Slot 1" or "Slot 2" message for a second. Press `*` again to go back to the slot the channel was programmed with.

The swap belongs to that channel and lasts until you move that side to another channel or zone, step to another talk group (or back to the channel's own contact) with the [independent talk group](#6-independent-talk-groups) keys, or power off. It also works when the talk group's name sets the slot ([section 9](#9-timeslot-from-the-talk-group-name)): `*` always swaps the slot of the talk group on screen. Nothing is saved to the codeplug. Dual watch does not undo it. If you come back to the channel later, it is on its programmed slot again.

**Where `*` still does what it did before.**

- On an analogue channel, and in VFO, short `*` toggles NOAA weather, as stock. In weather mode, `*` leaves it.
- On a digital simplex (direct) channel, `*` gives the refusal tone and nothing changes. The radio always uses slot 1 on simplex.
- A long press of `*` locks the keypad, as stock.
- In menus, while scanning, during a call, or while typing a channel number, `*` does what stock does.

**Known limits.** The radio's own channel menu still shows the programmed slot after a swap. The [timeslot indicator](#8-timeslot-indicator) shows the swap on the channel screen.

**Tested on a radio?** Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open. The emulator shows the firmware switch the slot settings and keep them through dual watch, but it cannot show which slot the radio transmits on.

## 8. Timeslot indicator

**What it does.** On a digital channel, the icon row of each side shows `TS1` or `TS2` just left of the `DIG` badge. It is the slot that channel uses: the slot it was programmed with, or the other one after a [star key swap](#7-star-key-timeslot). A digital simplex (direct) channel always shows `TS1`, because the radio always uses slot 1 there.

It shows on both sides, in that side's colour. It is redrawn with the `DIG`/`ANA` badge, so it follows channel changes, star key swaps and talk-group steps. During a scan it follows the channel the scan stops on: on an analogue channel it goes away.

**Where it does not show.** Analogue channels, mixed-mode (`A+D`/`D+A`) channels, VFO and weather mode.

Talk-group stepping, the star key and the badge all work on every channel number, including channel 4000 (an early build refused it).

**Known limits.** The stock recording icon, if the radio ever draws it, sits under the badge. Recording appears to have been removed from this firmware, so it should not be seen. The radio's own channel menu still shows the programmed slot after a swap.

**Tested on a radio?** Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open. The emulator gate checks the badge text and position in the screen it records.

## 9. Timeslot from the talk-group name

**What it does.** When you step to a talk group with the [independent talk group](#6-independent-talk-groups) keys, and its contact name ends in `TS1` or `TS2`, the channel switches to that timeslot straight away, for receive and transmit. This is how you give a talk group its own slot with the official CPS: put the slot at the end of the contact name, for example `Scotland TS2`. Case does not matter, spaces at the end are ignored, and the space before the suffix is optional, so `Scotland ts2` and `ScotlandTS2` work too.

- The name line shows the name without the suffix (`Scotland`). The [timeslot indicator](#8-timeslot-indicator) shows the slot.
- Step to a talk group without a suffix, or back to the channel's own contact, and the channel goes back to its own slot.
- The channel's own stored contact never sets the slot, whatever its name says.
- Change channel and come back: the talk group you had selected, and its slot, are still there. Power off clears both.
- The [star key](#7-star-key-timeslot) still swaps the slot while a suffixed talk group is selected: short `*` puts the channel on the other slot, and a second press goes back to the suffix's slot. Stepping to another talk group, or back to the channel's own contact, drops the swap, and that talk group's suffix, or the channel's own slot, applies.
- On a digital simplex (direct) channel the radio always uses slot 1, suffix or not.

**A slot stored in the RX group list wins.** If Codeplug Studio stored a slot for that member of the channel's RX group list, that slot applies and the suffix is ignored (the name line still hides it). The star key still overrides both. A member with no stored slot uses its suffix as above. The store needs a Codeplug Studio version that writes it. If you change a list's members in another tool afterwards (the official CPS, for example), the radio ignores that list's stored slots until Studio writes them again, so you never get a slot meant for a different talk group.

**Known limits.** The suffix uses three or four of the name's 16 characters. A name that happens to end in `ts1` or `ts2` sets the slot too. There is no switch to turn suffixes off. The radio's own channel menu still shows the programmed slot.

**Tested on a radio?** Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open. The emulator shows the firmware switch the slot settings and the call go to the selected talk group, but not which slot goes out on air.

## 10. Which version is installed

This firmware is built on Baofeng's stock firmware **v1.01.048**. The radio shows that base as `DM32.01.L01.048`, and
shows our version as **`mm9pdy-`** followed by the release, for example `mm9pdy-1.1.0` or `mm9pdy-1.1.0-rc.1`. Stock
firmware never shows a `mm9pdy-` line.

**Where to look** (from 1.1.0; not in 1.0.0 or earlier):

- **At power-on.** `mm9pdy-1.1.0` in small white text, centred at the bottom of the boot screen, under the stock
  welcome text or boot picture. It stays up as long as the boot screen does.
- **Settings > Device Info > Versions.** Stock shows `Firmware Ver:` and `DM32.01.L01.048` (unchanged: that is the
  Baofeng base), then `CPS Ver:`. Our version is the small line below them: `mm9pdy-1.1.0`.

A build you made yourself without `--version` shows `mm9pdy-g` and seven hex digits of the commit (`-dirty` after it
when the checkout had uncommitted changes), or `mm9pdy-<tag>` when the checkout was exactly at a release tag. A
plain `mm9pdy` with nothing after it is an unstamped build (the image the emulator gate tests); a release never shows it.

**Known limits.** On a boot picture, the version line covers a strip of the picture about 8 pixels per character wide
and 16 high. The official CPS and Codeplug Studio still read `DM32.01.L01.048` as the firmware version, because that text
is unchanged.

**Tested on a radio?** Checked on the owner's radio for the 1.1.0 release; the full on-air checks are still open. The emulator gate checks both lines in the screens it records.

**Older releases (1.0.0 and its RCs)** do not show our version on the radio; Device Info shows only `DM32.01.L01.048`.
For those:

- **From behaviour:** if the Flashlight key opens the Quick menu box, the radio runs rc.1 or later.
- **From a read-back:** rc.2 and later also stamp the release into the image, which a firmware read-back shows.
  Codeplug Studio does not read firmware back yet.

## 11. Known limits in 1.1.0

The ones that matter in use, collected from the sections above. The 1.1.0 features were checked on the owner's radio for the release; the full on-air checks are still open.

- **Nothing is saved.** Talk-group selections and star-key swaps live in RAM only and are gone at power-off. The
  codeplug is never written by them. The radio's own channel menu still shows the programmed timeslot after a swap or a
  suffix; the `TS1`/`TS2` badge shows what is really used.
- **Which slot goes out on air is radio-only.** The emulator shows the firmware switch its slot and call settings, not
  the air. Until the on-air check, treat which slot goes out (sections 7 and 9) as unconfirmed.
- **A brief frequency first.** After a channel change, the line under the channel name can show the frequency for a
  moment before the contact name appears (section 6).
- **A stale name after an edit.** If you change a channel's transmit contact in the radio's own channel menu, the old name
  stays on the line until you change channel or power off (names are kept per channel).
- **Scanning shows the frequency.** While a scan walks or holds, the line under the channel name shows the scanned
  channel's frequency, never a talk-group name. Showing the scanned channel's own talk group is planned for 1.2.0.
- **No badge on every kind of channel.** No `TS1`/`TS2` badge on analogue channels, mixed-mode (`D+A`/`A+D`) channels,
  VFO or weather mode.
- **Talk-group names with a slot.** A name ending in `ts1` or `ts2` sets the slot even if you did not mean it, and there
  is no switch to turn that off. The suffix takes three or four of the name's 16 characters. The star key always wins
  over a suffix, and a talk-group step drops the swap.
- **Frequency display mode.** If the radio is set to show the frequency as the big line, there is no talk-group name.
- **Version line.** On a boot picture, the version line covers a strip at the bottom of it.
