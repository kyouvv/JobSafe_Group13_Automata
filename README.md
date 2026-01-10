Code Guide Dashboard

The Code is working. It runs, it has a UI, and it validates structure.
Logic is "Strict" so if a contract is missing a section, it will REJECT it.

PLease me Help fix the Gaps and Discrepancies listed below.

File Directory 

app.py: The UI. Handles file uploads (PDF/TXT) and displays results.
symbol_mapper.py: The Translator It looks for keywords and turns them into tokens (H, R, D, etc.).
pda_validator.py: The central system This is the Pushdown Automata logic. It checks the sequence and manages the Stack.

Discrepancies that i noticed
We need to address these before final submission

- Currently, if a contract skips any section (like a missing "Duration"), it rejects it. actual conrtracts may not be like that. We need to decide if some sections should be optional.
- If a contract uses a word we haven't listed (e.g., "Monthly Stipend" instead of "Basic Pay"), the mapper will miss it and cause a crash.
- Raw Txt lang ang kaya muna for now (i havent implemented the pdf version yet. will do this coming week)

PLease help me and contribute
Tasks
- Expand the Dictionary (symbol_mapper.py)
- We need more keywords.

Action: Open symbol_mapper.py, look at the self.rules dictionary, and add more synonyms for "Salary," "Duties," and "Signatures" that you find in actual contracts na makikita nyo.


- Try to "break" the program code.

Action: Find 5 different employment contracts online. Save them as txts. Upload them to the app. then let us know the results of your testing

Goal: Explain the Math.

Action: We need a formal State Transition Table and CFG Rules for the paper. We currentlu have a simple logic and I need someone to write it down sa documentation.

Open Terminal in this folder (dont forget these commands cuz ndi gagana sa local device nyo to if skipped)

source venv/bin/activate
streamlit run app.py
pip install pypdf (optional)
