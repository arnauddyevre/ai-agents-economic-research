# 2 — Continue a session from your phone

Start on your Mac, send a follow-up from your phone, and check that it reaches the laptop and the
same project. Keep your Mac awake, online and signed in. You need the matching mobile app and
account; university accounts may require administrator approval.

## Claude Code

Sign in with your Claude subscription using `/login`. API-key authentication does not support
Remote Control. In your local session, type `/remote-control` (or `/rc`). On your phone, open the
Claude app, tap **Code** and pick that session. The CLI can also show a session QR code; `/mobile`
shows a download QR code if you need the app. Keep the local session running.

See [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control) for supported
plans, client versions and troubleshooting.

## Codex

Start setup in the **ChatGPT desktop app on your Mac**. Go to **Settings → Connections → Control
this Mac → Set up** (some versions show **Control this Mac or PC**, or **Add**). Approve remote
access, scan the QR code and finish pairing in ChatGPT on your phone with the same account and
workspace. Open the phone’s **Codex** tab (**Remote** in older versions).

If you use the VS Code extension, you still need the desktop app for this setup; it cannot start
from the IDE extension or CLI. See [Codex remote connections](https://learn.chatgpt.com/docs/remote-connections).
These procedures were checked on 2 October 2026; features can depend on rollout and account policy.

## Try it

On the laptop, open this workshop folder and ask the agent to read its README and history. On the
phone, send:

> Summarise where we are in this project and suggest the next small step. Do not change any files yet.

Check on the laptop that the message appears in the intended session and that the answer describes
this project accurately. Save a short result in `outputs/02-phone-continuation/check.md`: client,
whether pairing succeeded, whether the laptop received the message and any limitation.

If Remote Control is unavailable, continue on the laptop and record that pairing was skipped. No
additional dataset is needed and there is no simulated “successful pairing” fallback.
