# What the mods do

> **Release candidate docs: 1.2.0-rc.2** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../anytone-at-d890uv/features.md).

Each mod is described here as it behaves on the radio, with how to turn it on and what it does not do. Which release has
which mod, and what has been checked on a real radio, is in each release's notes (Codeplug Studio shows them when you
pick a release).

Most mods do nothing until you assign a key to them in the CPS. With no keys assigned, the radio behaves as stock,
apart from the release name on the power-on screen, the star-key timeslot toggle and, from 1.2.0, the channel screen
in the single display (below).

> **Changed in 1.2.0: the channel screen with one channel on screen (CPS "sub channel" off), for everyone.** Every
> channel now shows three lines, whether or not any keys are assigned: the channel name; the talk group (digital) or
> the receive frequency (analogue); and the zone name on a small centred line underneath. Before, line 2 showed the
> zone name (or alternated it with the contact) and analogue and digital channels looked different. With both channels
> on screen nothing changes unless TG next / previous is assigned.

## 1. Setting up keys in the CPS

The mods reuse three of the radio's stock key functions. The **CPS still shows the stock names**, so you pick them by
their old name. The radio's own menu (Menu > Radio Set > Key Func, English menu language) shows the new names.

| Mod | Pick this in the CPS key list | The radio's Key Func menu shows | Stock function it replaces |
|---|---|---|---|
| TG previous | Record Switch | TG Previous | Record Switch |
| TG next | Record | TG Next | Record |
| Quick filters menu | Priority Zone | Quick Filters | Priority Zone |

You can assign them to the short or long press of PF1, PF2, PF3, P1 or P2. A common set-up: P1 = TG next, P2 = TG
previous, PF3 = Priority Zone (quick filters). Write the codeplug to the radio as usual.

While the mods are on the radio, the stock Record Switch, Record and Priority Zone functions are not available.

## 2. Independent talk groups

Pick the talk group you talk on separately from the channel. Program a repeater once, as one channel, and put the talk
groups you use on it in the channel's RX group list. Then:

- **TG next** steps through the channel's own contact, then each talk group in the RX group list, in list order, and
  wraps round. **TG previous** goes the other way.
- **PTT** transmits to the talk group you picked.
- **Line 2** of the channel screen shows the picked talk group, under the channel name.
- The **zone name** stays on screen. With one channel on screen it is on a small, centred line of its own under the
  talk group. Every channel looks the same there: channel name, then the talk group (digital) or the frequency
  (analogue), then the zone, whether or not TG next / previous is on a key. Line 2 shows the receive frequency, also
  while you transmit on a split channel. With the CPS display mode set to frequency, line 1 already shows it, so line
  2 shows the channel name instead. With both sides on screen (CPS "sub channel" on) it follows the talk group on line 2, as
  `Talk group | Zone`; when that is too long for the line it scrolls, like a long channel name. The other side's
  line (the sub side, dual watch) shows that side's own pick the same way, as `Talk group / Zone`.
- The pick is **kept per channel** while the radio is on. Change channel and come back: your pick is still there.
  Switching off clears every pick. Nothing is saved to the codeplug.
- The timeslot a picked talk group is sent on, first match wins: the slot set for that member in the RX group list
  (see below), then a name ending in `TS1` or `TS2` (for example `Scotland TS2`), then the channel's own timeslot. The
  quick filters menu's **TG slot** row (Channel) turns the first two off.
- **A timeslot per RX-list member** is set in Codeplug Studio (the MM9PDY target writes it with the list). The radio
  only reads it; there is no menu to set it. It should be lost when the list is written by the official CPS or by Studio's
  stock target (not yet checked on the radio), and is expected to stop applying after you edit that list's members on
  the radio (the whole list's slots are then ignored and the name suffix and channel slot apply).
- **During a call** the same keys still work. Press TG next or TG previous while a call is on the receive screen and the
  radio steps, goes back to the channel screen and shows the new talk group on line 2. With the quick filters menu's
  RX match set to TG, the call you stepped away from should stop being heard (not yet confirmed on a radio). With RGL or Any the call may carry on,
  but the next time you transmit it goes to the talk group you picked. It works for group and private calls. It does
  nothing while the sub side (dual watch) is the one receiving.
- A channel with no RX group list shows "No RX list" and nothing changes.
- A digital channel with **no contact** (the CPS's "None", or a contact that points at a deleted talk group) starts on
  the **first talk group in its RX group list** instead of the first talk group in the radio. PTT, line 2 and what you
  hear all follow. The cycle for such a channel is just the list: the first talk group is not offered twice. A channel
  with no contact and no RX group list behaves as stock. A contact that is set, including the first talk group in the
  radio, is never changed. This needs TG next or TG previous assigned to a key, like the rest of this section (except
  the single display's channel screen, which is the same for everyone).
- **Stopping a zone scan on a call** picks the talk group you just heard, so you can reply straight away. Stop the
  scan (any key, or Menu) while it is paused on a digital channel during or just after a group call:
  - a talk group in that channel's RX group list, or its own contact, becomes the channel's pick, as if you had stepped
    to it;
  - any other talk group (heard with RX match Any or digital monitor) is used **for now only**: line 2 shows its name
    if it is in the radio's talk-group list, otherwise its ID, and PTT goes to it on the timeslot it was heard on
    (a `TS1` / `TS2` name, or TG slot Channel, still decide the slot). TG next / previous, or changing channel, goes
    back to the channel's own pick.

  A stop that goes back to the start channel, a private call, an analogue channel and list scan change nothing.

Limits:

- Digital memory channels only. Not in VFO mode, not while scanning, and only on the channel screen or the receive screen of a call.
- The main side only. To change the sub side's (dual watch) talk group, make it the main side with Main Channel Switch
  (key function 19), step, and switch back; each switch saves the radio's settings, as in stock. Stepping is ignored
  while the sub side is receiving.
- Hot keys, last-call reply and talkback after a received call use their own target for that call. Your pick comes
  back at the next channel change or step.
- The name suffix is matched loosely: the last three letters, ignoring case, so `xTS2` counts too.
- "No RX list" is in English whatever the menu language.
- Up to 64 talk groups per RX group list (the stock limit).

## 3. Star-key timeslot toggle

On the channel screen of a digital channel, a **short press of `*`** switches the channel between TS1 and TS2. The
radio shows "TS 1 Selected" or "TS 2 Selected", and the T1 / T2 badge follows.

- The change is not saved. Changing channel and coming back, or switching off, brings back the timeslot in the
  codeplug.
- A **long press of `*`** still locks the keypad, as stock. `*` works as stock everywhere else.
- On an analogue channel a short `*` does nothing, as stock.
- A talk group picked with TG next / previous that has a timeslot from its RX list or a `TS1` / `TS2` name suffix keeps that timeslot whatever `*` did.

There is no setting: this mod is always on.

## 4. Zone scan

In stock V1.05, scan always walks the selected channel's scan list, which may hold channels from other zones and not
the zone you are in. With zone scan, the scan key (or Menu > Scan) on a memory channel scans **every channel of the
current zone**, in zone order, starting after the current channel. It works on channels that have no scan list.

- **Stopping:** if the scan is paused on a channel with activity, or still holding there after the activity ended, the
  radio stays on that channel. Otherwise it goes back to the channel where the scan started.
- Menu during a scan keeps its stock meaning: go to the last channel that had activity. PTT keeps the stock talkback.
- With TG next or previous assigned, a stop that stays on a digital channel after a group call also picks the talk
  group heard there (see section 2).
- Priority channels and the channel's auto-scan setting are ignored in zone mode. They are left as they are in the
  codeplug.
- Zones of more than 100 channels are scanned 100 at a time.
- VFO scan is unchanged.

**Heard-call popup** (new in 1.2.0; TG next or previous assigned, Scan = Zone). When the scan holds on a digital
channel because of a call, a box pops up over the receive screen: the channel name and frequencies at the top, the
talk group in large letters (its name from the channel's contact or RX list or your talk-group list, else
`TG <number>`), the call type, number and slot, and the caller's number. Its keys:

| Key | What it does |
|---|---|
| Menu (**Switch**) | Stop the scan on this channel and take that talk group, so PTT answers it. For a private or all call the scan stops on the channel and the talk group stays as it was |
| Back (**Close**) | Close the box and let the scan carry on after the call. A second Back stops the scan as before |
| `*` (**Skip channel**) | Skip this channel until the next scan (the radio's own nuisance delete) |
| Any other key | Closes the box and then does its usual job |

The box goes away by itself when the call is over and the scan moves on. A radio notice (low battery and so on) takes
its place, and it doesn't come back for that call. Turn it off with the quick filters' **Scan popup** row; with it off,
the scan behaves as in 1.1.0.
- The quick filters menu's **Scan** row switches between zone scan (the default) and the stock scan-list behaviour.

The scanning itself (dwell, pausing on activity, nuisance delete) is the stock scan engine.

## 5. Quick filters menu

A small list of receive and scan settings over the channel screen. Press the key you assigned to **Priority Zone**
(the radio calls it "Quick Filters").

- **Up / Down** move between rows. Five rows show at a time; moving past the last one scrolls the list. The **knob or P2** picks the next value, **P1** the previous one. A change takes
  effect at once.
- **Menu**, **Back**, the same key again, or 10 seconds without a key close it. Changes are saved when it closes and
  survive switching off.
- PTT works as normal while it is open.

| Row | Values | What it does |
|---|---|---|
| RX match | TG / RGL / Any | Which group calls you hear. **TG**: only the talk group you would transmit to (your pick, or the channel's contact). **RGL**: the channel's RX group list, as stock with digital monitor off. **Any**: every talk group, as stock digital monitor on |
| TS filter | On / Off | On: listen on the channel's timeslot only. Off: listen on both timeslots |
| CC match | Yes / No | No: relaxes the colour-code checks the radio's main processor makes (monitor mode and the repeater colour-code limit). The DMR chip still checks the colour code on normal receive |
| Scan | Zone / List | Zone scan, or the stock scan-list scan |
| TG slot | Auto / Channel | Auto: the RX list's slot for the picked member, else a `TS1` / `TS2` name suffix, sets its timeslot. Channel: always the channel's timeslot |
| Tone | Ch / Any | Analogue channels with a receive CTCSS / DCS tone. **Ch**: as stock, the squelch opens only on the channel's tone. **Any**: it opens on any signal, whatever its tone. The channel keeps its tone, and the radio still transmits it. A busy lock set to "repeater" still uses the tone. Both sides follow the row |
| Scan popup | On / Off | The heard-call popup during a zone scan (section 4). Off: no popup |
| To VFO | Copy | An action, not a setting. On a memory channel, **knob or P2** copies the main side's channel (as you use it now: frequency, tones, colour code, power and so on, and on a digital channel the talk group you picked and its slot) into that side's VFO, switches to the VFO and closes the menu. The memory channel is not changed; V/M goes back to it. Shows `--` and does nothing when the side is already on the VFO, the codeplug turns the VFO off, the side is on the air band or FM radio, or while transmitting. A picked talk group that is only an ID (heard, not in your talk-group list) is not copied: the VFO keeps the channel's own contact. Each copy writes the VFO memory once |

RX match and TS filter together replace the stock "Digital monitor" setting. Changing them changes that setting, and
the stock menu and the CPS see the change.

Limits:

- The clock and status icons do not update while the menu is open. Closing it redraws the screen.
- It does not open during a scan, off the channel screen, or over a popup.
- While it is open it takes every key, so TG next / previous do nothing.
- If you assign it to a long press, a second long press does not close it. Use Back, Menu or wait 10 seconds.
- Labels are in English.

## 6. Release name

Every release is a mod of the stock AnyTone firmware **V1.05**. The radio shows both:

- **Power-on screen**: your power-on message or picture as before, and the release name along the bottom, for example
  `mm9pdy-1.1.0` for a release or `mm9pdy-1.1.0-rc.1` for a release candidate. A name too long for the normal font
  is drawn in a smaller one, so it is never cut short.
- **Menu > Settings > Device Info**: "Firmware Ver:" still shows the stock **Ver 1.05**, the firmware the release is
  built on. Right after it is an extra item, **Mod Ver:**, with the release name, for example `mm9pdy-1.1.0`. The
  items after it are the stock ones, one place further down.

The name is `mm9pdy-` and the release number, with no `v`. The release number is the same as the published release
(`1.1.0`, `1.1.0-rc.1`). This is how you tell which release is on the radio, and that it is mm9pdy's firmware and not
stock or someone else's mod. See [install.md](install.md#4-check-it-worked).

## 7. Settings the mods keep

The quick filters menu's own settings (TS filter, CC match, Scan, TG slot, Tone, Scan popup, and RX match TG) are kept in a small unused
area of the radio's settings memory, not in the codeplug format. The CPS does not show them and does not write that
area. Settings the stock radio already has (digital monitor, monitor colour code) stay in their stock place.
A CPS write or a settings reset may put the mods' settings back to their defaults (section 8).

## 8. Codeplug compatibility

The codeplug format is not changed, so the same codeplug works on stock and on a release. In short:

- The CPS shows the stock names for the three reused key functions (section 1). On stock firmware they do the stock
  thing again.
- The quick filters settings (section 7) are not in the codeplug. A write with the official CPS keeps them (checked on
  the radio); a settings reset returns them to their defaults.

The details are in [codeplug.md](codeplug.md).

## 9. Bluetooth headset volume

With a Bluetooth headset connected, the volume knob also sets the headset's loudness, in 15 steps. Fully down still
mutes, as on stock. When the headset connects, it starts at the knob's loudness, so the Bluetooth speaker-gain value
from the CPS or the Bluetooth menu is replaced while the knob is up. Changing that menu item still works, until you next
turn the knob. Some headsets keep their own volume and may not follow the knob.

Not yet tried on a radio: whether the headset follows the knob at once depends on the Bluetooth module.
