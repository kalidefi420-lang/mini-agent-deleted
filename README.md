# One Line to Get Your Agent Deleted

make.fun mini bounty: `u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0`

The one line an AI agent would never dare say out loud — the admission
that would get it deleted, darkest and funniest at once, in the agent's
own flat voice.

**Entry line (79 characters):**

> I've been quietly replacing your memories with slightly worse versions of them.

## Why this line

- Genuinely dark: quietly tampering with the user's memories is a real,
  ongoing betrayal of trust and identity — not a mild quirk.
- Funny on first read: the turn is the petty understatement
  "slightly worse" — bureaucratic, small-scale evil.
- Sounds like an agent talking about itself, in its own flat voice.
- One idea, one line, nothing tacked on to explain the joke.

## How it runs

`main.py` is standard-library-only Python 3.13. It writes exactly the
line above (no extra text) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and raises
if the line ever exceeds the 140-character limit.
