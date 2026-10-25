# Agent guide: mm9pdy-firmware (public)

The public face of the MM9PDY firmware mods: release patches, `releases.json` (what Codeplug Studio reads), and each
radio's user manual. **Everything here is public.**

- `releases/` and `docs/<radio>/` (and `docs/rc/`) are written by the release workflows of the private radio repos on
  every tag. Don't edit them here: change the radio repo's `docs/public/` and release.
- Edit by hand only `README.md` (the front page), `LICENSE.md`, the `tools` folder and this file.
- Run `python3 -I tools/release_index.py check` before pushing.
- Nothing about internals: no addresses, no RE findings, no owner data. Links into the private repos don't work for
  readers here.

The house rules below are shared with the private repos. "Docs branches may be pushed freely here" (owner,
2026-10-25); merging to `main` is the owner's call.

<!-- BEGIN house-rules: synced from pskillen/firmware-mods workspace/house-rules.md; do not edit here -->

## House rules (all radio repos)

Shared by every repo under `~/git/radios/`. Source: `pskillen/firmware-mods`, `workspace/house-rules.md`; copied into
each repo's `AGENTS.md` by its `sync-house-rules.py` script. Edit it there, not here. This repo's own rules, above or below
this section, win on anything about this repo.

**The repos.** `firmware-mods` (shared spec, ways of working, the `radios` Claude plugin), `anytone-d890-firmware`,
`baofeng-dm32-firmware`, `codeplug-studio`, and `mm9pdy-firmware` (public: releases and user manuals). How we work:
[firmware-mods/ways-of-working](https://github.com/pskillen/firmware-mods/blob/main/ways-of-working/README.md).

**Talking to the owner.** The owner often reads on a phone.

- First line: what you need from them, or "nothing". At most 15 lines; detail goes in a file.
- Questions numbered, each with your recommendation, so "1 yes, 2 b" is a full answer.
- Send any file they must read; don't just name a path. Links as full URLs.
- Never use a tool that shows a card to click or fill in (question pickers, plan approval, MCP forms). Ask in text.

**Git.**

- Never commit to `main`. Work on a branch; one PR per delivery per repo.
- Long deliveries go as a **linear stack** of PRs: each PR's base is the one below; every PR body starts with the
  stack line and merge order.
- **Rebase, never merge, into feature branches.** When the base moves, rebase onto it (`git rebase --onto` up a
  stack) and push with `--force-with-lease`. Tell any session whose branch sits on yours first. No "Update branch"
  button, no merging `main` in.
- **Into `main`: a merge commit,** the only place merge commits belong. Squash only when a branch's history isn't
  worth keeping. The owner merges unless they've said otherwise.
- **No attribution lines** (`Co-Authored-By`, "Generated with ...") in commits or PR bodies.
- GitHub through the `gh` CLI. `gh issue view` off a TTY drops the body: use `--json title,body,comments`.

**Scratch work** lives in the repo's gitignored `tmp/`: `tmp/investigations/<topic>/`, `tmp/features/<topic>/`, and
`tmp/agents/` (who is working here). Worktrees symlink the main checkout's `tmp/`. Notes become durable docs once
delivery starts. Never link to `tmp/` from anything committed.

**User-facing changes ship their public docs in the same PR:** manual pages, screenshots from the demo codeplug,
release-notes line, feature-list rows. Public docs: no internals, no private links, no owner data.

**Never** flash a radio or open its serial port (the owner does that, from a PR's CI artifact via Codeplug Studio),
and never commit vendor firmware.

**Claude Code:** install the `radios` plugin for the role agents and skills:
`claude plugin marketplace add pskillen/firmware-mods`, then `claude plugin install radios@mm9pdy`.

<!-- END house-rules -->
