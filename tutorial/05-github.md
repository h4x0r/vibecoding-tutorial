# 5. GitHub

## Git and GitHub are not the same thing

This trips up everyone, so let us settle it before the account.

**Git** is the program you installed last chapter. It runs on your Mac and
keeps every version of your work. It needs no internet and no account. Git is
yours.

**GitHub** is a website that keeps a copy of your Git history in the cloud. It
is a backup, a way to share, and — the part that matters here — **the thing
Vercel watches**. When you send new code to GitHub, Vercel notices and
republishes your website.

You can use Git with no GitHub at all. You cannot get automatic publishing
without it.

---

## What a repository is

A **repository** — everyone says "repo" — is one project's folder plus its
entire history.

Not the current state of the folder. *Every* state it has ever been in, and who
changed what, when, and why. A repo is less like a folder and more like a folder
with a time machine bolted to it.

You will make one repo, called `my-calendar`, holding your calendar.

Two more words you will meet constantly:

**Commit.** A save point. You make one when something works, with a short note
saying what changed. Every commit can be returned to, forever. This is the
single habit that separates "I broke it and I'm stuck" from "I broke it, let me
go back ten minutes".

**Push.** Sending your commits up to GitHub. Committing is local and private;
pushing publishes.

---

## Make the account

Go to **[github.com/signup](https://github.com/signup)**.

You need an email address, a password, and a username. Three notes:

- **The username is public and appears in every URL** — your calendar will live
  at `github.com/yourname/my-calendar`. Pick something you would put on a CV.
  Changing it later breaks every link anyone has saved.
- Use a **real email address you can open right now**; you will need to click a
  link in it.
- Turn on **two-factor authentication** when offered. GitHub will insist
  eventually anyway, and doing it now is five minutes rather than a locked
  account later.

The free plan is genuinely free, with unlimited private repositories. There is
no card and no trial.

### One decision that matters later

When GitHub offers to create an **organisation**, decline. Make your repository
under your **own personal account**.

This is not tidiness. Vercel's free plan **cannot connect to repositories owned
by a GitHub organisation** — the repo will simply not appear in the list, with
nothing on screen explaining why. It is the single most common wall people hit
in chapter 8, and choosing right now avoids it entirely.

---

## Connect your Mac to GitHub

Your Mac needs to prove it is you before it can push. The pleasant way is
GitHub's own command-line tool.

**Install it.** Go to **[cli.github.com](https://cli.github.com)** and download
the macOS installer, or take it straight from the
[releases page](https://github.com/cli/cli/releases/latest) — the file you want
is the one ending **`_macOS_universal.pkg`** (at the time of writing,
`gh_2.100.0_macOS_universal.pkg`). Open it and click through, exactly like Node.

Quit and reopen Terminal, then:

```bash
gh --version
```

**Log in.**

```bash
gh auth login
```

It asks a short series of questions. The answers:

| Question | Answer |
|---|---|
| What account do you want to log into? | **GitHub.com** |
| What is your preferred protocol? | **HTTPS** |
| Authenticate Git with your GitHub credentials? | **Yes** |
| How would you like to authenticate? | **Login with a web browser** |

It shows an eight-character code, then opens your browser. Paste the code,
approve, and come back to Terminal.

**Check it worked:**

```bash
gh auth status
```

```
github.com
  ✓ Logged in to github.com account yourname (keyring)
  - Active account: true
  - Git operations protocol: https
```

That `✓` means your Mac can now push code to GitHub without asking you for
anything again.

> **Why not SSH keys?** Because they are a whole chapter of their own —
> generating a key, adding it to an agent, uploading the public half, learning
> what a fingerprint is. HTTPS through `gh` gets you to the same place today.
> Learn SSH when you have a reason to.

---

## Tell Git who you are

Git stamps every commit with a name and email. Set them once:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

Use the same email as your GitHub account, so GitHub links your commits to your
profile. If you would rather not publish your address, GitHub can give you a
private forwarding one — it is under **Settings → Emails → Keep my email
address private**, and looks like `12345+yourname@users.noreply.github.com`.

Skip this and your first commit fails with a message telling you to do exactly
this. Doing it now saves the interruption.

---

## You do not have to do the git parts by hand

From chapter 7 onwards, Claude Code will run most of these commands for you. You
will type "commit this" far more often than you type `git commit`.

That is fine — but it is why this chapter exists. **Knowing what a commit is
means you can ask for one at the right moment**, and can tell when the assistant
has done something you did not want. Delegating is only safe when you can read
the result.

---

## Where you are

- A GitHub account, under your own name, with two-factor on
- `gh auth status` showing a tick
- Git knowing your name and email

No repository yet. That arrives in chapter 7, when there is something to put in
it.

---

**Next:** [6. Talking to Claude Code →](06-talking-to-claude.md)
