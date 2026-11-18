---
version: 1.2.0
channel: final
stock: MAIN V1.61 (20231202)
published: 2026-11-18
summary: The radio board (RF CPU) update for the audio level meter in front-panel release 1.2.0.
verify: With front-panel release 1.2.0 and MTR set to ON in the FUNC MENU, the audio level meter appears in single watch while receiving a signal.
---

Release 1.2.0 of the Retevis RT95 radio board (RF CPU) update. It applies to the stock radio board firmware **MAIN V1.61** (20231202) only. Its one change: it reports the received audio level and your microphone level to the front panel, for the audio level meter in front-panel release 1.2.0. Everything else on the radio board is as the maker made it.

**How far it has been checked:** checked in an emulator and used on a radio with test builds during development. There was no separate release candidate.

**Before you start:** Codeplug Studio asks you to save this radio's calibration backup and to type the serial number from the label. Keep the backup somewhere safe. Install the front-panel release first, then this one: the RT95 user guide's install page has the steps.

**Checking it worked:** set MTR to ON in the FUNC MENU. While the radio receives a signal (the RX tag lit), the row under the signal bars shows nine level segments in single watch.

**Without the front-panel release** (or with MTR off), nothing changes on the screen and the radio works as stock.

**Going back:** write the maker's stock radio board firmware (MAIN V1.61) with Codeplug Studio, as the RT95 user guide's back-to-stock page describes.
