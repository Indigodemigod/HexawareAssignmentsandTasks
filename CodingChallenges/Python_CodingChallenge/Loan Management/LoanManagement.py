from entity.CarLoan import CarLoan
from entity.HomeLoan import HomeLoan
from dao.ILoanRepositoryImpl import ILoanRepositoryImpl


class LoanManagement(ILoanRepositoryImpl):
    def __init__(self):
        super().__init__()

    def main(self):
        while True:
            print("----Menu----")
            print("1. Apply loan.")
            print("2. Get All Loan History.")
            print("3. Get Your Loan Details.")
            print("4. Make Loan repayment.")
            print("5. Get Loan status.")
            print("6. Exit")
            choice = int(input("Enter your choice here : "))
            match choice:
                case 1:
                    loan = None
                    customer = self.get_customer()
                    loan_amount = float(input("Enter the amount you want to borrow : "))
                    interestRate = float(input("Enter the interest rate : "))
                    loanterm = int(input("Enter the tenure for which you want to take loan : "))
                    loanType = input("Enter your loan type (HomeLoan/CarLoan) : ")
                    loanstatus = "Pending"
                    if loanType == "HomeLoan":
                        propertyAddress = input("Enter the address of the property : ")
                        propertyValue = float(input("Enter the value of the property : "))
                        loan = HomeLoan(customer, loan_amount, interestRate, loanterm, loanType, loanstatus,
                                        propertyAddress, propertyValue)
                    elif loanType == "CarLoan":
                        carModel = input("Enter car model : ")
                        carValue = float(input("Enter the value of car : "))
                        loan = CarLoan(customer, loan_amount, interestRate, loanterm, loanType, loanstatus, carModel,
                                       carValue)
                    self.applyLoan(loan)
                    print("We're heading you to main menu.")
                    print()
                case 2:
                    loans = self.getAllLoan()
                    for l in loans:
                        print("Loan id : ", l[0])
                        print("Customer Id : ", l[1])
                        print("Principal Amount : ", l[2])
                        print("Interest Rate : ", l[3])
                        print("Loan term : ", l[4])
                        print("Loan type : ", l[5])
                        print("Loan status : ", l[6])
                        print("----------------------------------")
                case 3:
                    loanId = int(input("Please enter your loan ID : "))
                    loans = self.getLoanById(loanId)
                    for l in loans:
                        print("Loan id : ", l[0])
                        print("Customer Id : ", l[1])
                        print("Principal Amount : ", l[2])
                        print("Interest Rate : ", l[3])
                        print("Loan term : ", l[4])
                        print("Loan type : ", l[5])
                        print("Loan status : ", l[6])
                        print("------------------------------------")

                case 4:
                    loanId = int(input("Enter your loan Id : "))
                    amount = float(input("Enter the amount you want to repay : "))
                    self.loanRepayment(loanId, amount)
                    print()
                case 5:
                    loanId = int(input("Enter your loan id : "))
                    self.loanStatus(loanId)
                    print()
                case 6:
                    print("Thanks for visiting us. Have a good day.")
                    break
                case _:
                    print("Invalid input please try again.")


loan = LoanManagement()
loan.main()