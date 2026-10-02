# Your outputs

Save activity outputs under `outputs/<exercise>/`, using the folder name given in the exercise guide.
Both agents can read these files when they are working in this project. Git ignores everything
here except this README, including nested folders and archives.

Completed document tasks use `outputs/archive/<task>/`. Preserve the originals, resulting notes and
an archive note that records the source filenames and verified SHA-256 checksums. Follow the
[document inbox workflow](../document_dump/README.md) before removing inbox copies.

These folders are created as needed. Do not create a second set of agent instructions or a second
project history merely to change agents; the shared context files at the pack root remain the
handoff. Each exercise can have its own working notes.

Local does not mean backed up. Keep a backup of work you want to retain. If you later decide to
version some outputs in your own project, review those files and change the tracking policy
deliberately. The distributed `close-session` skill leaves ignored files untracked.
