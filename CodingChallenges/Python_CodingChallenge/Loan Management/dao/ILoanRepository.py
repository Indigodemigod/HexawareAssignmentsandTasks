from abc import abstractmethod,ABC

from entity.Loans import Loan


class ILoanRepository(ABC):

    @abstractmethod
    def applyLoan(self, loan: Loan):
        pass

    @abstractmethod
    def calculateInterest(self, loanId):
        pass

    @abstractmethod
    def loanStatus(self, loanId):
        pass

    @abstractmethod
    def calculateEMI(self, loanId):
        pass

    @abstractmethod
    def loanRepayment(self, loanId, amount):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(self, loanId):
        pass