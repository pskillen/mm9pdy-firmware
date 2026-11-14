# Recovery

> **Release candidate docs: 1.0.0-rc.1** These pages describe a release candidate that is still being tested.

**Not yet checked on a radio.** Every step below is a plan, not a record.

## The update stopped part way

The cable came out, the battery ran down, or the computer went to sleep during **Connect and flash**.

1. **Not yet checked on a radio.** Charge or change the battery if it is low. Plug the cable back in.
2. **Not yet checked on a radio.** Switch the radio on **without holding any keys**. If the update was cut, the screen
   stays dark: the radio is waiting to carry on.
3. **Not yet checked on a radio.** In Codeplug Studio, with the **same files** you used before (the same release or
   to-stock file, and the same [stock file](install.md#what-you-need)), press **Connect and flash** again. Studio
   carries on from where the radio is. Leave everything alone until the radio shows its normal screen.
4. **Not yet checked on a radio.** Check it as in [install.md](install.md#3-check-it-worked), or for back to stock as
   in [back-to-stock.md](back-to-stock.md#check-it-worked).

If the radio starts normally instead, the update either finished or never began. Check Radio Info: a fourth line with
the build name means it finished. Otherwise start the install again from the beginning.

## The radio refused the file

- **The file is for the other kind of UV-5R Mini.** The radio refuses it before anything is installed. Its FM radio
  presets and volume may have been reset; set them again. Nothing else has changed. Check your radio's suffix, Firmware
  and Hardware lines ([the first page](README.md#read-this-first)).
- **"Not for this radio's key."** The files do not fit this radio, and nothing was written. Check that you chose
  the right release and stock file for your radio.

## The red TX light came on while entering update mode

Switch the radio off at once. The keys were not pressed together, or not held while switching on. Try again: hold
**PTT-A** and **=** first, then switch on.

## When it needs a repair with the case open

A few failures can't be fixed with the cable:

- the power is lost at one particular instant near the end of an update (a fraction of a second), which can leave the
  radio unable to start or to update;
- the radio shows nothing at all, and **Connect and flash** with the same files can no longer reach it.

Then the radio needs a repair with the case open, by someone with the right tools. A fully charged battery, and not
touching the radio, the cable or the battery during an update, keep this from happening.

## Things to avoid

- Do not use files meant for another kind of UV-5R Mini.
- Do not switch the radio off and on repeatedly to "try again": go back to the steps above.
- A factory reset (**Radio Set › Reset**) does not change the firmware, and does not help here.

If none of this works, ask for help with the radio's suffix, Firmware and Hardware lines, the release you wrote, and
what the screen did.
