# Installing a release

> **Release candidate docs: 1.2.0-rc.1** These pages describe a release candidate that is still being tested. For the current release, see [these docs](../../baofeng-dm32uv/install.md).

From nothing to a running radio, with [Codeplug Studio](https://codeplug.mm9pdy.net). Read
[README.md](README.md#read-this-first) first.

## 1. Get the stock v1.01.048 image

The image is Baofeng's and is not part of this project. Baofeng publishes it at
<https://baofeng.s3.amazonaws.com/Baofeng_DM-32UV_Firmware_v1.01.048.zip>.

Download it and keep the zip somewhere safe: it is also your way back to stock. Codeplug Studio checks the image inside
it:

| File | SHA-256 |
|---|---|
| `DM32_L01_048_20250821.bin` | `fda860febfcf1a234eed7fa73272112891074aac83746e4f8dfe224a2a700f8f` |

## 2. Save your codeplug

A firmware write does not touch the codeplug, but save a copy before your first write anyway: read the radio with
Baofeng's CPS or Codeplug Studio and save it to a file.

## 3. Flash with Codeplug Studio

Open [codeplug.mm9pdy.net](https://codeplug.mm9pdy.net) in Chrome or Edge on a desktop computer and choose
**Tools > Firmware flasher**. Close the CPS and anything else that might use the cable's port. Then follow the steps:

1. **Radio:** pick the Baofeng DM-32UV.
2. **Firmware:** pick a release. Finals are listed by default; **Show release candidates** adds the test builds.
   **Release notes** shows what the release contains and its known limits.
3. **Stock firmware:** drop the stock zip (or the `.bin`). Studio checks it and refuses any other version.
4. **Prepare:** Studio applies the release to your stock image on your computer and checks the result against the
   hash the release declares. Nothing is sent to the radio yet.
5. **Before you flash:** confirm the battery is full, the cable is direct and other programs are closed.
6. **Enter update mode**, in this order:
   1. Turn the radio **off** and leave the cable **out** of the radio.
   2. Hold **SK1** (the side key below the PTT) and **PTT** together, and turn the radio on.
   3. The LED lights **green**. Release the keys.
   4. **Now** plug the cable into the radio.

   The order matters: with the cable plugged in before power-on, the radio has been left unusable until it was
   power-cycled. To leave update mode without writing anything, turn the radio off.
7. **Flash:** pick the cable's port. The whole write takes about two minutes, starting with about 13 seconds while
   the radio erases. **Do not touch the radio or the cable until Studio says it has finished.**

If Studio stops with an error, go to [recovery.md](recovery.md) before trying anything else.

Baofeng's own guide says to factory-reset after an update. You do not need to: the radio has kept its channels and
settings after every update. A factory reset erases your codeplug.

## 4. Check it worked

1. Turn the radio off and on again. It should start normally with your channels and settings.
2. From 1.1.0: the **boot screen** shows `mm9pdy-` and the release at the bottom, for example `mm9pdy-1.1.0`, and
   **Settings > Device Info > Versions** shows `DM32.01.L01.048` (Baofeng's base, unchanged) with `mm9pdy-1.1.0` below
   it. Stock firmware never shows a `mm9pdy-` line.
3. For 1.0.0, which has no version line: press Scan on a channel with no scan list. A zone scan should start.

## 5. Updating to a newer release

Repeat section 3 with the newer release. You do not need to go back to stock first.

## Without Codeplug Studio

Codeplug Studio is the supported way to install a release. Each release's patch file is also in the
[releases folder](https://github.com/pskillen/mm9pdy-firmware/tree/main/releases/baofeng-dm32uv), with its SHA-256 in
`releases.json`. In Studio's flasher, **Advanced: use a patch file from disk** accepts a downloaded patch and
recognises a published one.
