# Back to stock

Steps marked *Not yet checked on a radio* are a plan, not a record.

Going back means writing the maker's own front-panel firmware again. It leaves the codeplug alone.

## With Codeplug Studio

1. **Not yet checked on a radio.** Open *Tools*, *Firmware flasher*, and pick the Retevis RT95 front panel.
2. **Not yet checked on a radio.** Choose the stock firmware (version LCD V1.41) instead of a release, and drop in your
   own copy of the stock files.
3. **Checked on a radio once** (writing the stock V1.41 firmware with Studio). Put the radio into front-panel update mode (remove the DC power, then hold **P1** and the knob
   while you switch on; the screen stays blank), connect the cable, and write, as in [install.md](install.md).
4. **Checked on a radio once** (writing the stock V1.41 firmware with Studio). The radio restarts running the maker's firmware.

## The radio board (RF CPU)

If you put the optional audio level meter update on the radio board ([install.md](install.md#the-radio-board-rf-cpu-update-for-the-audio-level-meter)), you can take it off by writing the maker's stock radio board firmware again. The front panel is separate: you can leave it as it is.

1. **Not yet checked on a radio.** In Studio, *Tools*, *Firmware flasher*, pick the Retevis RT95 main board (RF CPU)
   and choose the stock radio board firmware option instead of a release. Drop in your own copy of the stock files.
2. **Not yet checked on a radio.** Enter radio board update mode with a cold start, as in install.md; the screen must
   read `UPDATE THE` and `RF CPU`. Studio asks for the calibration backup before any write to the radio board. Connect the cable and write.
3. **Not yet checked on a radio.** Switch the radio off and on. With the stock radio board firmware the audio level
   meter is simply not shown; nothing else changes.

## With the maker's tool

If Studio cannot be used, the maker's own programming software for the radio can write the same stock files.

1. **Not yet checked on a radio.** Install the maker's programming software and have your stock firmware files ready.
2. **Not yet checked on a radio.** Put the radio into front-panel update mode as above (cold start).
3. **Not yet checked on a radio.** Follow the software's firmware update steps for the front panel only. Do not update
   the radio board's firmware.

If the radio will not start, see [recovery.md](recovery.md).
