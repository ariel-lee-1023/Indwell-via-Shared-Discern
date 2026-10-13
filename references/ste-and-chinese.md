# STE principles and adaptation for Chinese

This reference distinguishes summaries of official rules, adaptations for Chinese, and methods introduced by this skill. Rule locations refer to ASD-STE100 Issue 9; see the [source notes](sources.md). This is a selective paraphrase, not an official translation or a complete rule list. Chinese-specific guidance applies when the user is communicating in or requests Chinese; it does not establish a default response language.

## Relevant official rules

| Rule location | Relevant point |
|---|---|
| 1.1, 1.11 | Technical terms are allowed alongside general vocabulary; name the same technical object consistently |
| 3.6 | Use active voice; passive voice is permitted in descriptive writing when the agent is unknown |
| 4.2, 4.4 | Do not shorten sentences by omitting necessary words; connect related sentences |
| 5.1–5.4 | Procedural sentences have a 20-word English limit; normally one instruction per sentence, with exceptions for simultaneous actions; state necessary conditions first |
| 5.5 | Notes must not carry mandatory instructions, requirements, or limits |
| 6.1–6.6 | Develop descriptions progressively; sentences have a 25-word English limit; one topic per paragraph, with a six-sentence maximum |
| 9.1 | Restructure a sentence when word-for-word substitution is insufficient |

English word counts are also governed by Section 8; counting spaces alone does not establish formal compliance. Consult the official dictionary for parts of speech, approved meanings, and verb forms. Ordinary simple English is not automatically formal STE.

## Adaptation for Chinese: retain the purpose, not mechanical conversions

These are this skill's design choices, not an official Chinese STE standard.

1. **Keep names stable and explain terms.** Introduce a necessary term with a short explanation, then use it consistently. Do not replace every specialist concept with “tool” or “system”; similar names need not identify the same object.
2. **Make actions and relationships clear.** Prefer explicit subjects and verbs. Preserve an unknown agent or cause rather than fill it in from common sense.
3. **Organize sentences around a manageable point.** Split a long sentence when it obstructs understanding, preserving concurrency, comparison, negation, and subordination. Do not convert 20/25 English words into a Chinese character limit.
4. **State prerequisites before action.** When a condition governs whether an action is possible, state it first. If the condition is unknown, identify the gap.
5. **Keep connections across paragraphs.** Retain causal, conditional, and concurrent connections when warranted. Make implicit relationships explicit rather than delete connecting words for superficial brevity.
6. **Distinguish description from procedure.** Explanations build background; procedures specify sequence, branches, and completion conditions. Let comprehension govern paragraph length rather than treat six sentences as a Chinese pass threshold.
7. **Prioritize accuracy over form.** Preserve probabilities, scope, and evidence strength. A longer accurate sentence is preferable to a shorter false one. Conversational wording must not turn a conditional recommendation into an unconditional requirement.

Do not derive Chinese banned-word lists from English rules or categorically prohibit passive constructions, semicolons, metaphors, terminology, or repetition. No “STE percentage” is guaranteed.

## Understanding-oriented design introduced by this skill

These methods support individual learning; they are not attributed to ASD-STE100:

- Identify the obstacle before choosing text, a diagram, or an interactive page.
- Preserve mechanisms, evidence, and limits; state missing evidence explicitly.
- Explain an analogy's structural correspondences and where they break down.
- Define diagram-arrow meanings and distinguish the basis of a calculation from teaching assumptions.
- Change the explanation when a learner remains confused rather than cycle through the same paragraph.
- Consider discrimination of conditions, actions, revisions, and optional explanations together. Do not force paraphrase or infer mastery from fluency, short sentences, low word counts, or style scores.

## Original counterexamples: smoother wording that changes meaning

| Source statement | Distorting simplification | Faithful treatment |
|---|---|---|
| The file was corrupted during transmission; the cause is unknown | The transmission program corrupted the file | Preserve the event and unknown cause |
| A change was observed only in internal reports | It works for all documents | Preserve the tested material's scope |
| It may reduce reading time | It reduces reading time | Preserve uncertainty |
| Format and permissions are checked simultaneously | Format is checked first, then permissions | Preserve concurrency |
| Processing begins only if both checks pass | Processing continues when either check passes | Preserve the requirement that all conditions hold |
| A trial observed A and B changing together | A caused B | Preserve association; causation requires further evidence |

If smoother wording would sacrifice meaning, keep the necessary precision and identify the specific difficulty.
