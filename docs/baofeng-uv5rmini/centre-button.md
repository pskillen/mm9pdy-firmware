# Centre button and flashlight

<!-- variant-status:start -->
> **Availability by radio:** NRF, Firmware V0.27, Hardware V1.7: latest release 1.1.0. NRFB, Firmware V0.04, Hardware V1.7: latest release 1.1.0.
<!-- variant-status:end -->

On the MM9PDY firmware the blue button in the middle of the UV-5R Mini can do something different when you **tap** it
and when you **hold** it, and you choose both. The flashlight now just switches on and off.

This needs a MM9PDY release that lists the centre button in its notes, on one of the supported radios (see
[the first page](README.md#read-this-first)).

## Out of the box

Nothing changes until you choose something else:

- **Tap**: the flashlight on or off.
- **Hold** (about a second): Seek, the frequency search the radio calls SEARCH.

A radio updated from an earlier MM9PDY release or from the maker's firmware starts the same way, unless another
programming tool (CHIRP, for example, or the maker's software) has already stored one of the listed choices in the
radio's settings. Then the button does that choice from the start. Pick what you want in the menu as below.

## Choosing what the button does

1. Press **MENU**, go **DOWN** to **Radio Set** and press **MENU**.
2. Go to **PRESS SK2** (the tap) or **HOLD SK2** (the hold). They are right after PRESS SK1, the side key's setting.
3. Press **MENU**. The list is the same as the side key's, **FM RADIO**, **SCAN**, **SEARCH**, **VOX**, **LAMP**,
   **SOS**, then **QUICK ACCESS**, which opens the [Quick Access](quick-access.md) list. The highlighted one is what
   the button does now.
4. Move with **UP** and **DOWN** and press **MENU** to choose. The radio says *Save OK*. **EXIT** leaves the list
   without changing anything.

The choices are saved with the radio's other settings and kept when it is switched off.

## How it behaves

- **Tap and hold are separate.** Holding runs the hold's function once; the tap's function does not follow it, and
  holding longer does not repeat it.
- **Keypad lock.** The button follows the same rule as the side key: FM RADIO, LAMP and SOS still work with the keypad
  locked; SCAN, SEARCH, VOX and QUICK ACCESS give the lock beep.
- **While you transmit**, the button sends the repeater tone burst (Radio Set › ALERT) whatever you chose, as the
  maker's firmware does.
- **The flashlight** switches on and off; it no longer has a flashing setting. You can now switch it on or off during
  a scan too (the maker's firmware beeps and refuses). The side key set to LAMP switches the same flashlight.
- **SOS** still lights the flashlight while the alarm runs and puts it back as it was afterwards.
