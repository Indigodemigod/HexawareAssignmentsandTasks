from entity.Loans import Loan


class HomeLoan(Loan):
    def __init__(self, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status, address, value):
        super().__init__(customer, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.property_address = address
        self.property_value = value
