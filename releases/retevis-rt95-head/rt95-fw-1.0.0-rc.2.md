---
version: 1.0.0-rc.2
channel: rc
stock: LCD V1.41 (20231202)
published: 2026-10-28
summary: Release candidate 2: the first published build. The radio works as stock, and the power-on screen shows which firmware is installed.
verify: The bottom of the power-on screen shows "MM9PDY-1.0.0-RC.2".
---

The first release candidate of the Retevis RT95 front-panel modification, for testing. It applies to the stock front-panel firmware **LCD V1.41** (20231202) only, and leaves the radio board's firmware alone.

**How far it has been checked:** this exact build has been checked in an emulator only. A test build that differs from it only in the version line was written to a radio once with Codeplug Studio and worked. Nothing else has been tried on a radio.

**What's in it**

- **Everything else as stock:** the radio works as it does with the maker's front-panel firmware. The channels, the menus and the radio's own version text are unchanged.
- **Version on the power-on screen:** the bottom of the power-on screen shows `MM9PDY-1.0.0-RC.2`, so you can tell which firmware is installed. The radio's small text is capitals only.

**Known limits**

- The version line is only on the power-on screen, for as long as that screen stays up.
- The test screen (**FUNC** and **P4**) keeps showing the maker's version text. That is expected.

**Checking it worked:** switch the radio off and on and read the bottom of the power-on screen: it shows `MM9PDY-1.0.0-RC.2`.

**Going back to stock:** write the maker's stock front-panel firmware (LCD V1.41) again with Codeplug Studio, or use the maker's own tool.
