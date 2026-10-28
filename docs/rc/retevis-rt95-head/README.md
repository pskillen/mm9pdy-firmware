# Retevis RT95 front panel (MM9PDY)

> **Release candidate docs: 1.0.0-rc.2** These pages describe a release candidate that is still being tested.

A small, free modification for the front panel (the "head", with the screen, keys and knob) of the Retevis RT95 and the
AnyTone AT-778UV it is built on. It is applied to the **stock front-panel firmware, version LCD V1.41**, and leaves the
radio board's own firmware (the "RF" side) exactly as the maker made it.

**Very little here has been checked on a radio.** A test build was written once with Codeplug Studio and worked. Every
step not yet seen on a radio is marked *Not yet checked on a radio*; the others say they were checked once.

## Pages

| Page | What it is for |
|---|---|
| [features.md](features.md) | What the modification does (release 1.0.0-rc.2: the version line on the power-on screen, nothing else) |
| [install.md](install.md) | Putting it on the radio with Codeplug Studio |
| [back-to-stock.md](back-to-stock.md) | Putting the maker's firmware back |
| [recovery.md](recovery.md) | If the radio does not start after a write |

## Read this first

- **It is a risk.** Writing firmware can leave a radio that does not start. There is a way back
  ([recovery.md](recovery.md)), but you accept the risk, and it is your radio. Nothing here is a promise.
- **Stock LCD V1.41 only.** The modification applies to a front panel running the stock version LCD V1.41 (dated
  2023-12-02). Codeplug Studio checks this before it writes anything and refuses anything else.
- **Check your radio's revision first.** Retevis has made three revisions of the RT95, told apart by serial number
  (the first six digits are the year and month: 202101 means January 2021):

  | Serial | Revision | Notes |
  |---|---|---|
  | before 202101 | 1 | No VOX. Retevis's 2024 firmware set is reported to **brick** these radios |
  | 202101 to 202312 | 2 | The revision Retevis's 2024 firmware set is issued for |
  | 202401 onward | 3 | Already has the mic gain that set adds; that set may not match |

  Never flash a front-panel image made for a different model or revision, and never the AT-778UV front-panel firmware
  onto an RT95: it is for a different chip and the radio will stop with a model error. If you are unsure which you have,
  do not write.
- **No maker firmware is published here.** You supply your own copy of the stock front-panel firmware; Codeplug Studio
  checks it against known fingerprints. Ask Retevis support for it, or use the unofficial mirror Studio lists (which is
  not run by us).
- **Writing firmware does not touch your codeplug.** Channels, contacts and settings stay as they are. Take a backup
  with Codeplug Studio or the official CPS before you start anyway.
- **Keep a way back.** Keep the stock firmware file and the maker's programming software where you can reach them
  ([back-to-stock.md](back-to-stock.md)).
- **Release candidates** (versions ending `-rc.1`, `-rc.2`, ...) are for testing. Studio shows them only when you ask.
  A release candidate may have faults.

The release name the radio shows is `mm9pdy-` followed by the version, for example `mm9pdy-1.0.0`.
