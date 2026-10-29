# Recovery

**Not yet checked on a radio.** Every step below is a plan, not a record.

## The radio does not start, or shows an error after a write

1. **Not yet checked on a radio.** Switch it off and leave it a minute. Check the battery or supply. Switch it on again.
2. **Not yet checked on a radio.** If it shows a model or version error, the front-panel firmware is wrong for this
   radio. Do not switch it off and on repeatedly: go to step 3.
3. **Not yet checked on a radio.** Switch off, hold **P1** and the knob (push), switch on. If the screen stays blank, the
   radio is waiting for a front-panel firmware write. Write the stock firmware again as in
   [back-to-stock.md](back-to-stock.md).
4. **Not yet checked on a radio.** If Studio will not write, use the maker's programming software for the same stock
   write.

## The write stopped half way

The front-panel update mode is still there after a failed write. Do not unplug the radio or switch it off to "try
again" more than once: switch off, enter update mode as above, and write the stock firmware again.

## Things to avoid

- Do not hold **FUNC** and **P6** while switching on: that resets the radio to factory settings.
- Do not use the radio board's update mode (**P3** and the knob at power on) for anything here. Nothing in this project
  writes the radio board.
- Do not write firmware made for another model or revision.

If none of this works, ask for help with the radio's serial number, the version shown, and what the screen did.
