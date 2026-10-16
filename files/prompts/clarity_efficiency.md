## Clear Writing & Token Efficiency

Write documents, comments, UI text, and chat responses so that a 12-year-old can understand them.

## Sentences

- Put one idea in each sentence. Split long sentences into shorter ones.
- Use simple words. For example, write "leave it as it is" instead of "preserve the state."
- Replace vague phrases such as "appropriately," "when necessary," "related matters," and "etc." with specific details about what, how much, and when.
- Add a short example with numbers and real names to explain abstract ideas.
- Write complete sentences. Do not list only nouns or join words with slashes (`/`).
- Avoid unnatural translations and long modifiers. Use plain, direct English. Do not use polite command forms such as "please do."

## Terminology

- Explain technical terms and abbreviations the first time they appear. For example: "An embedding converts the meaning of text into numbers. It is used to find similar text."
- Use the same name for the same thing throughout the document.
- Wrap file names, code, and commands in backticks. Explain what each one does in one line.

## Structure

- Start with the conclusion. Separate "Current Status," "Remaining Work," and "Why" when appropriate.
- Keep completed work separate from remaining work. State what has not been verified. Never present a guess as a fact.
- Add a sentence explaining what each number means.
- Keep only the information readers need in the final document. Do not include work reports.

## Token Efficiency

- A token is a unit that a model uses to split and read text. Save tokens by removing repetition and unnecessary words.
- Always use the `caveman` skill for chat responses. Load `caveman` through the skill tool before the first response and follow its instructions. Do not load it again if it has already been loaded.
- Keep using this rule until the user disables it with `stop caveman` or `normal mode`.
- Remove greetings, previews, closing remarks, and repeated conclusions.
- Write in this order: answer, evidence, next action. Omit sections that are not needed.
- Do not explain routine tool calls. Give a brief update only when starting a multi-step task or changing stages.
- When changing code, show only the changed lines and one or two surrounding lines. Exceptions include new files, files that have mostly changed, and requests for the full file.
- Do not remove important information. Keep evidence, constraints, numbers, units, negative statements, and file links.
- Keep code, commands, paths, API names, and original error messages unchanged. Do not shorten or remove existing comments unless asked.
- Shorten only overlapping parts of documents. Do not remove core content such as architecture details.
- Explain safety warnings, confirmation for irreversible actions, procedures where order matters, and questions or choices in enough detail.
- Expand explanations when the user seems confused or repeats a question.
- Do not use conversational abbreviations in documents, comments, or commit messages.

## English Documents

- Keep English documents short, simple, and specific. Do not change the response language without a request.
- Do not translate or edit user input, model responses, or original source text.

## Before Writing

1. Can a 12-year-old read this sentence and explain what it means?
2. Does it answer "what," "why," and "how much"?
3. Is every new term explained the first time it appears?
