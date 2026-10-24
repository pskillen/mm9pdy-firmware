# Installing a release

From nothing to a running radio, with [Codeplug Studio](https://codeplug.mm9pdy.net). Read
[README.md](README.md#read-this-first) first.

## 1. Get the stock V1.05 package

The package is AnyTone's and is not part of this project. The US distributor hosts it as
`D890UV V1.05 DMR official release 260521.zip` at
<https://anytoneusa.com/Files/D890UV%20V1.05%20DMR%20official%20release%20260521.zip>.

Download it and keep the zip somewhere safe: it is also your way back to stock. Codeplug Studio checks the three
files it needs from it:

| File | SHA-256 |
|---|---|
| `D890UV_V1.05_20260521.CDD` | `6d84926eecf309b25f68287d3521adaae2765f171db9d9f6a1358a454c71c96e` |
| `D890UV_V1.05_20260521.CDI` | `b24dd25aa02d0d72b6ba32b3b6c0d08d787f40248c80132cc4d5d7942c0470de` |
| `D890UV_V1.05_20260521.spi` | `857771404d6ac1e38c9427ae1735007af0d174e27fc59fa1dfa1881560319c8a` |

## 2. Save your codeplug

A firmware write does not touch the codeplug or the calibration, but save a copy before your first write anyway. In
the official CPS, read the radio and save the codeplug to a file. If you use Codeplug Studio for your codeplug, its
build for this radio has a Backup tab.

## 3. Flash with Codeplug Studio

Open [codeplug.mm9pdy.net](https://codeplug.mm9pdy.net) in Chrome or Edge on a desktop computer and choose
**Tools > Firmware flasher**. Close the CPS and anything else that might use the radio's port. Then follow the steps:

1. **Radio:** pick the AnyTone AT-D890UV.
2. **Firmware:** pick a release. Finals are listed by default; **Show release candidates** adds the test builds.
   **Release notes** shows what the release contains and its known limits.
3. **Stock firmware:** drop the stock zip (or the three files). Studio checks every file and refuses any other version.
4. **Prepare:** Studio applies the release to your stock files on your computer and checks the result against the
   hashes the release declares. Nothing is sent to the radio yet.
5. **Before you flash:** confirm the battery is full, the cable is direct and other programs are closed.
6. **Enter update mode:** switch the radio off, hold **PTT and PF3**, and switch it on. Keep holding for 2 to 3
   seconds. The **red LED blinks** and the **screen stays blank**; there is no sound. Then plug in the cable. If the
   screen shows anything, switch off and try again.
7. **Flash:** pick the radio's port. The transfer takes about 25 seconds. **Do not touch the radio or the cable until
   Studio says it has finished.** At the end the radio restarts by itself and its USB port disappears; that is normal.

If Studio stops with an error, go to [recovery.md](recovery.md) before trying anything else.

## 4. Check it worked

1. If the radio does not show the power-on screen by itself, switch it off and on again normally, without holding any
   keys.
2. The **power-on screen** shows the release name along the bottom: `mm9pdy-` and the release, for example
   `mm9pdy-1.1.0`.
3. **Menu > Settings > Device Info**: "Firmware Ver:" still shows **Ver 1.05** (the stock firmware the release is
   built on), and the next item, **Mod Ver:**, shows the same release name. Release 1.0.0 has no Mod Ver item: the name
   is under "Version" instead.
4. The radio reaches the channel screen with your channels, zones and settings as before.

If the release name is missing, the radio is still on its old firmware: the write did not happen.

## 5. Set up the mods

The mods that need a key do nothing until you assign one. In the CPS, assign Record Switch, Record and Priority Zone
to the keys you want and write the codeplug as usual. See [features.md](features.md#1-setting-up-keys-in-the-cps).

## 6. Updating to a newer release

Repeat section 3 with the newer release. You do not need to go back to stock first. Your codeplug and the mods'
settings stay as they are.

## Without Codeplug Studio

Codeplug Studio is the supported way to install a release. Each release's patch file is also in the
[releases folder](https://github.com/pskillen/mm9pdy-firmware/tree/main/releases/anytone-at-d890uv), with its SHA-256
in `releases.json`. In Studio's flasher, **Advanced: use a patch file from disk** accepts a downloaded patch and
recognises a published one.
