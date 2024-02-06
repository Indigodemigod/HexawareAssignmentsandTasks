from entity.Loans import Loan


class CarLoan(Loan):
    def __init__(self, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status, car_model, car_value):
        super().__init__(customer, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.car_model = car_model
        self.car_value = car_value
