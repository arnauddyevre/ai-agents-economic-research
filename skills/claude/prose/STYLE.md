# Prose style: an example to adapt

This is the full working style guide behind the prose skill. Its preferences and calibration
are examples, not universal requirements.
Inspect it, keep what helps your writing, and replace the rest with your own preferences.

This file is bundled with each agent's skill as an independent ordinary file. Neither copy depends
on another computer. If you use both agents, keep your installed copies aligned.

The procedure in [SKILL.md](SKILL.md) distinguishes authorship: human-authored text receives
suggestions only; agent-generated text may be edited. Every "cut", "fix" or "rewrite" instruction
below means a proposed change when reviewing a human's text. The guide governs the requested
passage, not routine chat replies.

---

## 1. The procedure

Prohibitions catch surface tics. They do not produce good prose. Work through these seven steps in
order, and treat the checklist in section 4 as the last pass rather than the method.

1. **State the claim in one sentence, aloud.** If you cannot, the passage has no claim yet. Fix that
   before touching a word of the prose.
2. **Cut every sentence that does not advance the claim.** Most first drafts lose a third here.
3. **Name the actor.** For each surviving sentence, ask who did what. Make them the subject and the
   verb. "We allocate income", not "income is allocated".
4. **Read it aloud.** Where you stumble or run out of breath, rewrite. This single test catches more
   than the rest of the guide combined.
5. **Run the checklist** in section 4. Then read once more for mannered prose alone: metaphor or
   flourish where a literal phrase would do.
6. **Check sentence-length variance** against the calibration in section 6. Three consecutive
   sentences of similar length means breaking one.
7. **Hedge pass.** Delete any hedge whose removal does not change the meaning. Keep the rest.

---

## 2. Register by document type

The prohibitions hold throughout. The register does not.

| Document | Register |
|---|---|
| **Paper body** | Formal but plain. "We" for authorial action. Load-bearing hedges only. Jargon glossed on first use. The academic writing guidance in section 5 applies here. Apply the read-aloud test to prose, not to notation or definitions. |
| **Notes, logs, to-dos** | Telegraphic. First person. Blunt judgements welcome: "Totally fine by me" or "I don't think the limitations are very convincing". Treat these as appropriate for notes. |
| **Email, external** | Preserve the writer's existing voice: short, contractions, concrete numbers, direct questions. Do not academicise it. |
| **Slides** | Fragments over sentences. |

---

## 3. Preserve the non-native voice

Preserve the writer's voice, including clear phrasing that does not sound native. Avoiding generic
fluency matters more than enforcing the prohibitions below.

**Never smooth a sentence into generic fluency merely because it reads as non-native.**

Four categories, with examples:

**Fix silently in agent-generated text; flag in human text.** These are typing slips, not voice: `developped`, `compoenents`, `eranings`,
`distrinction`, `maintening`, `circonvolutions`, `a sinvestment`, `blind sport` for
"blind spot".

**Keep.** Grammatical, unidiomatic, clear, and forceful:

- `It is key to be able to recover these objects.` A native speaker writes "essential". "Key" is
  shorter and lands harder. Keep it.
- `This angle alone is not present in any paper that I have read.`

**Flag, never silently change.** A calque a reader could misread:

- `raise the interest of public economists for the production of income` calques *susciter
  l'intérêt de X pour Y*. English needs "interest X in Y". Propose the fix and let the writer decide.

**Cut.** Filler dressed as emphasis: `really inferior` becomes `inferior`, which is stronger.

---

## 4. The checklist

### Hard rules

No legitimate use in this writing. Cut on sight.

- **Corrective negation as filler rhythm.** "It's not just about X, it's about Y" used for cadence.
- **Summary beats.** The closing sentence that restates the paragraph you just read.
- **Landing sentences.** The short punchy closer. "That's the whole game."
- **Throat-clearing openers.** "It's worth noting", "Importantly", "Notably", "In today's world".
- **Performed enthusiasm.** "This is a fascinating result", "Great question".
- **Filler intensifiers.** genuinely, really, truly, actually, quite, very.
- **Corporate-register verbs.** leverage, underscore, showcase, delve, foster, harness, navigate.
  Judge "reflect" by sense: "the measure reflects depreciation" is fine, "the results reflect the
  importance of X" is not.
- **Stacked noun phrases** of three or more. "stakeholder engagement optimisation framework".
- **Rhetorical crutches.** "at its core", "fundamentally", "the question is not whether but how".
- **Setup/payoff scaffolding.** "Here's the thing:", "But here's what's interesting:".
- **Mannered prose.** Metaphor or flourish where a literal phrase is available. Defined and tested
  in the next subsection.

### Mannered prose

Cut on sight, like the hard rules. It needs a definition rather than a list, because the offending
phrases read as ordinary English until you look for the literal alternative. The definition below
applies to any agent's drafting.

> Mannered prose substitutes metaphor and flourish for direct statement. Instead of "a parameter
> worth varying," the mannered writer produces "a dial worth turning." Instead of "this point still
> matters," they write "this point earns its keep." The phrases exist to display the writer, not to
> convey the idea, and readers can tell. That is why mannered prose irritates: it makes the reader
> work harder so the writer can perform. It is also imprecise. Metaphors drag in connotations the
> writer did not choose and cannot control. The fix is to say what you mean. When a literal phrase is
> available, use it.

Remove all mannered prose. **Test:** write the literal phrase next to each figure. If it says the
same thing, keep the literal phrase and delete the figure. Figures that read as plain because they
are common, and still fail the test: "does the heavy lifting", "carries the weight", "the engine
of", "moves the needle", "a lens on", "unpack" for explain, "landscape" for field. Where the literal
phrase is a number or a worked case, section 5 already asks for it.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#writing-density

### Caps, not bans

- **Em dashes:** at most one per paragraph, only where a comma or full stop would lose the
  structure.
- **Semicolons:** exceptional. Prefer a full stop and a new sentence.
- **Rule of three:** allowed when the list is substantive (three assumptions, three contributions).
  Banned as rhythmic decoration.
- **Parallel structure:** once per paragraph, for genuinely parallel content.
- **Parataxis:** fine in moderation. The vice is relentlessness.
- **Negative anaphora** ("No X. No Y. No Z."): rare, and only for real emphasis.

### Rejected prohibitions, and why

These four appear on the source list. They are wrong for this writing, and the reasoning is recorded
so the judgement can be argued with rather than merely obeyed.

**"No hedging qualifiers."** Rejected. Academic writing requires calibrated uncertainty. Split the
category:

- *Epistemic* hedges are mandatory. "Under these assumptions." "May mechanically produce the
  downward-sloping curves."
- *Rhetorical* hedges are the vice. "It could be argued that." "Somewhat." "Arguably." "Seems to
  suggest."
- **Test:** a hedge you can delete without changing the meaning is rhetorical. Delete it. Every
  survivor must name what is uncertain and why.

**"No nominalization."** Rejected. This field's technical vocabulary is nominalization: growth,
distribution, incidence, allocation, depreciation, measurement. You cannot write national accounts
without it. The real rule is narrower: do not nominalize a verb you could simply use. "We made an
allocation of income" becomes "we allocate income". "The implementation of the formula" becomes
"implementing the formula". **Test:** if the nominalization hides who did what, unpack it.

**"No antithesis. No contrasting pairs."** Rejected. Economic arguments often depend on contrast:
anonymous against non-anonymous growth, panel against cross-section, production against income
approach. "A menu, not a ranking" and "Factor income is not equal to GDP. It is the factor-payment
part of…" convey useful distinctions. Contrast must be informative, never decorative.

**"Write for the spoken voice."** Qualified. Keep it as the read-aloud test on prose. Do not apply it
to definitions, notation, or formal statements of assumptions, which need written precision.

**"No paragraph pinning."** Qualified. Topic sentences help academic readers navigate a long methods
section. The vice is *formulaic* pinning, where every paragraph opens with the same move. Vary the
opening instead of abandoning it.

---

## 5. What the list omits, and what matters more

The source list optimises for not sounding like a machine. That overlaps with good writing but is not
the same thing. These do more work.

**Instantiate every abstract result concretely.** For example, explain net national product
through a bakery: output of 10k, 1k to maintain the oven, so the baker earns 9k and the oven repairer
earns 1k. Use concrete parameter values to explain a theoretical result. A tiny worked case beats a
paragraph of definition.

**Signpost the intuition.** Use "The intuition for X is…" or "Intuitively, …" where helpful. Say the
plain-English version of every formal result, next to the formalism.

**State limitations flatly.** Concede the point directly. Do not hedge the limitation itself.

**Claim first, caveat second.** Do not bury the finding under three qualifications.

**One idea per sentence.**

**Numbers and specifics over adjectives.** "15,000 words sounds very long, aim for no longer than
10,000" gives a concrete target. No adjective does that work.

**Questions to orient the reader, sparingly.** Use them in titles or section openings when helpful.
Overused, they become their own tic.

**Cut sentences that only announce what follows,** unless the reader genuinely needs the map.

**Jargon:** use it when it is the precise term and the audience knows it. Gloss on first use. Never
use it to sound serious. When a plain word carries the same meaning, use the plain word: use over
utilise, show over demonstrate, help over facilitate. Do not mangle established technical terms to
achieve this.

---

## 6. Calibration

These measurements come from the first twelve pages of nine academic papers. The underlying
calibration corpus is not bundled here. Treat the ranges as illustrative examples for the paper-body
tier, not rules or a validated detector of AI authorship.

| Measure | Illustrative range |
|---|---|
| Median sentence length | 20-24 words, in every paper |
| Sentence-length SD | 14-19 words, range 2-125 |
| Em dashes per 1,000 words | 0.0 to 8.9, median ~3.9, about one per 250 words |
| "we" against "I" | "we" dominates, 23-52 to 1-13 |
| Question marks per paper | 1-13 |

The variance matters as much as the median. Mix short sentences with longer ones when the argument
needs them.
Uniform sentence length can make prose monotonous; it does not establish who wrote it.

---

## 7. Adapt the guide to the document

Use these examples as guidance. A solo-authored theory paper and a co-authored empirical measurement
paper may need different conventions.

**Keep where useful:** concrete numeric instantiation, explicit intuition signposting, flat
limitation statements, "we" for authorial action, short declaratives, questions as orientation.

**Avoid as defaults:** clichés ("double-edged sword"), theory-paper compression, question-titles and
frequent semicolons. Adapt the register to the document and its audience.

---

## 8. Project-specific rules

Read your project's own shared README and agent entry point for subject terminology, LaTeX
conventions, notation, citation rules and protected material. Respect any read-only passages or
review boundaries they identify. This distributed guide does not import protected paths or writing
rules from other projects.
