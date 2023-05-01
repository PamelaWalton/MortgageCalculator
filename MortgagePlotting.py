# Pamela Walton | SDEV140 with Professor Newell | April 30th 2023 
# Assignment details: "Provide a progress update on the final project"

# Explanation: My current progress can be found here as I am currently plotting my strategy through psuedocode. However, a detailed description of this information can be found in the word document that is attached.

# Step 1 - Import the GUI library tkinker

import tkinter as tk

# Next step:  Creat a funtion for calculating the mortage size and payment schedule.

# Next step: 
1 - Import the GUI library tkinker

# Next step: 
2 - Define and set all variable to open strings or zero

# Next step: 
3 - Define the equation for calculating the mortgage called: mortgageEquation. This will be comprised of a few varaibles, including: (1) homeCost (2) downPayment (3) loanAmount (4) interestRate and (5) loanDuration

# Next step: 
4 - Create a function, called 'estimate', which 
(4.1) converts interestRate to a monthlyPayment
(4.2) determine how much, using monthlyPayment, interestRate and loanDuration, will be spent in interest alone #This will be useful later in determining the difference between monthly and bi weekly payment strategies.
(4.3) print the monthlyPayment in the form of a paymentSchedule with interestRate included at each iteration #I would like to code this where it creates an excel sheet with all of that information printed out. 
(4.4) print the monthly payment to the user

# Next step: 
5 - Create a function for step number four of the previous function. This will entail
(5.1) getting loanAmount from corresponding input tkinker widget
(5.2) getting interestRate from corresponding input tkinker widget
(5.3) getting loanDuration from corresponding input tkinker widget
(5.4) call the estimate function with loanAmount, interestRate, and loanDuration
(5.5) update a variable, called 'mortgagePayment' based on the result of the estimate function with the calculated mortgage payment

# Next step: 
6 - create the main function (mian())
(6.1) Create the GUI main window which shows all the information the user will be asked to provide #In anticipating how a user would use this, It would be helpful for them to know right from the get go what information they should have on hand. 
(6.2) Create buttons to begin, where each stage is a new section # Ideally I want a 'go back' feature but I will have to learn how to do that
(6.3) Use tkinker GUI Widgets to get values for loanAmount, interestRate and loanDuration which will be used in steps 4 and 5
(6.4) Create a button to initiate step 5 and retrieve the mortgagePayment variable value
(6.5) Initiate the tkinker main loop #this step feels like it should be the first, but I have to remember is goes last!

# Next step: 
7 Call the main function to run these processes 

# Notes: Ideally, I would like to include a featur eto optimize a loan, such as including what payments would look like if paid 1/2 every 2 weeks instead of in full every month. Additionally, possibly also a calculation to show at what interest rate it would be finacially smart to refinace. 