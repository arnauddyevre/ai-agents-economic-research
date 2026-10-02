# Quick start (macOS, with a Windows note)

Use **one** coding agent: Claude Code or Codex. Having both is optional. The workshop folder works
from an extracted ZIP; a Git repository is not required to do the exercises.

> **On Windows?** The steps are the same, with a few differences. Use PowerShell or Windows
> Terminal where this guide says Terminal. Install each agent with its official Windows instructions:
> [Claude Code](https://code.claude.com/docs/en/setup) (Windows 10 or later; Git for Windows is
> recommended) and [Codex](https://learn.chatgpt.com/docs/windows). Run the Python scripts with `py`
> instead of `python3`. For LaTeX, use [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)
> rather than MacTeX. Phone pairing works too: Codex needs the ChatGPT desktop app for Windows. When a
> guide shows a macOS command, ask your agent for the Windows equivalent before running it.

## Before class

1. Extract the whole pack to a writable folder on your Mac. Open the **pack root**, containing
   `README.md`, `AGENTS.md` and `CLAUDE.md`, in your agent or IDE. Do not open only an exercise folder.
2. Open [presentation/index.html](presentation/index.html) in your browser. Images and diagrams are
   embedded; reference links require internet. The Beamer skill’s maths template also uses an online CDN.
3. Sign in to your chosen agent and check that you have usage available. For exercise 4, use your
   subscription account rather than separately billed API credentials.
4. For the phone exercise, have the matching mobile app ready and keep your Mac awake and online.
5. Bring a Beamer deck folder and PDF if you have one. A small supplied deck and worked conversion
   are available if you do not. Connecting Gmail/Slack/Zoom is optional if your account prevents it;
   the fictional message export lets you practise retrieval and checking.

## Command-line client for exercise 4

In Terminal, check `codex --version` or `claude --version`. An IDE extension can work even if the
standalone CLI is missing from PATH. Ask your agent to locate it before installing anything.

If the CLI is missing, follow its official macOS installer guide:

- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli): install the command, then run `codex` and
  choose **Sign in with ChatGPT**. `codex login status` checks the sign-in method.
- [Claude Code quickstart](https://code.claude.com/docs/en/quickstart): install the command, then run
  `claude` and sign in with your Claude subscription. `/login` changes sign-in inside the session;
  `claude auth status` checks it from Terminal.

Use the official guide’s current installation command; these links were checked on 2 October 2026.
Never copy an authentication file or token into the workshop folder. If a command is not found after
installation, open a new Terminal window and follow the guide’s PATH troubleshooting.

The optional runners require **Python 3.9 or later** (`python3 --version`), with no third-party Python
packages. If absent, use the [official macOS Python installer](https://www.python.org/downloads/macos/).
Live calls require internet and available usage. The worked classification and reviewer require neither.

## Skills and extra tools

Start by reading [skills/README.md](skills/README.md). Copy the **whole selected skill folder** to
`.claude/skills/` or `.agents/skills/`, preserving existing versions. Invoke `/skill-name` in Claude
Code or `$skill-name` in Codex. Exercise 3 uses `beamer-to-html`; the other seven skills are reusable
examples you can explore after class. Downloading the pack does not install them.

LaTeX/`latexmk` is needed only for compiling a deck or paper; Poppler is useful for PDF text/figure
conversion. The sample Beamer PDF is already compiled. Git is needed only for Git-dependent skills;
those skills should report if the extracted folder is not a repository. Skills that ingest papers
need a readable full paper, which is an optional activity rather than a supplied course input.

## First prompt

> Read README.md and PROJECT_HISTORY.md, then get familiar with this workshop folder. Summarise
> the five in-class exercises and the inputs already supplied. Tell me which prerequisites are
> available for my chosen agent and what I need to set up. Do not install software, connect
> accounts or change files yet.

Save exercise work under `outputs/<exercise>/`. See the [exercise index](exercises/README.md) for
exact paths, inputs, prompts, completion checks and fallbacks. If you hit a limit, record it and
use the relevant fallback rather than describing a live call or connection that did not happen.
