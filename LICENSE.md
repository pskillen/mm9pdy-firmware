# Licence

Copyright (c) 2026 Patrick Skillen (MM9PDY).

This repository holds three kinds of material under different terms.

## Documentation and release notes

Everything under `docs/`, the release notes (`releases/**/*.md`), and the README files are licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International licence](https://creativecommons.org/licenses/by-sa/4.0/)
(CC BY-SA 4.0).

## Release patches

The release patches (`releases/**/*.patch.json`) and the release index (`releases.json`) may be used, copied and
redistributed, by anyone, for any purpose, free of charge, provided they are **not modified** and this notice goes with
them. A modified patch is not a release of this project and must not be presented as one.

A patch holds this project's own code, where it goes, and SHA-256 hashes of the manufacturer files it applies to and
of the result. Some patches also hold a few bytes of the original at each place they change, so that the patch tool
can refuse to apply to the wrong file. A patch cannot be used without the manufacturer's firmware, and grants no rights
in it. The manufacturer's firmware remains the manufacturer's, under
the manufacturer's terms, and you obtain it from them yourself.

## Tools

The scripts in the tools folder and the GitHub workflow files are licensed under the MIT licence:

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
> documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
> rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
> permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
> Software.

## No warranty

ALL OF THE ABOVE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE MATERIAL OR ITS USE. **Flashing firmware can leave a radio
unusable.** You do so entirely at your own risk.
