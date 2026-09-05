# 1. What you're making

You are going to build a calendar and put it on the internet.

Not a toy that runs only on your laptop. A real address, on a real web host,
backed by a real database, that you can open on your phone or send to a friend.

![The finished calendar](../screenshots/app/06-appointments-in-grid.png)

It marks public holidays in red. It knows the holidays of 206 countries, and
you pick which one from a menu. You can click any day and write something on
it, and what you write is saved in a database rather than in the browser, so it
is still there tomorrow.

---

## What "vibecoding" means, and what it doesn't

Vibecoding is describing what you want in ordinary English and letting an AI
assistant write the code. It works. People with no programming background ship
real, useful things this way every week, and this course will get you there.

Here is the part that usually goes unsaid.

The app is easy. The *second week* is hard. You ask for one more feature, the
assistant obliges, and something that used to work stops working. You cannot
tell what changed, because you did not write any of it. There is no way back to
the version that worked. So you ask the assistant to fix it, and it changes five
more things, and now you have a mess you understand even less than before.

That is not a failure of the AI. It is a failure of *process*, and it has been
solved for decades — professional programmers have exactly the same problem and
have built tools for it. This course teaches you those tools alongside the app.
There are only about six of them and none is difficult.

So: **maintainable** vibecoding. You will finish with a working calendar, and
also with the ability to change it next month without fear.

---

## The shape of it

You will build the app three times over, each time adding one layer. This is
deliberate. Each layer forces you to learn one new idea at exactly the moment it
becomes useful, instead of learning nine ideas up front and forgetting eight.

**First — a calendar.** A month of days, ruled like a page in a diary, that you
can page backwards and forwards through. By the end of it the app is on the
internet at its own address, and updates itself whenever you change the code.
*What you learn: the loop. Change something, save it, watch it go live.*

**Second — the holidays.** The days that matter go red, and a settings menu lets
you choose whose holidays to show — Hong Kong, Germany, California, whatever.
*What you learn: how to try a change safely before it reaches the live site,
and why some code must run on the server rather than in the browser.*

**Third — appointments.** Click a day, write on it, and it is saved forever in a
database. *What you learn: what a database is, what a secret is, and the rule
that decides who is allowed to read what.*

---

## What it costs

**Nothing.** Every service in this course has a free tier that a project this
size will not come close to exhausting, and none of them asks for a card.

Two honest caveats, both of which have their own section in the next chapter:

- The free web hosting is **for non-commercial use only**, and the definition is
  broad enough that an advert or a donate button breaks it.
- The free database **pauses itself after a week of no activity**. Your data is
  safe, but you come back to an app that looks broken until you click Resume.

Neither will bite you during the course. Both will bite you eventually, so they
are written down rather than glossed over. Appendix C has the full numbers.

---

## What you need

- **A Mac.** The commands here are for macOS. Most of it works identically on
  Linux; Windows differs enough that you would be fighting the instructions.
- **An email address**, for three free accounts.
- **About a weekend**, though not all at once.

You do not need to know any programming. You do not need to have opened Terminal
before. You do not need to know what any of the words in the last section meant.

---

## Roughly how long

| Chapters | What happens | Time |
|---|---|---|
| 2 | Reading, no typing | 15 min |
| 3–4 | Terminal, and installing your tools | 45 min |
| 5–6 | GitHub account, meeting Claude Code | 40 min |
| 7–8 | Build the calendar, put it on the internet | 1–2 hrs |
| 9 | Holidays and the settings menu | 1 hr |
| 10 | The database | 1–2 hrs |
| 11 | Reading, no typing | 20 min |

Chapters 3 and 4 are the least fun part of the whole course — installing things
always is. They are also the only chapters where nothing visible happens. Push
through them in one sitting if you can; everything after is immediately
rewarding.

---

## One habit, starting now

When something in this course confuses you, **ask the assistant to explain it
before moving on**. Type the confusion in plain words:

> I don't understand what a "branch" is. Explain it to me like I've never
> used git, using this project as the example.

You are not being slow. You are doing the thing that separates people who can
still change their app in six months from people who cannot.

---

**Next:** [2. The stack, and why these three →](02-the-stack-and-why.md)
