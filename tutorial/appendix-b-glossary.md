# Appendix B — Glossary

Written for someone who has never read a technical document. Where a word has a
loose everyday meaning and a precise one here, both are given.

---

## The terminal

**Terminal** — The Mac app where you type instructions instead of clicking. Not
a separate computer; the same files, described in words.

**Command** — One instruction, typed and run with Return.

**Prompt** — The `%` (sometimes `$`) waiting for you to type. **When you cannot
see it, the computer is still busy.** Copied commands often show a leading `$`;
that symbol is not part of the command.

**Shell** — The program interpreting what you type. On modern Macs, `zsh`.

**Directory** — A folder. `pwd` says which one you are in, `ls` lists it, `cd`
moves you.

**`~`** — Your home folder: the one with Desktop, Documents, Downloads.

**Flag** — A modifier after a command, usually with dashes. In
`npm install -D vitest`, the `-D` is a flag.

**`sudo`** — "Do this as administrator." Asks for your Mac password and shows
nothing as you type it. Treat every `sudo` command as worth understanding first.

**Control-C** — Stops whatever is running. Not ⌘-C.

---

## Code and tools

**JavaScript** — The language the web is written in. **TypeScript** is
JavaScript with labels saying what kind of thing each value is, so mistakes are
caught before the code runs.

**Node** — Runs JavaScript on your computer rather than in a browser.

**npm** — Downloads other people's code. Also the command you run to do it.

**`npx`** — Runs a tool once without installing it permanently.

**Package** — Someone else's code you can use. **Dependency** — a package your
project needs.

**`package.json`** — The list of your project's dependencies and commands.
**`package-lock.json`** — the exact versions actually installed. Commit both.

**Framework** — A pre-built structure you fill in. **Next.js** is the one here.

**React** — The library for building interfaces out of reusable pieces called
**components**.

**Component** — One reusable piece of a page. A button, a day cell, a whole grid.

**Tailwind** — A way of styling by putting many small class names directly on
elements (`className="mt-4 text-sm"`) rather than in a separate stylesheet.

**shadcn/ui** — Ready-made components you copy *into* your project rather than
install. Because they are your files, you can change them.

**Build** — Turning your source code into the optimised version that actually
gets served. `npm run build`.

**Bundle** — The JavaScript sent to a visitor's browser. Its size is how long
they wait.

---

## Git and GitHub

**Git** — Keeps every version of your project. Runs on your Mac. No account.

**GitHub** — A website holding a copy of your Git history. What Vercel watches.

**Repository / repo** — One project plus its entire history.

**Commit** — A save point, with a note about what changed. Permanent.

**Branch** — A parallel line of work that does not affect `main` until merged.

**`main`** — The branch that is the real, published version.

**Push** — Send your commits to GitHub. **Pull** — bring GitHub's down.

**Pull request (PR)** — A proposal to merge a branch, with a page to discuss and
review it. Where the preview link appears.

**Merge** — Fold a branch's changes into `main`.

**`.gitignore`** — A list of files Git must never save. Your keys live in one.

**Diff** — What changed between two versions.

---

## The web

**Server** — A computer, somewhere, that answers when a browser asks. **Client**
— the visitor's browser.

**Server component / client component** — In Next.js, code that runs on the
server before sending HTML, versus code sent to the browser to run there. The
distinction has a measurable cost: chapter 9's holiday library was 1.4 MB that
never had to travel.

**`localhost`** — Your own machine. `http://localhost:3000` is visible only to
you.

**Deploy** — Publish a version so the world can reach it.

**Production** — The real, live site. **Preview** — a complete copy at its own
address, for trying a change first.

**Environment variable** — A setting kept outside the code, usually because it
differs between your machine and the live site, or because it is secret.

**`NEXT_PUBLIC_`** — A prefix meaning "compile this into the browser." Anything
with it is genuinely public. **Never put a secret in one.**

**Cookie** — A small piece of data the browser stores and sends back with every
request, so the server can read it while building the page.

**API** — A way for one program to ask another program for something.

---

## Databases

**Database** — Storage built for many small records that arrive while the app is
running and must be found again quickly.

**Postgres** — The specific database used here. **Supabase** wraps it in a
website and adds logins.

**Table / row / column** — A sheet, one record in it, one field every record has.

**Query** — A question asked of the database.

**SQL** — The language questions and changes are written in.

**Migration** — A saved file describing a change to the database's shape, kept in
your repository so the change is reviewable and repeatable.

**Schema** — The overall shape: what tables exist, with what columns.

**Row Level Security (RLS)** — Rules, enforced inside the database, about which
rows each user may see or change. **Off by default on tables created by SQL**,
which is the most consequential fact in this glossary.

**Policy** — One RLS rule. `using` picks which existing rows you may touch;
`with check` decides which new rows you may write.

**Grant** — Permission to touch a table at all. Separate from RLS; both needed.

**Publishable key** — Identifies your Supabase project. Safe in a browser.
**Secret key** — full access, server only, never in git.

---

## AI assistance

**Claude Code** — The assistant, running in your terminal, able to read and
change your project.

**Model** — Which version of Claude. `fable` is an alias always pointing at the
newest and most capable.

**Effort** — How much thinking to spend: `low`, `medium`, `high`, `xhigh`,
`max`. Set with `/effort`.

**`ultrathink`** — A real keyword. Put it in a message for deeper reasoning on
that turn. **`think hard` and `think harder` are not keywords** and do nothing.

**`ultracode`** — Two things: a keyword that runs one task as a coordinated
multi-agent workflow, and a session setting (`/effort ultracode`) that does it
for everything. The keyword first.

**Skill** — A packaged set of instructions for a kind of task.
`frontend-design` is the one that stops your app looking generic.

**`CLAUDE.md`** — A file in your project that the assistant reads at the start of
every session. Your project's standing instructions. Under 200 lines.

**Context** — Everything the assistant can currently see. Limited, which is why
`CLAUDE.md` should be short and why long sessions drift.

**Hallucination** — Confidently stating something untrue. Most likely about
things that change often: APIs, key formats, flags, prices. The defence is
checking, not trusting.
