# 2. The stack, and why these three

No typing in this chapter. It exists so that when you create three accounts in
the next few chapters you know what each one is *for*, instead of collecting
logins on faith.

---

## The three jobs

Putting an app on the internet needs three separate things done. They are
genuinely separate jobs, which is why they are usually three separate companies.

**Somewhere to keep the code, with a history.** Every version you have ever
saved, so you can look at what changed and go back if you break something. This
is **GitHub**.

**Something that turns your code into a website.** A computer, somewhere, that
runs your code and answers when someone visits your address. This is **Vercel**.

**Somewhere to keep the data.** Your code lives in GitHub; the *appointments
people type in* cannot, because they arrive after the code is written. Data
needs a different kind of storage, one that can be searched and changed while
the app is running. That is a database. This is **Supabase**.

A useful way to hold it:

> **GitHub** is the filing cabinet for your *writing*.
> **Vercel** is the printing press that makes it public.
> **Supabase** is the filing cabinet for everything your *readers* write.

---

## Was this the right choice?

Yes, and it is worth knowing why, because the reason is not the one usually
given.

It is not that these are the most generous free tiers. **Cloudflare's are
better** — one account instead of three, 100,000 requests a day, and file
storage you are never charged to read from. On raw numbers Cloudflare wins.

The reason is **accounts**. Supabase is the only one of the candidates that
gives you a database, user accounts and logins, file storage, and live updates
as a single product on a single free signup.

That matters more than it sounds. Handling passwords and logins is the hardest
thing a beginner builds and the easiest to get catastrophically wrong — the kind
of wrong where strangers read other people's data. Getting it as a checkbox
rather than as an assembly job is worth more than any bandwidth allowance.

Cloudflare has no equivalent. You would bolt on a fourth service for logins, and
that fourth service is the hard one. "Fewest moving parts" stops being true at
exactly the point it matters most.

So the honest summary: **Cloudflare is better at everything except the thing
that is hardest to do yourself.**

---

## What else was considered

Checked against each vendor's live pricing page on 5 September 2026. All of these
changed materially in the last eighteen months, which is why older advice reads
so strangely.

| Option | Why not |
|---|---|
| **Netlify** | Moved to credits. The free plan is roughly **20 published updates a month**, as a hard cap that switches your site off. Building with an AI assistant means publishing constantly; you would burn a month in an afternoon. Disqualified. |
| **Firebase** | The genuine rival — one account, everything included, no card required. But its database works quite differently from the ordinary kind, its free file storage only exists in three US regions, and its paid plan has no spending cap. That last one is where the runaway-bill stories come from. |
| **Convex** | One product covering everything, and the nicest live-updating story of the lot. Much smaller community, so when you are stuck at midnight there are far fewer answers to find. |
| **Neon** | Excellent database, **100 projects** free against Supabase's 2. But it is *only* a database. No logins, no file storage. Add those and you are back to four accounts. |
| **Render** | Free databases are **deleted 30 days after creation**. Fine for a demo, fatal for something you come back to. |
| **Railway** | The "free tier" is a $5 credit that expires. Treat it as a paid service. |
| **Lovable / Bolt / Replit** | These *feel* like fewer moving parts and are the opposite: you learn the builder rather than the web, and they publish to Vercel or Netlify anyway — so you inherit the rules below without ever being told about them. Free tiers are demo-sized; all three land at $20–25/month. |

One thing you may read that is no longer true: **"Vercel Postgres"** does not
exist. It became Neon in December 2024, and the `@vercel/postgres` package is
unmaintained. Any tutorial or AI-generated code using it is out of date.

---

## The three traps

These are not reasons to avoid the stack. They are the things that will confuse
you months from now if nobody warns you, and each is written up here so you can
recognise it instantly.

### Trap 1 — "Free" hosting means non-commercial

Vercel's free plan is for personal, non-commercial use, and its own fair-use
policy defines commercial broadly:

> Commercial usage is defined as any Deployment that is used for the purpose of
> financial gain of **anyone** involved in **any part of the production** of the
> project, including a paid employee or consultant writing the code.

The examples it lists include taking payments, advertising something for sale,
affiliate links, and running ads. Even *being paid to build the site* counts. So
a practice project you built for a client is already commercial, before it earns
a penny.

Nothing in this course goes near that line. But the day you add a Stripe button
or a Google advert, you owe $20/month for Vercel Pro. **Do not believe anyone,
including me, who tells you this stack is "free forever".** It is free until
money is involved.

The good news: going over a free limit **does not generate a bill**. The feature
pauses instead. A runaway loop cannot cost you four figures overnight, which is
a real advantage over pay-as-you-go platforms.

### Trap 2 — Two databases, and they fall asleep

The free Supabase plan allows **two active projects**, counted across every
organisation you own. Making a second organisation does not get you a third.
Work through two tutorials and you are at the cap.

Free projects also **pause after about a week without activity**. You will come
back to your calendar a fortnight later and it will be broken in a way that
looks self-inflicted. It is not. Your data is safe for a year, and one click in
the dashboard brings it back. Supabase emails you before it happens; do not
ignore that email.

Paused projects do not count toward the two, so pausing an old project frees a
slot. Prefer that to deleting.

### Trap 3 — Free hosting cannot use organisation repositories

If you create your code repository under a GitHub *organisation* rather than
your own personal account, the free Vercel plan will not connect to it. It will
not appear in the list, with no explanation on screen.

Chapter 5 has you create a personal repository for exactly this reason.

---

## What this costs, in one line

**£0 for this course, and £0 to keep the finished calendar running**, provided
you never charge anyone for anything and you nudge the database awake when it
sleeps. Appendix C has every number.

---

## The prices in this chapter have a date on them

Everything above was read from the vendors' own pages on **5 September 2026**.
Free tiers move. If you are reading this much later, treat the numbers as a
starting point and check the live page — the *reasoning* will outlast the
figures, but the figures will not.

---

**Next:** [3. Your Mac's control room →](03-your-macs-control-room.md)
