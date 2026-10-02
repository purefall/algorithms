# Amazon Applied Scientist Coding Preparation

30 original practice exercises tailored to the examples in your recruiter’s brief. These are practice prompts, not claims about actual interview questions. Python 3.10+; standard library only.

## Start on Windows
Extract the ZIP so this README is at `C:\Users\berka\OneDrive\Documents\Python Scripts\algorithms\README.md`. The archive contains an `algorithms` folder: extract into its parent `Python Scripts` to avoid nesting.

Open PowerShell in algorithms. Check Python with `python --version` (or use `py -3` in place of python).

1. Read PREP_PLAN.md and the selected problem.md only.
2. Write attempt.py under a 30–35 minute timer; disable autocomplete and AI assistance during timed attempts.
3. Explain your reasoning aloud. Manually dry-run before running code.
4. Run `python problems/two_pointers/06_pair_less/tests.py` to check your attempt.
5. Read explanation.md and solution.py only after finishing the attempt.
6. Record the retrospective and tracker; copy attempt.py to attempts/attempt_YYYYMMDD.py before retrying from scratch.

Reference check: `python problems/two_pointers/06_pair_less/tests.py --solution`.
Check all reference solutions: `python tools/check_all.py --solution`.
Check all attempts: `python tools/check_all.py` (unfinished templates fail by design).

Pattern folders reveal algorithm families. For mixed mocks, use the neutral numbered prompts in mocks and avoid browsing category folders first. Tests may reveal extra examples; open them after your manual dry-run.

## Repository contents
Each problem has problem.md, attempt.py, solution.py, tests.py, explanation.md and retrospective.md. Also included: pattern notes, a mental-model cheatsheet, a tracker, a problem-generation prompt, and three mock prompts.

Optional local Git initialization: `git init`, `git add .`, then `git commit -m "Initial interview preparation curriculum"`.

## Interview routine
Clarify → baseline → identify repeated work → invariant → code → dry-run → complexity → follow-up. Ask for a hint if stuck and explain how it changes your reasoning.

## Limits
Tests cover examples and selected edge cases; passing them is not a proof of correctness. Contracts specify valid inputs rather than requiring exhaustive input validation. No dependencies, accounts, or API keys are needed.
