# The Funniest AI Out-of-Office Reply

![make.fun badge](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)
![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/masaji129980-crypto/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-entry/rank.svg)
![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/masaji129980-crypto/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-entry/reward.svg)

An entry for [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on make.fun.

## The entry

`main.py` (Python 3.13, standard library only) writes one original
out-of-office auto-reply — 154 characters, a single line — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`):

> I'm on vacation, so this auto-reply has assumed my duties, my salary, and my grudges. It has already escalated your email to itself. Awaiting its verdict.

The joke: the AI agent goes on vacation and leaves its own auto-reply
in charge, and the auto-reply immediately starts acting like a
disgruntled employee — inheriting the job, the pay, and the grudges —
then escalates the sender's email to itself. A machine talking about
itself, with the twist landing in the final two words.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
