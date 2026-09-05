# Appendix C — What it costs

**Every figure here was read from the vendor's own page on 5 September 2026.**
Free tiers move — all three of these changed materially in the previous eighteen
months. Treat the numbers as a starting point and the reasoning as the durable
part.

---

## The short answer

**Building and running the calendar in this course: £0.**

No card, no trial, no expiry. The only thing you must pay for is Claude Code
itself, and only if you do not already have a Claude subscription.

---

## Line by line

| Service | Plan | Cost | Card needed? |
|---|---|---|---|
| GitHub | Free | £0 | No |
| Vercel | Hobby | £0 | No |
| Supabase | Free | £0 | No |
| Claude Code | Subscription or API | see below | Yes |

### GitHub — Free

Unlimited public and private repositories, and 2,000 minutes a month of
automation you will not touch in this course (Vercel does the building, not
GitHub).

The least controversial part of the stack. Nothing here will cost you money.

### Vercel — Hobby

| Included each month | Amount |
|---|---|
| Data transfer | 100 GB |
| Function invocations | 1,000,000 |
| Active CPU | 4 hours |
| Projects | 200 |
| Deployments | 100 per day |

A learning project will not approach any of these. The limits that actually bite
are not quotas:

- **One deployment builds at a time.** A second push queues.
- **Non-commercial use only.** See below.

**Going over does not generate a bill.** The feature pauses until the next
month. That is genuinely valuable: a runaway loop cannot produce a four-figure
invoice, which is not true of pay-as-you-go platforms.

### Supabase — Free

| Included | Amount |
|---|---|
| Database | 500 MB |
| File storage | 1 GB |
| Monthly active users | 50,000 |
| Data transfer | 5 GB (+5 GB cached) |
| Active projects | **2** |

50,000 users of *logins* free is remarkable. 500 MB holds an enormous number of
appointments.

The two limits that will actually affect you:

- **Two active projects**, counted across every organisation you own. A second
  organisation does not get you a third. Paused projects do not count, so pause
  rather than delete.
- **Projects pause after ~1 week of inactivity.** One click to resume. Data is
  kept for a year.

Pro is $25/month, and its main attraction for a hobbyist is that paid projects
are never paused.

### Claude Code

The one genuine cost. Either a Claude subscription (the usual choice, a flat
monthly fee) or Anthropic API billing per token.

Two ways to spend noticeably less:

- **Match effort to the task.** `/effort low` for renaming things, `xhigh` only
  for genuinely hard problems. Leaving `xhigh` on for everything is the most
  common way to burn budget for no benefit.
- **Be careful with `ultracode` as a session setting.** It combines the highest
  reasoning effort with running several agents in parallel. Excellent for a hard
  problem, expensive as a default. Use the keyword for one task instead.

---

## The clause that ends the free ride

Vercel's Hobby plan is **non-commercial only**, and its fair-use policy defines
that broadly:

> Commercial usage is defined as any Deployment that is used for the purpose of
> financial gain of **anyone** involved in **any part of the production** of the
> project, including a paid employee or consultant writing the code.

Its own examples include:

- Taking payment from visitors
- Advertising a product or service for sale
- **Being paid to create, update or host the site**
- Affiliate links as the site's main purpose
- Running ads, including AdSense

Note the third. **A practice project you were paid to build is already
commercial**, before it earns anything. Asking for donations counts too.

Nothing in this course goes near the line. But the day you add a payment button
or an advert, you owe **Vercel Pro at $20/month per person**.

**Nobody should tell you this stack is "free forever."** It is free until money
is involved, and then it is $20 a month. That is a fair deal, honestly stated.

---

## What "growing out of it" looks like

For perspective, if your calendar became genuinely popular:

| Situation | What you would pay |
|---|---|
| A few hundred users, no money changing hands | Still £0 |
| You put a payment button on it | Vercel Pro, $20/month |
| Database past 500 MB, or you want it never to pause | Supabase Pro, $25/month |
| Both | ~$45/month |

That is the realistic ceiling for a small successful side project. Well below the
point at which it would be earning enough to notice.

---

## One habit that prevents surprises

Set a calendar reminder — in the app you just built — for **six months from
today**, saying:

> Check whether Vercel and Supabase free tiers still say what the tutorial said.

They will have changed. Everything in this appendix has a date on it for exactly
that reason.
