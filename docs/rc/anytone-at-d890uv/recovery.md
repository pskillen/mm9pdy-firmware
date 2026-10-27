# Recovery

> **Release candidate docs: 1.2.1-rc.1** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../anytone-at-d890uv/recovery.md).

What to do when a firmware write fails or the radio will not start afterwards.

## 1. What a firmware write can and cannot damage

| Part of the radio | Can a firmware write change it? |
|---|---|
| The firmware (the radio's main program) | Yes. That is what is written |
| The update program that runs in update mode (the bootloader) | No. Codeplug Studio refuses to write there, and the stock package does not either |
| The radio's activation data, next to the bootloader | No. Codeplug Studio refuses to write there |
| Codeplug, settings, calibration, serial number | No. They live in a separate memory chip that a firmware write does not reach |

So a bad or broken write puts only the firmware at risk. **As long as the radio still enters update mode, you can put
stock back** ([back-to-stock.md](back-to-stock.md)).

## 2. First: stop

At the first sign of trouble, stop. Do not retry straight away, and do not try other tools to see what happens. Write
down:

- what the screen and the red LED show;
- what Codeplug Studio said (its summary can be copied or saved as text);
- whether the radio still shows up on the computer.

## 3. What to do

| What happened | What it means | What to do |
|---|---|---|
| Studio stopped with an error before the radio was touched | Nothing was written | Check the cable and the port, then start again |
| Studio stopped with an error during the transfer, and the red LED is still blinking | The firmware is partly written. The radio will not start normally | Check the cable. Run the **whole** flash again from the start. A write cannot be resumed. If it fails again, flash stock ([back-to-stock.md](back-to-stock.md)) |
| Power or USB was lost during the write | The same, and the radio is no longer in update mode | Reconnect, charge, enter update mode again (PTT and PF3) and flash again, or flash stock. **Not tried on the radio yet**: see below |
| The write finished but the radio shows nothing, restarts over and over, or shows garbage | The firmware image is bad | Enter update mode and flash stock. Then report it |
| The write finished, but the release name is not on the power-on screen | The old firmware is still on the radio | Flash again |
| The radio works but the codeplug, calibration or serial number look wrong | Should not happen from a firmware write | Do not write anything else. Report it |
| PTT and PF3 give no blinking LED | Update mode cannot be reached | Charge the battery and try again, holding the keys before switching on. If it still fails, contact your dealer or AnyTone. There is no further self-service step |

The radio shows up on the computer the same way in normal mode and in update mode. Only the blinking red LED and the
blank screen say it is in update mode.

## 4. Not yet tested

- **An interrupted write.** What the radio does after a write that stopped halfway, and whether PTT and PF3 still
  reach update mode afterwards, has not been tried. It is expected to work, because update mode starts before the
  firmware does. Until then, always write with a full battery, a direct cable and the stock zip to hand.

## 5. Avoiding trouble

- Full battery, short direct USB cable, no hub.
- Close the CPS and anything else that might use the radio's port before flashing.
- Keep the stock zip and a copy of your codeplug.
