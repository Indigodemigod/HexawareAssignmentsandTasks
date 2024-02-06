from entity.CarLoan import CarLoan
from entity.Customers import Customer
from util.DBUtil import DBUtil
from entity.HomeLoan import HomeLoan
from dao.ILoanRepository import ILoanRepository
from exception.InvalidLoanException import InvalidLoanException
from entity.Loans import Loan


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        super().__init__()
        self.con = DBUtil.getDBConn()

    def get_customer(self):
        print("Are you a new customer?")
        choice = input("Enter yes or no : ").lower()
        if choice == "no":
            customer_id = int(input("Enter your customer id : "))
            cursor = self.con.cursor()
            cursor.execute("select * from customers where customer_id = %s", (customer_id,))
            customer_data = cursor.fetchone()
            if customer_data:
                name = customer_data[1]
                email = customer_data[2]
                phone = customer_data[3]
                address = customer_data[4]
                creditscore = customer_data[5]
                customer = Customer(name, email, phone, address, creditscore)
                customer.customerId = customer_id
                return customer
        elif "yes":
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            phone = input("Enter your phone : ")
            address = input("Enter your address : ")
            creditScore = int(input("Enter your credit score : "))
            cursor = self.con.cursor()
            q = "insert into customers(name,email,phone,address,creditScore) values (%s,%s,%s,%s,%s)"
            cursor.execute(q, (name, email, phone, address, creditScore,))
            self.con.commit()
            customer_id = cursor.lastrowid
            customer = Customer(name, email, phone, address, creditScore)
            customer.customerId = customer_id
            print("You're successfully registered as a new customer.")
            print(f"Your customer id is {customer_id}")
            return customer

    def applyLoan(self, loan: Loan):
        confirm = input("Please confirm if you want to apply for loan (Yes/No)").lower()
        if confirm == "yes":
            cursor = self.con.cursor()
            query = "insert into loan (customer_id,principal_amount,interest_rate,loan_term,loan_type,loan_status) values (%s,%s,%s,%s,%s,%s)"
            values = (loan.customer.customer_id, loan.principal_amount, loan.interest, loan.loan_term, loan.loan_type,
                      loan.loan_status)
            cursor.execute(query, values)
            self.con.commit()
            loan.loan_id = cursor.lastrowid
            loan_id = loan.loan_id
            if isinstance(loan, HomeLoan):
                q_home = "insert into HomeLoan (loan_id,propertyAddress,propertyValue) values (%s,%s,%s)"
                loanData = (loan_id, loan.property_address, loan.property_value)
                cursor.execute(q_home, loanData)
                self.con.commit()
            elif isinstance(loan, CarLoan):
                q_car = "insert into CarLoan (loan_id, carModel, carValue) values (%s,%s,%s)"
                loanData = (loan_id, loan.car_model, loan.car_value)
                cursor.execute(q_car, loanData)
                self.con.commit()
            print("Congratulations! You've successfully applied for the loan.")
            print(f"Your loan id is {loan_id}")
        else:
            print("Loan application cancelled.")

    def calculateInterest(self, loanId):
        cursor = self.con.cursor()
        cursor.execute("select interest_rate from loan where loan_id=%s", (loanId, ))
        monthly_interest = cursor.fetchone()
        if monthly_interest:
            return monthly_interest[0]/1200
        else:
            raise InvalidLoanException("Loan not found")

    def loanStatus(self, loanId):
        cursor = self.con.cursor()
        cursor.execute("select creditScore from customers join loan on loan.customer_id=customers.customer_id and loan_id = %s", (loanId, ))
        stat = cursor.fetchone()
        if stat:
            credScore = stat[0]
            if credScore > 650:
                q = "update loan set loan_status='Approved' where loan_id=%s"
                cursor.execute(q, (loanId, ))
                self.con.commit()
                print("Congratulations! Your loan is Approved.")
            else:
                q = "update loan set loan_status='Rejected' where loan_id=%s"
                cursor.execute(q, (loanId,))
                self.con.commit()
                print("Sorry! Your loan is rejected due to low credit score.")
        else:
            raise InvalidLoanException("Loan not found.")

    def calculateEMI(self, loanId):
        cursor = self.con.cursor()
        query = "select principal_amount,interest_rate,loan_term from loan where loan_id=%s"
        cursor.execute(query, (loanId,))
        loan_data = cursor.fetchone()
        if loan_data:
            principal, interest_annual, term = loan_data
            interest = self.calculateInterest(loanId)
            emi = (principal*interest*(1+interest)**term)/(((1+interest)**term)-1)
            return emi
        else:
            InvalidLoanException("Loan not exists.")

    def loanRepayment(self, loanId, amount):
        cursor = self.con.cursor()
        query = "select principal_amount,interest_rate,loan_term from loan where loan_id=%s"
        cursor.execute(query, (loanId,))
        loan_data = cursor.fetchone()
        if loan_data:
            principal, interest, loanTerm = loan_data
            emi = self.calculateEMI(loanId)
            emi_possible = amount//emi
            if emi_possible < 1:
                print("Payment Rejected. Amount is less than a single EMI. ")
            else:
                print(f"{int(emi_possible)} EMI's paid from the amount.")
        else:
            raise InvalidLoanException("Loan Not Found.")
        print("We're heading you to main menu.")

    def getAllLoan(self):
        cursor = self.con.cursor()
        cursor.execute("select * from loan")
        return cursor.fetchall()

    def getLoanById(self, loanId):
        cursor = self.con.cursor()
        cursor.execute("select * from loan where loan_id=%s", (loanId,))
        return cursor.fetchall()
