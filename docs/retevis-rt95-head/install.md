# Installing

Steps marked *Not yet checked on a radio* are a plan, not a record. Steps marked *Checked on a radio once* were done once, with test builds that differ from a release only in the version line. Do not rely on any of it more than that.

You need: a charged battery or a stable supply, the programming cable, a computer with a Chrome-based browser, your own
copy of the stock front-panel firmware (version LCD V1.41, see [the first page](README.md#read-this-first)), and the
time to do it without being interrupted.

## 1. Before you start

1. **Not yet checked on a radio.** Check your radio's serial number against the table on [the first page](README.md#read-this-first).
2. **Not yet checked on a radio.** Make a backup of the codeplug with Codeplug Studio (Read, then save) or the official
   programming software.
3. **Not yet checked on a radio.** Make sure the stock firmware and the maker's programming software are to hand
   ([back-to-stock.md](back-to-stock.md)).

## 2. Write it with Codeplug Studio

1. **Checked on a radio once** (a test build). Open Codeplug Studio, *Tools*, *Firmware flasher*, and pick the Retevis RT95 front
   panel.
2. **Not yet checked on a radio.** Choose a release. Studio offers final releases; tick *show release candidates* to see
   test builds.
3. **Not yet checked on a radio.** Drop in your stock front-panel firmware files. Studio checks them against known
   fingerprints and refuses anything else.
4. **Not yet checked on a radio.** Answer Studio's questions about your radio (its serial number and the version shown on
   the radio's test screen). Studio will not go on if they do not fit.
5. **Checked on a radio once** (a test build). Put the radio into front-panel update mode with a cold start: remove the DC power, then hold **P1** and the
   knob (push) while you switch it on. The screen stays blank.
6. **Checked on a radio once** (a test build). Connect the cable, choose the port in Studio, and start the write. Do not touch the
   radio, the cable or the power until Studio says it is finished.
7. **Checked on a radio once** (a test build). The radio restarts by itself, in under a minute. If it does not, switch it off and on.

## 3. Check it worked

1. **Checked on a radio once** (a test build). The radio starts and shows its channel screen.
2. **Checked on a radio once** (a test build). Switch the radio off and on again and read the bottom of the power-on screen: it
   shows `MM9PDY-` and the version you wrote (for example `MM9PDY-1.0.0-RC.2`). It is only on screen for a moment.
3. **Not yet checked on a radio.** Hold **FUNC** and press **P4**: the test screen still shows the maker's version text.
   That is expected; the modification leaves it alone.
4. **Not yet checked on a radio.** Your channels and settings are as they were.

If anything is different or the radio does not start, go to [recovery.md](recovery.md).
