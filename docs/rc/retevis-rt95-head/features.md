# What it does

> **Release candidate docs: 1.0.0-rc.2** These pages describe a release candidate that is still being tested.

Release 1.0.0-rc.2 is the unmodified front-panel firmware plus one change: the version line below. Nothing else is changed.

Each feature adds a row to this table in the release that ships it, and the row says how far it has been checked.

| Feature | What you see | Since | Checked on a radio |
|---|---|---|---|
| [Version on the power-on screen](#version-on-the-power-on-screen) | A small line along the bottom of the power-on screen: `MM9PDY-` and the firmware version | 1.0.0-rc.2 | Once, on a test build; not yet on this release candidate |

The vendor's own version text (what the official programming software and Codeplug Studio read from the radio) is not
changed. The release name appears separately, as `mm9pdy-` plus the version (shown in capitals on the power-on screen).

## Version on the power-on screen

**Checked on a radio once**, on a test build that differs from this release candidate only in the text of the line. Not yet checked on the release candidate itself.

When the radio starts, the power-on screen shows its usual text (RETEVIS, or your own) and, in small letters along the
bottom, `MM9PDY-` followed by the firmware version. The line stays as long as the power-on screen does. The radio's
small text is capitals only, so it reads in capitals.

| Firmware | The line reads |
|---|---|
| A release | `MM9PDY-1.0.0` |
| A release candidate | `MM9PDY-1.0.0-RC.2` |
| A test build | `MM9PDY-G` followed by a code, such as `MM9PDY-G1A2B3C` |

Where to look: the power-on screen only. The radio has no version page of its own, and the maker's test screen (which
you reach by holding **FUNC** and pressing **P4**) keeps showing the maker's version text; do not use it to check this
feature. Everything else on every screen is as before.
