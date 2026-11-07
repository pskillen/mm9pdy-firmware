# NXDN (open beta)

The stock V1.05 firmware already contains an NXDN mode. AnyTone hasn't released it: an official NXDN update waits for
approval by the NXDN Forum. Stock hides the mode and forces the radio to DMR at every power-on.

The mods let you turn it on, behind a 4-digit PIN. The PIN is a deliberate opt-in step that says you have read this
page, not a lock. Everything the radio does in NXDN mode is **AnyTone's own, unreleased NXDN code**. It isn't
approved by the NXDN Forum, and the mods change none of the protocol. What the mods add is the unlock, and guards that
stop a DMR channel from transmitting NXDN (below).

Treat it as a beta. It works, but it has rough edges, and some of them are AnyTone's (one protocol at a time, a slow
switch). NXDN is for amateur use here: check that your licence allows it where you transmit.

The NXDN Access row is in every release from 1.3.0.

## 1. Turning NXDN on

1. Settings > Radio Set > Other Func > **NXDN Access**, the last row. It opens a PIN screen: "Enter PIN", four boxes.
2. Enter the PIN, supplied separately from this manual.
   - Right: the radio shows "NXDN unlocked" and saves.
   - Wrong: it shows "Wrong PIN" and clears. There's no lock-out.
   - Back deletes a digit, or closes the screen.
3. Other Func now shows the stock **Protocol** row, just before NXDN Access. Pick **NXDN** or **DMR**. The switch
   takes 5–6 seconds. The protocol is kept over a power-off.

To lock it again, open NXDN Access, which now offers **Unlocked / Lock**. Lock switches the radio back to DMR first,
then locks.

Until you unlock it, the radio is DMR only, as stock: a codeplug that asks for NXDN is ignored.

## 2. One protocol at a time

The radio runs **one digital protocol for every channel**: all DMR or all NXDN, chosen with Protocol. It can't scan or
receive DMR and NXDN at the same time, and it doesn't switch by itself when you change channel or zone. Analogue
channels work in both modes.

## 3. Programming NXDN

- **Use Codeplug Studio** (the MM9PDY modded firmware target), not the vendor CPS. Studio checks that the radio has
  NXDN unlocked before it writes any NXDN setting.
- **Read the radio in Studio** before the first Write after you unlock NXDN.
- **Set a default NXDN Digital ID** in Studio's Library (Digital IDs). Write sets it as the radio's NXDN ID. Without one,
  the radio sends source ID 0.
- **Give each NXDN channel a call target** (PTT Call with a contact). Without one, the transmit screen shows "NULL ID"
  and the radio makes a group call to ID 0.
- **Avoid writing with the vendor CPS** once NXDN is unlocked:
  - A vendor CPS write can lock NXDN again.
  - It can set "Reset Digital Protocol", which forces one protocol at every power-on. Studio sets that to Off.

## 4. How channels behave

| | In NXDN mode | In DMR mode |
|---|---|---|
| Analogue channel | Works as usual | Works as usual |
| Digital channel with NXDN settings | Works as an NXDN channel | Works as a DMR channel |
| Digital channel with no NXDN settings (DMR only) | **Hidden** from its zone, and **can't transmit**: PTT shows "Not NXDN" | Works as a DMR channel |

- **In DMR mode nothing is hidden.** A channel you set up for NXDN only is still in its zone and **would transmit DMR**.
  Don't key up on NXDN channels while the radio is in DMR mode.
- **Repeater mode** is refused in NXDN mode while either side is a DMR-only channel.
- **A channel with both FM and NXDN settings** is treated as digital in NXDN mode. If one ever transmits FM, please
  report it.

## 5. Emergency alarm and other sends

The guards above act on PTT. Some transmissions don't go through PTT, and in NXDN mode they go out as stock sends them,
on whatever channel they use:

- **The emergency alarm** (and man down, lone worker): not blocked, because blocking it could silently stop an
  emergency call. It transmits NXDN on its channel, even a DMR-only one. While you use NXDN, set the digital alarm's
  channel (CPS Alarm tab) to an NXDN channel, or set the digital alarm type to Alarm only.
- **A hot-key NXDN status message, the contact menu's call alert, radio check, remote monitor and stun or kill, and
  SMS**: sent on the current channel. With DMR-only channels hidden, that's an NXDN or analogue channel.

## 6. What it doesn't do yet

- The mods' talk-group features are DMR only: talk groups picked independently of the channel, and the Reply key on
  the call screen. NXDN equivalents are planned.
- No caller-name directory for NXDN IDs yet. Names come from the radio's NXDN list.
- No per-channel record of which protocol a channel is for, so the DMR-mode case above can't be blocked yet.

## 7. Going back to stock

Stock firmware forces the radio to DMR at every power-on, so after [going back to stock](back-to-stock.md) the radio is
a DMR radio again. Your NXDN channels stay in the codeplug. Stock treats them as digital (DMR) channels, so don't
transmit on them.

## 8. Reporting a problem

Open an issue on the public repository (see [Getting help](README.md#getting-help)). Say step by step what you did:
the channel type, the Protocol setting, and what a second radio or a decoder heard.
