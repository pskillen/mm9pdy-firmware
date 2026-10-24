# Recovery

> **Release candidate docs: 1.2.0-rc.1** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../baofeng-dm32uv/recovery.md).

What to do when a firmware write fails, and what never to do. It depends on whether the radio can still enter update
mode.

## If something goes wrong

1. **The write stopped part-way, or the radio does not start after a write.** Turn it off. Try update mode (radio off,
   cable out, SK1 and PTT at power-on). If the LED turns **green**, plug in the cable and flash stock again
   ([back-to-stock.md](back-to-stock.md)). A write cannot be resumed, so always start from the beginning. This is the
   expected repair: as far as is known, the update writes only the firmware, not the bootloader that receives it.
   Others have reported recovering a wrong or half-written firmware this way; the project has not had a failed write
   yet.
2. **No green LED with SK1 and PTT.** Stop. Don't keep power-cycling. The bootloader itself may be damaged, and there
   is no tested repair: the remaining routes need hardware (a clip on the flash chips). Ask for help in an issue.
3. **The radio works but says "model error", refuses to transmit, or its tuning or levels are wrong.** That points at
   the factory sector or the calibration, which a firmware write does not touch. Restoring them needs a hardware
   programmer and your own backup of that radio; nothing in this project does it.
4. **Your channels are gone.** A firmware update has not done this so far. Write your codeplug back with the CPS or
   Codeplug Studio. A factory reset (SK1 and SK2 at power-on) also clears it, by design.

When in doubt, go back to stock and report what happened in an
[issue](https://github.com/pskillen/mm9pdy-firmware/issues/new/choose), with what Codeplug Studio said (its summary
can be copied or saved as text).

## What never to do

- **Never write the calibration page or the factory sector**, and never try to "restore" them from someone else's
  radio. One wrong write there has no repair, and another radio's factory sector does not work in yours.
- **Never send raw commands to the radio** with serial terminals or scripts from elsewhere. Some of the radio's PC-link
  commands erase or rewrite the factory sector or the calibration, and none of that can be repaired.
- **Never flash firmware for another radio or another firmware version.** Every release is built against v1.01.048
  (`DM32.01.L01.048` on the radio) only. Codeplug Studio checks this; other tools may not.
- **Don't enter update mode with the cable already plugged in** at power-on.
