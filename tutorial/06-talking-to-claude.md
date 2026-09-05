# 6. Talking to Claude Code

This is the chapter that decides whether your app is maintainable. Not because
of anything clever — because of five settings and one file.

---

## Starting it

Make a folder for your work and go into it:

```bash
mkdir -p ~/code
```

```bash
cd ~/code
```

```bash
claude
```

The first run asks you to pick a colour theme and then to log in, which opens
your browser. You need either a Claude subscription or an Anthropic API account.

From now on, `claude` started **inside a project folder** gives you an assistant
that can see that project. That is the whole idea: it is not a chat window that
happens to know about code, it is a thing sitting inside your project with the
ability to read and change it.

Two things to know immediately:

- **`/` opens the command menu.** Everything below starting with `/` is typed
  into Claude Code, not into the terminal.
- **`Escape` interrupts.** If it is doing something you did not want, stop it.
  You do not have to let it finish.

---

## Which model

Type `/model` for a picker, or name one directly:

```
/model fable
```

The names you can type are `default`, `best`, `fable`, `sonnet`, `opus`,
`haiku`, and `opusplan`.

**Use `fable`.** At the time of writing the newest and most capable model in
Claude Code is **Fable 5.1**, and `fable` is an alias that always points at the
newest Fable. Type the alias rather than the full `claude-fable-5-1`, so that
you follow the newest model automatically as you update.

**If Fable 5.1 gives you an error**, your Claude Code is too old. The message is
unhelpful — a raw `API Error: 400 ... does not support this model`. The fix:

```bash
claude update
```

This is exactly the trap chapter 4 mentioned: installed one way, Claude Code
updates itself; installed another way, it sits still until this happens.

**`opusplan` is worth knowing about.** It thinks with the expensive model and
executes with the cheaper one. If you are paying per token and want a sensible
default, it is a better one than most people use.

---

## How hard it thinks

Separately from *which* model, you can set **how much effort it spends**.

```
/effort
```

with no argument opens a slider. Or set it directly:

```
/effort xhigh
```

The levels are `low`, `medium`, `high` (the default), `xhigh`, and `max`.

The practical advice:

| When | Use |
|---|---|
| Renaming things, small edits, tidying | `/effort low` or `medium` |
| Normal building | `/effort high` |
| A design decision, a nasty bug, anything security-shaped | `/effort xhigh` |

**`xhigh` before something hard is the highest-leverage habit in this chapter.**
It costs more and takes longer, and it is worth it precisely when you are least
able to check the answer yourself.

---

## `ultrathink`, and a myth to unlearn

Put the word **`ultrathink`** anywhere in a message and Claude Code will reason
harder on that one turn:

```
ultrathink — is storing the locale in a cookie the right call here, or
should it be in the database? What breaks with each?
```

It is per-message, free, and does not change your session setting.

Now the myth. **You will read, in post after post, that there is a ladder:
`think` → `think hard` → `think harder` → `ultrathink`.**

**There is no ladder.** The documentation is explicit that phrases like `think`
and `think hard` are passed through as ordinary prose and are not recognised as
keywords at all. Only `ultrathink` does anything.

If you have been sprinkling "think hard about this" into prompts believing it
was a switch, it has been doing nothing beyond the ordinary meaning of the
words.

One more distinction worth holding, because they are complementary rather than
alternatives:

- **`/effort xhigh`** changes the reasoning budget sent to the model, for the
  session.
- **`ultrathink`** adds an instruction to think harder, for one message, without
  changing that budget.

Using both on a genuinely hard question is reasonable.

---

## `ultracode`

**`ultracode` is two different things**, and confusing them is expensive.

**As a keyword in a message**, it runs *that one task* as a coordinated
workflow — Claude plans out sub-tasks and runs several agents in parallel — and
leaves your session settings alone:

```
ultracode: go through every file in lib/ and check each function that
takes a country code actually rejects an unknown one
```

**As a session setting** (`/effort ultracode`), it turns that on for *every*
substantial request until you change it. It combines `xhigh` reasoning with
automatic workflow orchestration, so it is powerful and genuinely expensive.

Start with the keyword. Reach for the setting only when an entire session is
going to be hard.

> **A small trap:** typing the word while merely *discussing* it will trigger
> it. Press **Option-W** to dismiss that for the message, or turn off "Ultracode
> keyword trigger" in `/config`. If you paste a paragraph of this tutorial into
> Claude Code, expect it to fire.

---

## Skills, and the one that stops your app looking like everyone else's

Vibecoded apps have a look. Same fonts, same soft purple gradient, same rounded
cards. It is the visual equivalent of a stock photo, and it is the fastest way
to signal that nobody made a decision.

There is a skill for that. Install it once:

```
/plugin install frontend-design@claude-plugins-official
```

Then, when you want it:

```
/frontend-design:frontend-design
```

The doubled name is the plugin name and the skill name — nobody guesses it, so
copy it. It also fires by itself when you ask for a page or a component.

What it actually does is forbid the defaults. It explicitly rules out the
overused fonts — Inter, Roboto, Arial, the system stack — and the clichéd colour
schemes, and pushes for one committed aesthetic direction rather than a
compromise.

The calendar in this course was built with it. The aesthetic it chose was
"red-letter day": paper and ink, holidays in vermilion, because in hand-written
calendars holy days were literally inked in red. **That idea belongs to this
app.** You could not paste it onto a different one, which is precisely what
makes it not look generic.

---

## `CLAUDE.md` — the file that makes this maintainable

Here is the failure this prevents.

Week one, you and the assistant agree on something: run the tests before
committing, never use raw colour codes, always add holidays on the server.
Week three, in a new session, it knows none of that. It was never told; it was
told *you*, and you are not the thing that persists.

**`CLAUDE.md` is a file in your project that Claude Code reads at the start of
every session.** It is the project's standing instructions.

Create a starting one by running, inside your project:

```
/init
```

It reads your code and writes a first draft — build commands, how to run tests,
the layout. Then you edit it as you learn things.

Four rules for keeping it useful:

**Keep it under 200 lines.** This is the documented guidance, and the reason is
worth understanding: `CLAUDE.md` is *context*, not enforced configuration. A
long file consumes attention and measurably reduces how reliably it is followed.
The natural failure is to keep appending rules until it is enormous and ignored.

**Write things that can be checked.** "Run `npm test` before committing" is
followable. "Write good tests" is not.

**Record what bit you.** The most valuable lines are the scars. From this
project's real file:

```markdown
## Things that have already bitten us

- `parse("2026-9", "yyyy-MM")` returns 2026-08-31, not an error. date-fns is
  lenient and hands back a plausible wrong answer.
- A table created by SQL gets no privileges on current Supabase and fails with
  `permission denied` until it is granted.
```

Each of those cost real time once. Written down, they cost nobody time again.

**Know which file you are editing.** There are two:

| File | Applies to | Committed to git? |
|---|---|---|
| `./CLAUDE.md` | this project | **yes** — shared with anyone who clones it |
| `~/.claude/CLAUDE.md` | every project you ever work on | no, it is yours |

Personal preferences go in the second. Project rules go in the first. Putting
personal habits in the project file publishes them to everyone.

Check what actually loaded with `/context`, under "Memory files".

> Next.js now writes its own instructions file too. A new project contains
> `AGENTS.md` beginning **"This is NOT the Next.js you know — APIs, conventions,
> and file structure may all differ from your training data."** The framework
> itself is warning AI assistants that their knowledge is out of date. Leave it
> alone; it is doing you a favour.

---

## How to ask for things

**Say what you want, not how to build it.** "The month should be in the URL so I
can bookmark it" beats "add a useState for the month". You are describing the
outcome; the how is its job.

**One thing at a time.** A request with four features in it produces a change
you cannot review. You will not read it, and not reading it is where
unmaintainable begins.

**Ask it to explain, always.** After anything you do not follow:

> Explain what you just changed, and why, as if I have never used React.

**Ask it to disagree with you.** This is the underused one:

> I want to store appointments in the browser's local storage. ultrathink —
> what breaks, and is there a better option?

An assistant that only agrees is a very expensive yes-man. The calendar in this
course stores its locale in a cookie rather than local storage, and the reason
came from exactly this question.

---

## One more command worth knowing

```bash
claude ultrareview
```

Run from your project, this launches a multi-agent review of the work on your
current branch and prints what it finds. When you have written code you do not
fully understand — which, vibecoding, is most of it — having something
adversarial read it before it goes live is the cheapest safety net available.

---

## Your settings, before chapter 7

```
/model fable
```

```
/effort high
```

```
/plugin install frontend-design@claude-plugins-official
```

And `ultrathink` in your pocket for the hard questions.

The official documentation is at **code.claude.com/docs** — note that host; the
older `docs.claude.com/en/docs/claude-code` addresses now redirect there, and
redirects are the first thing to rot.

---

**Next:** [7. Build the calendar →](07-build-the-calendar.md)
