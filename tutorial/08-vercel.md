# 8. Put it on the internet

Your calendar exists on your laptop. This chapter gives it an address.

---

## Send the code to GitHub

In your project folder:

```bash
gh repo create my-calendar --public --source=. --push
```

Four parts: create a repo called `my-calendar`, make it public, use the folder
you are standing in, and push what is already committed.

> **Public or private?** Either works — GitHub's free plan gives unlimited
> private repos, and Vercel's free plan can deploy from a private repository as
> long as it belongs to **you personally** rather than to an organisation.
> Public is friendlier if you want to show someone. There are no secrets in this
> project yet, and chapter 10 makes sure it stays that way.

Check it:

```bash
gh repo view --web
```

Your browser opens on your code, on the internet. Not the website yet — the
*source*.

---

## Make a Vercel account

Go to **[vercel.com/signup](https://vercel.com/signup)** and choose **Continue
with GitHub**.

Signing up with GitHub rather than an email matters: it is what lets Vercel see
your repositories in the next step.

Choose the **Hobby** plan. It is free and needs no card. Chapter 2 covered the
catch — it is for non-commercial use only — and nothing here goes near that
line.

---

## Import the project

Click **Add New… → Project**, or go straight to
**[vercel.com/new](https://vercel.com/new)**.

You will see your GitHub repositories. Find `my-calendar` and click **Import**.

> **If `my-calendar` is not in the list**, it is almost certainly the trap from
> chapter 5: the repository belongs to a GitHub *organisation* rather than to
> you. Vercel's free plan cannot connect to those, and it does not explain
> itself — the repo is simply absent. Appendix A has the fix.

On the configure screen: **change nothing**. Vercel detects Next.js and sets
everything correctly. Click **Deploy**.

### Do not add a config file

You may be tempted, or told, to add a `vercel.json` or a `vercel.ts`. **Do not.**
For a plain Next.js app the correct number of configuration files is zero. An
unnecessary config file is one of the more common ways people break a build that
was working fine.

---

## Watch it build

You get a log, a minute or two of scrolling, and then confetti and a URL like:

```
https://my-calendar-abc123xyz-yourname.vercel.app
```

**Click it.** That is your calendar, on the internet, reachable from your phone.

### The exception nobody mentions

You may have read that pushing to `main` publishes and everything else makes a
private preview. That is true — **from the second deployment onwards.**

> The first deployment of a new project is **always a production deployment**.

It happens whether you import in the dashboard, run the CLI without `--prod`, or
deploy from a branch that is not `main`. So the site you are looking at is
already live and public. Worth knowing before you assume your first attempt was
private.

---

## Now the good part

Change something small — ask Claude Code:

```
Change the footnote text at the bottom of the page slightly, then
commit and push.
```

Then watch your Vercel dashboard. Within a minute or so, without you doing
anything:

```
Building → Deploying → Ready
```

Refresh your live URL. The change is there.

**That is the loop.** From here on, publishing is a side effect of committing.
There is no upload step, no FTP, no "deploy" button. `git push` is the deploy
button.

---

## Check, do not assume

A push that produced no error is not the same as a deployment that worked. Builds
fail for reasons that never appear on your machine — a file that only exists
locally, a package installed but never saved to `package.json`.

**Look at the dashboard, or open the URL.** "It pushed" is not "it deployed".

If a build fails, the log says why, and the answer is usually in the last twenty
lines. Copy them to Claude Code:

```
My Vercel build failed. Here is the end of the log. What is wrong and how
do I fix it? <paste>
```

---

## Two things that will confuse you later

**Your preview links will ask strangers to log in.** From chapter 9 you will get
a preview URL for each branch. Vercel protects those by default — your
production site is public, but preview links show a Vercel login page to anyone
who is not you. Nothing is broken. If you want to share one, turn it off at
**Project → Settings → Deployment Protection**.

**A second push while a build is running looks like a hang.** The free plan runs
**one deployment at a time**; the second waits. It is queued, not stuck.

---

## What you have

- Code on GitHub, with history
- A live website, on a real URL
- Automatic publishing on every push
- Total cost: nothing

And a loop you will now use for everything: **change → commit → push → live**.

Chapter 9 adds the missing safety catch — how to try a change *before* it
reaches the site your friends are looking at.

---

**Next:** [9. Add the holidays →](09-holidays.md)
