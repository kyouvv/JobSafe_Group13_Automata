import re

class SymbolMapper:
    def __init__(self):
        # 1. Define Rules with Regex Boundaries
        # r'' indicates a raw string, essential for regex patterns.
       self.rules = {
            'H': [r'\bemployment agreement\b', r'\bcontract of employment\b', r'\bknow all men\b', r'\bservice agreement\b', r'\bletter of offer\b'],
            'R': [r'\bposition\b', r'\bjob title\b', r'\bdesignation\b', r'\bhired as\b', r'\brank\b'],
            # Refinement: 'term' matches only if NOT followed by 'ination' to avoid T overlap
            'D': [r'\bterm\b(?!ination)', r'\beffective date\b', r'\bprobationary\b', r'\bstart date\b', r'\bperiod of employment\b', r'\bduration\b'], 
            'S': [r'\bduties\b', r'\bresponsibilities\b', r'\bfunctions\b', r'\bdeliverables\b', r'\bscope of work\b', r'\bobligations\b', r'\bjob description\b'],
            'C': [r'\bbasic pay\b', r'\bmonthly rate\b', r'\bgross salary\b', r'\bremuneration\b', r'\bhourly rate\b', r'\bcompensation\b', r'\bsalary\b'],
            'B': [r'\ballowance\b', r'\b13th month\b', r'\bhmo\b', r'\bincentives\b', r'\bsss\b', r'\bphilhealth\b', r'\bpag-ibig\b', r'\binsurance\b', r'\bbenefits\b'],
            'F': [r'\bconfidentiality\b', r'\bnon-disclosure\b', r'\bdata privacy\b', r'\bproprietary\b', r'\bintellectual property\b'],
            'T': [r'\bresignation\b', r'\btermination\b', r'\bnotice period\b', r'\bbreach\b', r'\bseparation\b', r'\bend of contract\b'],
            'X': [r'\bsigned\b', r'\bwitness\b', r'\bconforme\b', r'\baccepted by\b', r'\bsignature\b']
        }

    def get_symbol(self, line):
        clean_line = line.strip().lower()
        if not clean_line:
            return None

        # Optimization: Limit search scope for long lines to avoid false positives in body text
        search_text = clean_line
        words = clean_line.split()
        if len(words) >= 20:
            search_text = " ".join(words[:15])

        for symbol, patterns in self.rules.items():
            for pattern in patterns:
                # We use re.search to find the pattern anywhere in the filtered line
                if re.search(pattern, search_text, re.IGNORECASE):
                    return symbol

# --- Quick Test Block ---
# You can run this file directly to test it: 'python symbol_mapper.py'
if __name__ == "__main__":
    mapper = SymbolMapper()
    
    test_lines = [
        "Frankly, I think this is a good idea.",       # Should be None (previously matched 'rank' -> R)
        "The Position is Junior Dev",                 # Should be R
        "This contract has a long term duration.",    # Should be D
        "We need strictly confidential treatment."    # Should be F
    ]

    print("--- Testing Symbol Mapper v2.0 ---")
    for line in test_lines:
        token = mapper.get_symbol(line)
        print(f"Input: '{line}' -> Detected: {token}")