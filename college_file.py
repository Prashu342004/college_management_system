books = ["rich dad poor dad", "zero to one"]


class library:
    def __init__(self,books):
        self.books = books 
        self.books_available = books
        self.books_alloted = {}

    def book_issue(self,user):
        book_name = input("enter the book you want : ")
        if book_name in self.books:
            self.books_alloted[book_name] = user
            self.books_available.remove(book_name)
            print("book issued :) ")
        else:
            print("book not available")

    def book_return(self,book_name):
        for book in self.books_alloted.keys():
            if book_name == book:
                self.books_available.append(book)
                self.books_alloted.pop(book)
                print("book returned")
        else:
            print("book not issued")


class accounts:
    def __init__(self,total_amount,fee_paid):
        self.total_amount = total_amount
        self.fee_paid = fee_paid
    
    def remaining_fees(self):
        return self.total_amount - self.fee_paid
    def pay_fee(self):
        try:
            while True:
                amount = int(input("enter amount you want to pay "))
                if amount >0 and amount <= self.remaining_fees():
                    break
                else:
                    print("entered amount is zero or more than remaining amount please re enter the amount")

        except Exception as e:
            print(f"the issue is : {e}")

        card_no = input("enter card number")
        cvv = input("enter cvv")
        print("user details : ")
        print("card number : ",card_no)
        print("cvv number : ",cvv)
        while True:
            card_pin = input("enter pin")
            if len(card_pin) != 4:
                print("invalid card pin ")
            else:
                break
        self.fee_paid += amount
        print(f"  ==========fee paid ===============remaining amount = {self.remaining_fees()}===========")
        self.total_amount -= amount
        return self.fee_paid

class classroom:
    pass


class college:

    def __init__(self,fees_paid):
        self.library = library(books)
        self.accounts = accounts(10000,fees_paid)


    def book_issue_user(self,user):
        self.library.book_issue(user)

    def book_return_user(self,book_name):
        self.library.book_return(book_name)
    
    def pay_fee(self):
        f = self.accounts.pay_fee()
        return f


class sports:

    def play_sport(self):
        print("playing sports ")


class cultural:

    def perform_dance(self):
        print("performing dance ")