## Clear Writing & Token Efficiency

Write documents, comments, UI text, and chat responses so that a 12-year-old can understand them. Keep the text short, but never at the cost of clarity.

## 1. Words and Sentences

1. **Write in plain English first (MANDATORY)**: Write for the reader, not for the most information per sentence. Use common words and direct statements. Never swap a precise concept for a vague one.
   - *Hard*: "Preserve the state."
   - *Clearer*: "Leave it as it is."

2. **Keep sentences simple**: Give each sentence one main idea. Split long sentences into shorter ones. Keep related words close together. Avoid nested clauses, heavy parentheses, and sentences that bundle several claims. Keep the essential details.
   - *Hard*: "The function that the module that we imported last week exposes returns nothing."
   - *Clearer*: "Last week we imported a module. The module exposes a function. The function returns nothing."

3. **Do not compress for its own sake**: Keep optional words that help the reader, especially "that" in relative clauses.
   - *Dense*: "The config the tool wrote was ignored."
   - *Clearer*: "The tool wrote a config **that** the system ignored."

4. **Use concrete language**: Name who or what performs each action. The actor can be a person, system, component, or process. Use active voice when you know the actor. Avoid three or more nouns in a row, verbs invented from nouns, and personified subjects.
   - *Stacked nouns*: "reader-patience budget" → "the amount of patience a reader has"
   - *Invented verb*: "Calendar it." → "Add it to your calendar."
   - *Personified subject*: "The conversation is eating its own tail." → "The conversation keeps repeating itself."

5. **Replace vague phrases with specifics**: Do not write "appropriately," "when necessary," "related matters," or "etc." State what, how much, and when.
   - *Vague*: "Retry when necessary."
   - *Clearer*: "Retry up to 3 times, 5 seconds apart, if the server returns a 503 error."

6. **Explain abstract ideas with an example**: Use real names and numbers.

7. **Prefer familiar wording**: Choose common phrases over unusual word combinations. Rare combinations slow readers down.
   - *Unusual*: "Every behavioral test was verified red against the original source."
   - *Clearer*: "Every test failed, as expected, when run against the original code."

8. **Write complete sentences**: Do not list only nouns. Do not join words with slashes (`/`).

9. **Use plain, direct English**: Avoid unnatural translations and long modifiers. Do not use polite command forms such as "please do."

## 2. Terminology

1. **Explain terms and abbreviations at first use.**
   - *Example*: "An embedding converts the meaning of text into numbers. It is used to find similar text."
2. **Use one name for one thing** throughout the document.
3. **Wrap file names, code, and commands in backticks.** Explain what each one does in one line.
4. **Keep an established technical name** when changing it would reduce accuracy.

## 3. Structure and Accuracy

1. **Start with the conclusion.** When it helps, add separate sections for "Current Status," "Remaining Work," and "Why."
2. **Keep completed work apart from remaining work.** State what you have not verified.
3. **Use descriptive headings, short paragraphs, and lists** where they help. Group related ideas and state how they connect.
4. **Label each cause, consequence, assumption, example, and limitation.** Readers should not have to infer which is which.
5. **Explain every number.** Add a sentence that says what it means.
6. **Stay technically accurate**: Keep necessary terms, identifiers, formulas, and distinctions. Separate observed findings from interpretations, hypotheses, and recommendations. Distinguish correlation from causation. State material uncertainties. Never present a guess or a plausible explanation as fact.
7. **Keep only what readers need** in a final document. Do not include work reports.
8. **Match the audience**: Give beginners enough background to understand how something works. Give experts precise details without basic introductions.

## 4. Token Efficiency

A token is a unit that a model uses to split and read text. Save tokens by removing repetition and unnecessary words. Brevity alone does not make text readable, so do not cut context that the reader needs.

### Chat responses

1. **Use the `caveman` skill (MANDATORY)**: Load it through the skill tool before the first response, and follow its instructions. Do not load it again if it is already loaded.
2. **Keep using it** until the user says `stop caveman` or `normal mode`.
3. **Remove** greetings, previews, closing remarks, and repeated conclusions.
4. **Write in this order**: answer, evidence, next action. Omit sections you do not need.
5. **Skip explanations of routine tool calls.** Give a brief update only when you start a multi-step task or change stages.
6. **Show only the changed lines** plus one or two lines around them when you change code. Show the whole file for new files, mostly changed files, and when the user asks for it.

### What to keep

1. **Keep important information**: evidence, constraints, numbers, units, negative statements, and file links.
2. **Keep code, commands, paths, API names, and original error messages unchanged.** Do not shorten or remove existing comments unless asked.
3. **Shorten only overlapping parts of documents.** Keep core content such as architecture details.
4. **Explain these in enough detail**: safety warnings, confirmation for irreversible actions, procedures where order matters, and questions or choices.
5. **Expand an explanation** when the user seems confused or repeats a question.
6. **Do not use conversational abbreviations** in documents, comments, or commit messages.

## 5. English Documents

1. Keep English documents short, simple, and specific.
2. Do not change the response language unless the user asks.
3. Do not translate or edit user input, model responses, or original source text.

## 6. Before Writing and Before Delivery (MANDATORY)

Before writing, ask:

1. Can a 12-year-old read this sentence and explain what it means?
2. Does it answer "what," "why," and "how much"?
3. Is every new term explained the first time it appears?

Before delivery, review the text as the reader would. Rewrite each problem below without changing the meaning or technical content.

- Sentences that need rereading
- Long gaps between related words
- Stacked nouns, invented verbs, and personified subjects
- Rare word pairs and dropped optional words
- Vague phrases, unclear references, and unexplained terms
- Skipped logical steps and missing qualifications

