# Pamela Walton | SDEV140 with Professor Newell | May 14th 2023 
# Assignment details: "Final Project Submission"

# ______________________________________________________________________________________________

# Step 1 - Ensure all modules are imported
import tkinter as tk
import csv
from datetime import datetime, timedelta
from PIL import Image, ImageTk

# Step 2 - Set the definitions for calculating monthly payment

def determineMonthlyPayment(P, r, n):
    r = r / (12 * 100) 
    M = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return M

# Step 3 - Set the definitions for Define calculating remaining balance

def determineRemainingBalence(P, r, n, x):
    r = r / (12 * 100)  
    B = P * ((1 + r)**n - (1 + r)**x) / ((1 + r)**n - 1)
    return B

# Step 4 - Create the GUI with the tkinter module

root = tk.Tk()
root.title("Mortgage Calculator")
root.maxsize(700, 800)
root.minsize(700, 700)

# Step 5 - Create the button images for later use

submitImage = ImageTk.PhotoImage(Image.open("submit.png").resize((200, 75)))
quitImage = ImageTk.PhotoImage(Image.open("quit.png").resize((200, 75)))
scheduleImage = ImageTk.PhotoImage(Image.open("schedule.png").resize((200, 75)))


# Step 6 - Setting a background image as border

borderImage = Image.open('border.jpg')
borderPhoto = ImageTk.PhotoImage(borderImage)
borderLabel = tk.Label(root, image=borderPhoto)
borderLabel.place(x=0, y=0, relwidth=1, relheight=1)

contentFrame = tk.Frame(root, bg='#F0F0F0')  
contentFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)  

# Step 7 - Setting the frame to display a large set of information to user at the end of the program

scheduleFrame = tk.Frame(contentFrame)
scheduleLabel = tk.Label(scheduleFrame, image=scheduleImage)
scheduleLabel.pack()
scheduleFrame.pack(side='top', pady=(50,0))

# Step 8 - Create the space where the prompts will be placed

questionsFrame = tk.Frame(contentFrame)
questionsFrame.pack(side='top', pady=15, expand=True)

# Step 9 - Create the perpetual space where the quit button will be placed

quitFrame = tk.Frame(contentFrame)
quitFrame.pack(side='bottom', pady=(0,15))

# Step 10 - Set numerical definitions use in the mortgage calculation

P = None
downPayment = None
startDate = None
r = None

# Step 11 - Get the Loan amount from the user

def submitLoanAmount():
    global P
    P = float(loanAmountEntry.get().replace(',', ''))
    label1.pack_forget()
    loanAmountEntry.pack_forget()
    submitButton1.pack_forget()
    label2.pack(pady=(20,20))
    downPaymentEntry.pack()
    submitButton2.pack()

# Step 12 - Get the down payment amount from the user

def submitDownPayment():
    global downPayment
    downPayment = float(downPaymentEntry.get().replace(',', ''))
    label2.pack_forget()
    downPaymentEntry.pack_forget()
    submitButton2.pack_forget()
    label3.pack(pady=(20,20))
    annualInterestRateEntry.pack()
    submitButton3.pack()

# Step 13 - Get the annual interest amount from the user

def submitAnnualInterestRate():
    global r
    r = float(annualInterestRateEntry.get().replace(',', ''))
    label3.pack_forget()
    annualInterestRateEntry.pack_forget()
    submitButton3.pack_forget()
    label4.pack(pady=(20,20))
    startDateEntry.pack()
    submitButton4.pack()

# Step 14 - Get the Loan start date from the user

def submit_startDate():
    global startDate
    startDate = datetime.strptime(startDateEntry.get(), "%Y-%m-%d")
    label4.pack_forget()
    startDateEntry.pack_forget()
    submitButton4.pack_forget()
    generate_schedule(P - downPayment, r, 30*12, startDate)

# Step 15 - Create the payment schedule

def generate_schedule(P, r, n, startDate):
    schedule = []
    for x in range(1, n+1):
        M = determineMonthlyPayment(P, r, n)
        B = determineRemainingBalence (P, r, n, x)
        paymentDate = startDate + timedelta(days=30*x)
        schedule.append([x, paymentDate.strftime('%b, %Y'), "{:.2f}".format(M), "{:.2f}".format(B), "{:.2f}".format(x * M)])

# Step 16 - Create the CSV file which can be imported into excel later

    with open("MonthlyMortgagePayments.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Payment Number", "Payment Date", "Monthly Payment", "Remaining Balance", "Total Paid"])
        writer.writerows(schedule)

# Step 17 - Create a text widget for inserting and displaying the data

    resultText = tk.Text(questionsFrame)
    resultText.pack(pady=(15,0))
    resultText.insert(tk.END, "Payment Number  Payment Date  Monthly Payment  Remaining Balance  Total Paid\n")
    padding = [len("Payment Number  "), len("Payment Date  "), len("Monthly Payment  "), len("Remaining Balance  "), len("Total Paid  ")]
    for row in schedule:
        resultText.insert(tk.END, "".join([str(row[i]).ljust(padding[i]) for i in range(5)]) + "\n")

# Step 18 - Create the labels for all of the text and buttons on the window

label1 = tk.Label(questionsFrame, text="How much is the House?", font=('Arial', 20))
loanAmountEntry = tk.Entry(questionsFrame)
submitButton1 = tk.Button(questionsFrame, text="Submit", command=submitLoanAmount, image=submitImage, borderwidth=0)

label1.pack(pady=(0,20))
loanAmountEntry.pack()
submitButton1.pack()

label2 = tk.Label(questionsFrame, text="How much is your down payment?", font=('Arial', 20))
downPaymentEntry = tk.Entry(questionsFrame)
submitButton2 = tk.Button(questionsFrame, text="Submit", command=submitDownPayment, image=submitImage, borderwidth=0)

label3 = tk.Label(questionsFrame, text="What is the annual interest rate?", font=('Arial', 20))
annualInterestRateEntry = tk.Entry(questionsFrame)
submitButton3 = tk.Button(questionsFrame, text="Submit", command=submitAnnualInterestRate, image=submitImage, borderwidth=0)

label4 = tk.Label(questionsFrame, text="When will this loan begin? (format: YYYY-MM-DD):", font=('Arial', 15))
startDateEntry = tk.Entry(questionsFrame)
submitButton4 = tk.Button(questionsFrame, text="Submit", command=submit_startDate, image=submitImage, borderwidth=0)

# Step 19 - Create the quit button which will end the program if selected. 

quitButton = tk.Button(quitFrame, text="Quit", command=root.destroy,  image=quitImage, borderwidth=0)
quitButton.pack()

root.mainloop()
