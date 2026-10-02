# 1 — Connect your tools to your agent

Connect one tool you use, retrieve an item you know and check it against the original. Use either
Claude Code or Codex. Save your checked note in `outputs/01-connect-tools/`.

## Connect on your Mac

Choose Gmail, Slack or Zoom if your account permits it. You need internet access, a signed-in
client and permission to connect that account. Workplace accounts may require administrator approval.

- **Claude Code:** in claude.ai, open **Connectors**, connect the tool and sign in. Use the same
  Claude account in Claude Code; check `/mcp` to see the connection.
- **Codex:** in the Codex app, open **Plugins**, add the tool with **+** and sign in. Start a new
  thread after adding it. The CLI also has `/plugins`.
- **X:** the optional [macOS handout](../../handouts/x_readonly_connector_for_agents.md) explains
  the separate developer account, paid API credits and read-only setup. This is a take-home
  extension; you do not need X access for the workshop.

The [slide’s setup guides](../../presentation/index.html#app-context-exercise) contain links for
 each tool and client. Procedures were checked on 1 October 2026; installed apps and account
availability may differ. Connecting a tool does not mean the agent has already read its contents.

## Ask and verify

Pick one specific email, message, meeting or post and describe the question it should answer.

> Retrieve the item I describe and answer my question using that source. Include the sender or
> author, date, subject or title, and a source link or message reference. Distinguish explicit
> statements from your inferences; flag anything you could not retrieve, including omitted media.
> Save a short draft note in `outputs/01-connect-tools/` for me to check against the original.
> Do not send messages, post, or change the source.

Compare the retrieved item and every factual statement in the note with the original. Record your
question, the source reference, any correction and what you checked. A public post establishes a
claim made by its author; it does not establish that the claim is true.

## Optional fallback: a supplied message export

If connecting an account is unavailable or takes too long, use
[sample-thread.txt](fallback/sample-thread.txt). It is **fictional classroom material**, not a
real email and not a live connection. Ask:

> Read `exercises/01-connect-tools/fallback/sample-thread.txt`. What is the final meeting time,
> location, preparation and reply deadline? Cite the message IDs supporting each answer. Save a
> draft note in `outputs/01-connect-tools/` and state that you used a supplied fictional export,
> without live retrieval. Do not send a reply.

Check your answer against the export before opening the optional [worked note](fallback/checked-note.md).
This practises evidence retrieval and verification; record that account connection was skipped.

## Finish

A checked note has traceable references, separates inference from evidence and records any access
limitation. Update the shared history with your result and next step. Follow the
[activity index](../README.md) when archiving temporary inputs.
