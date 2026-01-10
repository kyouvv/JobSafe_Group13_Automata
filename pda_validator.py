class PDAValidator:
    def __init__(self):
        self.stack = []
        self.current_state = 'q_start'
        self.log = [] 

        # TRANSITION
        self.transitions = {
            'q_start': {
                'H': ('q_header', None, None)
            },
            'q_header': {
                'H': ('q_header', None, None),       
                'R': ('q_role', 'PUSH', 'role_marker')
            },
            'q_role': {
                'R': ('q_role', None, None),         
                'D': ('q_term', None, None)
            },
            'q_term': {
                'D': ('q_term', None, None),         
                'S': ('q_scope', 'POP', 'role_marker')
            },
            'q_scope': {
                'S': ('q_scope', None, None),        
                'C': ('q_pay_base', 'PUSH', 'pay_marker')
            },
            'q_pay_base': {
                'C': ('q_pay_base', None, None),     
                'B': ('q_benefits', 'POP', 'pay_marker')
            },
            'q_benefits': {
                'B': ('q_benefits', None, None),     
                'F': ('q_legal', None, None)
            },
            'q_legal': {
                'F': ('q_legal', None, None),        
                'T': ('q_term_clause', None, None)
            },
            'q_term_clause': {
                'T': ('q_term_clause', None, None),  
                'X': ('q_accept', None, None)
            },
            'q_accept': {
                'X': ('q_accept', None, None)        
            }
        }

    def process_token(self, token):
       
        if token not in self.transitions.get(self.current_state, {}):
            error_msg = f"REJECT: Unexpected token '{token}' in state '{self.current_state}'."
            self.log.append(error_msg)
            return False

        
        new_state, action, marker = self.transitions[self.current_state][token]

   
        if action == 'PUSH':
            self.stack.append(marker)
            self.log.append(f"Action: PUSH '{marker}' -> Stack: {self.stack}")
        
        elif action == 'POP':
            if not self.stack or self.stack[-1] != marker:
                self.log.append(f"REJECT: Stack Violation. Expected to POP '{marker}', found {self.stack}")
                return False
            self.stack.pop()
            self.log.append(f"Action: POP '{marker}' -> Stack: {self.stack}")

       
        self.log.append(f"Transition: {self.current_state} -> {new_state} (Input: {token})")
        self.current_state = new_state
        return True

    def validate(self, token_stream):
        print(f"\n--- Starting Validation on tokens: {token_stream} ---")
        self.current_state = 'q_start'
        self.stack = []
        self.log = []

        for token in token_stream:
            if not self.process_token(token):
                return False, self.log 

        # FINAL CHECK
        if self.current_state == 'q_accept' and len(self.stack) == 0:
            return True, self.log
        else:
            self.log.append(f"REJECT: Ended in state '{self.current_state}' with Stack: {self.stack}")
            return False, self.log
