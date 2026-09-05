# Appendix A — When it breaks

Every error in this list was actually produced while building this course. Skim
it once now; you will recognise them faster later.

**The general method, before any specific fix:** copy the *whole* error, not
your summary of it, and paste it to Claude Code with what you were doing. The
exact text is the diagnosis. Retyping it from memory loses the part that
mattered.

---

## Installing things

### `zsh: command not found: claude`

That program is not installed, or the terminal has not noticed it yet.

Two fixes, in order. **Quit Terminal entirely (⌘Q) and reopen it** — a newly
installed program is only visible to windows opened afterwards, and this alone
solves it surprisingly often. If it persists, the install did not finish; run it
again and read the last few lines.

Also check the spelling in the message itself. It tells you the name it looked
for, which is how you catch a typo.

### `npm warn deprecated eslint@…` and `npm warn install-scripts`

**Not errors.** The first is a note about a package your project uses
indirectly. The second is npm declining to run an install-time script unless
allowed, which is a safety default.

If the command ended with `Success!` or the prompt came back cleanly, it worked.

### `npm error code ERESOLVE`

Two packages disagree about what they need. The message names both:

```
Found: @types/node@20.19.43
Could not resolve dependency:
peerOptional @types/node@"^22.0.0 || >=24.0.0" from vitest@5.0.0
```

**Read it before reaching for a flag.** Here the project asked for version 20
while the new package wanted 22 or newer — so the fix was to bring the old one
up to date:

```bash
npm install -D "@types/node@^24"
```

You will be tempted by `--force` or `--legacy-peer-deps`, which npm helpfully
suggests. Those *silence* the conflict rather than resolve it, and the breakage
turns up later somewhere unrelated. Use them only when you know why.

---

## Building and testing

### `Warning: Next.js ignored pnpm-lock.yaml in /Users/you because it is outside the current Git repository`

Next looks upward for a lockfile to work out where your project starts, and
found an unrelated one in a parent folder. Harmless, but noisy. Settle it in
`next.config.ts`:

```ts
turbopack: { root: __dirname }
```

### The tests pass but `npm run build` fails with a type error in a test file

`next build` type-checks everything, including tests, while the test runner only
runs them. A real example:

```
lib/locale.test.ts(27,25): error TS2345: Argument of type
'(raw: string | undefined) => void' is not assignable...
```

The build is right and the tests were hiding it. **Always run the build, not just
the tests, before pushing.**

### `Failed to resolve import "./holidays"` — and why that is not a real red

If you are writing a test before the code exists, this is what you get. It is a
*setup* failure, not a behaviour failure: it proves the file is missing, not that
your assertions work.

Create the module with empty stubs first, then run the tests. Now the failures
are real ones (`expected [] to have a length of 17 but got +0`), and passing them
means something.

### `Cannot find module '@radix-ui/react-popover'` (or any `@radix-ui/react-*`)

This one is worth knowing about in advance, because it is the most likely way a
confident assistant breaks your build.

shadcn/ui changed the library underneath it. A default install today is built on
**Base UI**, and the generated components import from `@base-ui/react/…`. Almost
every shadcn example written before that change — and therefore a good deal of
training data — imports `@radix-ui/react-something`, which is not installed and
will not compile.

Do not install the missing package to make the error go away; you would end up
with two component libraries. Say instead:

```
This project's shadcn install is built on Base UI, not Radix. Rewrite these
imports to match the components already in components/ui/.
```

Adding that fact to `CLAUDE.md` stops it recurring. It is exactly the kind of
line the "things that have already bitten us" section is for.

### `error: unknown option '--turbopack'`

`create-next-app` used to take that flag. Turbopack is now the default for both
development and building, so the flag was removed — there is nothing to turn on.
If you copied the command from an older guide, delete the flag.

Related, and easy to miss: **passing any `--flag` to `create-next-app` switches
off the questions entirely** and silently applies the default answer to
everything you did not specify. If you want to choose, pass no flags at all.

### `TypeError: loadEnv is not a function`

`loadEnv` comes from `vite`, not from `vitest/config`:

```ts
import { loadEnv } from "vite";
import { defineConfig } from "vitest/config";
```

---

## GitHub and Vercel

### My repository is not in Vercel's import list

Almost always: **the repository belongs to a GitHub organisation.** Vercel's free
plan cannot connect to organisation-owned repositories, and it does not say so —
the repo is simply absent.

Fix: create it under your personal account. To move an existing one, GitHub
**Settings → Transfer ownership**.

### The preview link shows a Vercel login page

Working as designed. Deployment protection is on by default for new projects:
your production site is public, preview links are not.

**Project → Settings → Deployment Protection** to turn it off.

### I set an environment variable and the site still says `undefined`

Environment variables are read **when the site is built**. Changing one does not
touch a site that is already built.

**Redeploy.** Vercel dashboard → Deployments → ⋯ → Redeploy.

### I pushed twice and the second build seems stuck

The free plan runs **one deployment at a time**. The second is queued. Wait.

### The build fails on Vercel but works on my Mac

Nearly always something that exists on your machine and not in git:

- A package installed but never saved — check it is in `package.json`
- A file that is gitignored (`.env.local` will not be there, by design)
- A filename whose capitalisation differs — macOS does not care, Linux does

`git status` shows anything uncommitted. The build log's last twenty lines
usually name the file.

---

## Supabase

### `permission denied for table appointments`

The table exists but nobody may touch it. Separate from Row Level Security:

```sql
grant select, insert, update, delete on public.appointments to authenticated;
```

Current Supabase no longer grants this automatically to tables created by SQL —
which is what an AI assistant writes.

### My list is empty and there is no error

Row Level Security is on and there are no policies, so the table correctly
returns nothing. This is default-deny working.

**Add policies. Do not turn RLS off.** Turning it off makes every row readable by
anyone holding the publishable key, which is in every visitor's browser.

### `Invalid API key`, or everything 401s

Three candidates, in order of likelihood:

1. **Wrong variable name.** The code reads
   `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. If you named it `..._ANON_KEY` it is
   `undefined`.
2. **Wrong key.** A long key starting `eyJ` is the legacy one. Use
   `sb_publishable_…`.
3. **Wrong header**, if you are calling the API by hand. New keys go on `apikey`,
   not `Authorization: Bearer`.

### My app worked last month and is now dead

The free project **paused after about a week of inactivity**. Nothing you did.

Supabase dashboard → your project → **Resume**. Data is kept for a year. Supabase
emails a warning first; that email is worth not ignoring.

### `supabase start` cannot find Docker

Local Supabase needs a container runtime. You do not need it for this course —
develop against the hosted project.

If you do want it, `podman` is lighter than Docker Desktop on a Mac, and the
Supabase CLI finds it once `podman machine start` is running.

---

## Claude Code

### `API Error: 400 … does not support this model`

Your Claude Code is older than the model you asked for.

```bash
claude update
```

This is the failure mode of installing by a route that does not update itself.
The official installer updates in the background; Homebrew and manual installs do
not.

### It did something I did not want

Press **Escape** to interrupt. Then:

```bash
git status
```

```bash
git checkout -- <file>
```

to undo changes to a file you have not committed. This is exactly why chapter 7
insisted on committing whenever something works.

### It keeps forgetting a rule we agreed

That rule is not in `CLAUDE.md`, or `CLAUDE.md` has grown too long to be followed
reliably. Check what actually loaded:

```
/context
```

Look under "Memory files". Keep the file under 200 lines and make each
instruction checkable.

### It confidently told me something wrong

Expected, and specifically likely about anything a vendor changes often — APIs,
key formats, CLI flags, pricing.

```
Check the current documentation before answering. Do not rely on what you
remember.
```

Then verify in the terminal, which outranks both of you:

```bash
npm view <package> version
```

---

## The bug with no error message

The worst category, and the reason chapter 9 exists: code that runs perfectly
and produces a wrong answer.

Two real ones from this project:

- `new Holidays("XX")` returns an empty list for a country that does not exist.
  The calendar renders fine, with no holidays.
- `parse("2026-9", "yyyy-MM")` returns **31 August 2026** — wrong month, last day
  of the previous one — because one zero was missing.

Neither throws. Neither logs. The only defence is asking, in advance:

> What happens if this gets a value it does not expect? Show me.
