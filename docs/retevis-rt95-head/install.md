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
4. **Not yet checked on a radio.** Answer Studio's questions about your radio. Studio will not go on if they do not fit:
   - the serial number is 21xx or later (**never flash a radio with a serial number before 2101**);
   - the test screen (hold **FUNC** and press **P4** while switching on) shows `LCD CPU V1.11` and `RF CPU V1.11`;
   - Studio's "Check the radio" test, made with the radio in its normal mode, finds the radio.
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

## The radio board (RF CPU) update, for the audio level meter

**Optional.** Everything above works without it. The audio level meter needs it, and nothing else does. It adds one
small piece to the radio board's firmware so that the front panel can show audio levels; it changes nothing else. It
applies to the maker's stock radio board firmware, version V1.61 (dated 2023-12-02), and Codeplug Studio refuses anything
else. Do the front-panel steps above first.

**Not yet checked on a radio.** Every step below is a plan, not a record.

1. **Not yet checked on a radio.** Before it starts, Codeplug Studio asks you to save this radio's calibration backup
   and to type the serial number from the label on the radio. It will not go on without them. Keep the calibration backup
   somewhere safe. Studio cannot yet restore it by itself; if something goes wrong, ask for help (see
   [recovery.md](recovery.md)) with the backup to hand.
2. **Not yet checked on a radio.** In Studio, *Tools*, *Firmware flasher*, pick the Retevis RT95 main board (RF CPU)
   and choose a release. Drop in your own copy of the stock files, as for the front panel.
3. **Not yet checked on a radio.** Put the radio into radio board update mode with a cold start: remove the DC power
   completely, then switch on with the keys Studio names held down (**P3** and the knob push). **The screen must read
   `UPDATE THE` and `RF CPU`.** If the screen is blank, stop: that is the front panel's update mode, not this one.
   Switch off and start again.
4. **Not yet checked on a radio.** Connect the cable, choose the port in Studio and tick *UPDATE THE RF CPU* (the
   screen says so) and start the write. It takes about 20 seconds. Do not touch the radio, the cable or the power until Studio says it is finished.
5. **Not yet checked on a radio.** When Studio is finished, switch the radio off and on again.

To check it: **not yet checked on a radio.** First set MTR to ON in the FUNC MENU (the meter is off until you do). Then,
while the radio is receiving a signal with the RX tag lit, the audio level meter appears. Your channels and settings are as they were. If the radio does not start, go to
[recovery.md](recovery.md#the-radio-does-not-start-after-a-radio-board-rf-cpu-update).
