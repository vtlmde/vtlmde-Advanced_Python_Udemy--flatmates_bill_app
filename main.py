class bill: 
    """
    Object that contains data about a bill such as total amount
    and period of a bill.
    """

    def __init__(self, amount, period):
        self.amount = amount 
        self.period = period

class flatmate: 
    """
    Creates a flatmate person that lives in the flat and pays a share of the bill. 
    """

    def __init__(self,name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays( self , bill , flatmate2 ):
        weight = self.days_in_house / \
                 (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
        
class bill_pdf_report(bill):
    """
    Creates a PDF that contains data about the flatmates such as their names,
     their due amount, and the period of the bill. 
    """

    def __init__( self , filename ):
        self.filename = filename

    def generate( self , flatmate1 , flatmate2 ):
        from fpdf import FPDF
        pdf = FPDF(orientation= "P", unit='pt', format='A4')
        pdf.add_page()

        # Add some text
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
        pdf.cell(w=100, h=40, txt='Period:', border=1, align='C')
        pdf.cell(w=150, h=40, txt="March 2021", border=1, align='C')
        pdf.output('tuto1.pdf','F')


bill1 = bill ( amount=120 , period = "March 2021")
john = flatmate ( name="John" , days_in_house=20 )
mary = flatmate ( name="Mary" , days_in_house=25 )
print ( "John pays the following: $", john.pays( bill1 , mary ) )
print ( "Mary pays the following: $", mary.pays( bill1 , john ) )