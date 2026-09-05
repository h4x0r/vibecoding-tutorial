# 11. Staying maintainable

You have a working app. This chapter is about month three.

---

## The seven habits, collected

Every one of these appeared in the course at the moment it was needed. Here they
are together, in rough order of how much grief each saves.

### 1. Commit whenever something works

Not at the end of the day. At the moment it works.

A commit costs ten seconds and buys you a guaranteed return path. Without them,
"it worked an hour ago" is a memory. With them, it is a command:

```bash
git log --oneline
```

```bash
git checkout <the-commit-that-worked> -- .
```

The message matters as much as the commit. `update files` tells your future self
nothing. Ask for messages that say **why**.

### 2. One thing per branch, and look at the preview

The temptation is to ask for three features at once because it feels faster. It
is not: it produces a change too large to review, so you do not review it, and
unreviewed change is where unmaintainable begins.

Branch → push → preview link → look at it → merge. Every time.

### 3. Make it explain, and check you can follow

After anything you do not understand:

> Explain what you just changed and why, as if I have never seen this before.

There is a sharper version, and it is the real test:

> If I deleted this file, what would break?

An answer of "nothing" means the file should go. A vague answer means neither of
you knows what it is for, and that is worth finding out now rather than in
month three.

### 4. Ask what happens when it fails

The habit that produced the best code in this entire course:

> What happens if this gets a value it does not expect? Show me.

That question found `date-holidays` returning an empty list for an unknown
country, and `date-fns` turning `"2026-9"` into 31 August. **Both looked like
working code.** Neither would have thrown an error. Both would have shipped.

Errors announce themselves. Silence does not.

### 5. Keep `CLAUDE.md` short and scarred

Under 200 lines. Verifiable instructions. And every time something bites you,
add one line so it cannot bite twice:

```markdown
## Things that have already bitten us
- A table created by SQL gets no privileges on current Supabase and fails
  with `permission denied` until it is granted.
```

That is what makes the assistant get better at *your* project rather than
staying generically competent.

### 6. Test the things that would fail silently

You do not need to test everything. You need to test the code that could be
wrong without looking wrong: date arithmetic, anything parsing user input,
anything deciding who may see what.

And **make each test fail once on purpose.** A green suite you have never seen
go red is not evidence of anything.

### 7. Never let a secret near git

`.env.local` for keys. `NEXT_PUBLIC_` only for things you would print on a
poster. And check rather than trust:

```bash
git check-ignore -v .env.local
```

If a key ever does reach GitHub, **renaming or deleting it is not enough** —
force-pushing does not un-publish it, because old commits stay reachable. The
only real remedy is to rotate the key at the provider.

---

## A rhythm worth keeping

**Every session.** Start in the project folder. Check `git status` is clean
before you begin, so you know what you changed. Commit before you stop.

**Every few weeks.** Ask for a health check:

> Are any of our dependencies significantly out of date? Which updates are
> routine and which are likely to break something? Do not update anything yet.

The "do not update anything yet" matters. You want the assessment separately from
the change, so you can decide.

`date-holidays` is the specific one to watch in this app — its holiday data is
frozen into the installed version, so an old copy quietly serves last year's
rules.

**Before anything you care about.** From your project folder:

```bash
claude ultrareview
```

A multi-agent review of your current branch. When most of the code was not
written by you, having something adversarial read it before it goes live is the
cheapest safety net there is.

---

## Knowing when the assistant is wrong

It will be confidently wrong sometimes. The tells are learnable.

**It is most wrong about things that change.** Model training has a cutoff, and
the fastest-moving things — cloud APIs, authentication, key formats, pricing,
CLI flags — are exactly where confident memory is most dangerous.

This course met three of these head-on: `middleware.ts` renamed to `proxy.ts`,
Supabase's `eyJ…` keys superseded, the `think hard` ladder that never existed.
Next.js is worried enough about it to ship a file in every new project warning
assistants that their training data is stale.

**So: when it is about a vendor, make it check.**

> Before you write this, check the current documentation. Do not rely on what
> you remember about their API.

**Confidence is the signal, not the reassurance.** Being very sure about a
specific flag or key format that neither of you has looked at today is precisely
when to look it up.

**And run it.** The final authority is not the assistant and not the docs, it is
your terminal. `npm view <package> version` settles an argument about a version
number in one second.

---

## When it all goes wrong

It will. Here is the ladder, cheapest first.

**Undo uncommitted changes to one file:**

```bash
git checkout -- path/to/file
```

**Undo everything since the last commit:**

```bash
git reset --hard
```

(That throws away uncommitted work. That is the point, but be sure.)

**Undo a commit you already pushed**, without rewriting history:

```bash
git revert <commit>
```

**Find something you thought was lost.** `git reflog` lists everywhere you have
been, including commits no longer on any branch. Work is very rarely actually
gone.

**And the one that fixes most situations:** describe what happened to Claude
Code, paste the error, and ask for the *safest* option:

> This is broken and I do not know what I changed. Here is `git status` and
> the error. What are my options, safest first? Do not change anything yet.

"Do not change anything yet" is the important half. You want the diagnosis
before the surgery.

---

## What to build next

The calendar is a scaffold with obvious next steps, each teaching one new thing:

- **Real accounts** instead of anonymous ones, so appointments follow you
  between devices. Supabase does the work; you add a sign-in page.
- **Editing** an appointment, not just adding and deleting.
- **Recurring** appointments — genuinely harder than it sounds, and a good test
  of asking for edge cases first.
- **Sharing** a month as a read-only link, which forces you to think properly
  about what your policies allow.

Each is one branch, one preview link, one merge.

---

## The thing worth remembering

Vibecoding is not a lesser kind of programming. It is programming where the
typing is delegated and the *judgement* is not.

Everything in this chapter is judgement: what to check, when to be suspicious,
what to write down, what "working" means and how you would know. None of it
requires you to write the code, and none of it can be handed over — because the
assistant does not know what you meant, only what you said.

Six months from now, the difference between an app you can still change and an
app you are afraid of will not be the model you used. It will be whether you
committed when things worked, looked at the preview before merging, and asked
what happens when it fails.

---

**Appendices:** [when it breaks](appendix-a-when-it-breaks.md) ·
[glossary](appendix-b-glossary.md) ·
[what it costs](appendix-c-what-it-costs.md)
