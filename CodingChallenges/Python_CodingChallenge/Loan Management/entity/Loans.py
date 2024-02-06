class Loan:
    def __init__(self, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status):
        self.customer = customer
        self.loan_id = None
        self.principal_amount = principal_amount
        self.interest = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    @property
    def loanId(self):
        return self.loan_id

    @loanId.setter
    def loanId(self, loan_id):
        self.loan_id = loan_id