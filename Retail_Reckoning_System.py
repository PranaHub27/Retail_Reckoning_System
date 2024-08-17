import math
import os
import smtplib
import tempfile
from tkinter import *
from tkinter import messagebox

title = 'AccuPay'
iconFileName = 'RupeeIconForBilling Project.ico'
size = '1270x685'
headingLabelTitle = 'Retail Reckoning System'
fontStyle = 'times new roman'
headerFontSize = 30
boldFont = 'bold'
backgroundColor = 'MediumPurple4'
fontColor = 'gold'
labelBorderSize = 12
fontSize = 15
fieldFontColor = 'white'
fieldBorderSize = 7
entryWidth = 7
totalEntryWidth = 10
customerDetailsFrameTitle = 'Customer Details'
customerDetailsTitlesList = ['Customer Name', 'Phone Number', 'Bill Number']
customerDetailsLabelList = []
customerDetailsEntryList = []

searchButtonTitle = 'Search'
buttonsTitlesList = ['Total', 'Bill', 'Email', 'Print', 'Clear']
buttonsButtonObjects = []

cosmeticsFrameTitle = 'Cosmetics'
groceryFrameTitle = 'Grocery'
coldDrinksFrameTitle = 'Cool Drinks'
billFrameTitle = 'Bill'
rupeeText = ' Rs. '
minusSymbol = ' - '
percentageSymbol = ' %'
zeroRupeesText = '0 Rs. '
# Cosmetics List
cosmeticsPriceList = [70, 100, 100, 190, 200, 40]
cosmeticsNamesList = ['Shampoo', 'Blush', 'Primer', 'Bronzer', 'Hair Gel', 'Powder']
cosmeticsTitlesList = [f"{name}{minusSymbol}{price}{rupeeText}" for name, price in zip(cosmeticsNamesList, cosmeticsPriceList)]
cosmeticsLabelList = []
cosmeticsEntryList = []

# Groceries List
groceryPriceList = [40, 110, 180, 80, 50, 45]
groceryNamesList = ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea']
groceryTitlesList = [f"{name}{minusSymbol}{price}{rupeeText}" for name, price in zip(groceryNamesList, groceryPriceList)]
groceryLabelList = []
groceryEntryList = []

# Cool Drinks List
coolDrinksPriceList = [20, 30, 35, 25, 10, 15]
coolDrinksNamesList = ['Maaza', 'Pepsi', 'Sprite', 'Frooti', 'Mirinda', 'Pulpy']
coolDrinksTitlesList = [f"{name}{minusSymbol}{price}{rupeeText}" for name, price in zip(coolDrinksNamesList, coolDrinksPriceList)]
coolDrinksLabelList = []
coolDrinksEntryList = []

# Tax percentages
cosmeticTaxPercentage = 0.12
groceryTaxPercentage = 0.05
coldDrinksTaxPercentage = 0.08

billFrameHeight = 14.2
billFrameWidth = 55
billMenuFrameTitle = 'Bill Menu'
# Bill Menu List
billMenuTitlesList = ['Cosmetic Price', 'Grocery Price', 'Cool Drinks Price', 'Cosmetic Tax', 'Grocery Tax',
                      'Cool Drinks Tax', 'Total Amount ']
billMenuLabelList = []
billMenuEntryList = []

errorText = 'Error'
successText = 'Success'
customerNameEmptyMessage = 'Customer Name Required'
customerMobileEmptyMessage = 'Customer Mobile Number Required'
customerMobileSizeNot10Message = 'Customer Mobile Number Should be 10 digits'
customerMobileErrorMessage = 'Customer Mobile Number Should be digits only'
productsEmptyMessage = 'No Products are Selected'
productQuantityNotInDigit = ' Quantity should be non negative digits'
confirmText = 'Confirm'
saveBillYesOrNo = 'Do You want to Save the Bill?'
billSavingConfirmation = ' Bill Saved successfully'
searchFieldEmptyMessage = 'Please Enter a Bill Number'
searchBillNotFoundMessage = ' is InValid'
printValidation = 'No Bill Content Found'
printCommandText = 'print'
billNumberTitle = 'Bill Number'
billNumber = 1
billPath = 'bills/'
billSavingExtension = '.txt'
totalNotDone = 'Please Press Total First'
welComeMessage = '---------------WelCome to Super Market-----------------\n'
starLine = '\n*******************************************************\n'
columnNamesInBill = 'Product\t\tPrice\tQuantity\tTotal'
# Email Sending Related
emailSendingLabelTitle = 'SENDER'
senderEmailIdText = "Sender's EmailId"
senderEmailKeyText = "Sender's Email Key"
receiverEmailIdText = "Receiver's EmailId"
emailReceiverLabelTitle = 'RECEIVER'
emailIdEntryWidth = 23
emailLabelPadx = 10
emailLabelPady = 8
messageText = 'Message'
sendButtonText = 'SEND'
senderEmailIdTextEmptyMessage = "Sender's EmailId is empty"
senderEmailKeyTextEmptyMessage = "Sender's Password is empty"
receiverEmailIdTextEmptyMessage = "Receiver's EmailId is empty"
emailSubject = headingLabelTitle + ' Bill Sending \n'
emailContentEmptyMessage = 'Email Content is Empty'
mailSentSuccessMessage = 'Bill sent Successfully to Email '
somethingWentWrongMessage = 'Something went Wrong Try again'
emailSmtp = 'smtp.gmail.com'
emailSmtpPort = 587
senderEmailId = 'poloju.pranathi27@gmail.com'
senderEmailKey = 'ideiykwqeykxhzaj'
searchBillStatus = False


def deleteAllBillLevelFields():
    for entry in billMenuEntryList:
        entry.delete(0, END)


def doCosmeticTotal():
    cosmeticTotal = 0
    for index, entry in enumerate(cosmeticsEntryList):
        quantity = entry.get()
        try:
            price = cosmeticsPriceList[index] * int(quantity)
            cosmeticTotal += price
        except:
            if quantity:
                messagebox.showerror(errorText, cosmeticsNamesList[index] + productQuantityNotInDigit)
    cosmeticSum = 0.0
    if cosmeticTotal > 0:
        billMenuEntryList[0].insert(0, str(cosmeticTotal) + rupeeText)
        cosmeticTax = cosmeticTotal * cosmeticTaxPercentage
        cosmeticTax = format(cosmeticTax, ".2f")
        billMenuEntryList[3].insert(0, str(cosmeticTax) + rupeeText)
        cosmeticSum = math.ceil(cosmeticTotal + float(cosmeticTax))
    return cosmeticSum


def doGroceryTotal():
    groceryTotal = 0
    for index, entry in enumerate(groceryEntryList):
        quantity = entry.get()
        try:
            price = groceryPriceList[index] * int(quantity)
            groceryTotal += price
        except:
            if quantity:
                messagebox.showerror(errorText, groceryNamesList[index] + productQuantityNotInDigit)
    grocerySum = 0.0
    if groceryTotal > 0:
        billMenuEntryList[1].insert(0, str(groceryTotal) + rupeeText)
        groceryTax = groceryTotal * groceryTaxPercentage
        groceryTax = format(groceryTax, ".2f")
        billMenuEntryList[4].insert(0, str(groceryTax) + rupeeText)
        grocerySum = math.ceil(groceryTotal + float(groceryTax))
    return grocerySum


def doColdDrinksTotal():
    coldDrinksTotal = 0
    for index, entry in enumerate(coolDrinksEntryList):
        quantity = entry.get()
        try:
            price = coolDrinksPriceList[index] * int(quantity)
            coldDrinksTotal += price
        except:
            if quantity:
                messagebox.showerror(errorText, coolDrinksNamesList[index] + productQuantityNotInDigit)
    coldDrinksSum = 0.0
    if coldDrinksTotal > 0:
        billMenuEntryList[2].insert(0, str(coldDrinksTotal) + rupeeText)
        coldDrinksTax = coldDrinksTotal * coldDrinksTaxPercentage
        coldDrinksTax = format(coldDrinksTax, ".2f")
        billMenuEntryList[5].insert(0, str(coldDrinksTax) + rupeeText)
        coldDrinksSum = math.ceil(coldDrinksTotal + float(coldDrinksTax))
    return coldDrinksSum


def total():
    textarea.delete(1.0, END)
    global productsSelected
    productsSelected = False
    deleteAllBillLevelFields()
    cosmeticTotal = doCosmeticTotal()
    groceryTotal = doGroceryTotal()
    coldDrinksTotal = doColdDrinksTotal()
    total = cosmeticTotal + groceryTotal + coldDrinksTotal
    global globalTotal
    globalTotal = 0
    if total > 0:
        billMenuEntryList[6].insert(0, str(total) + rupeeText)
        productsSelected = True
        globalTotal = total
    else:
        productsSelected = False
        messagebox.showerror(errorText, productsEmptyMessage)


if not os.path.exists(billPath):
    os.mkdir(billPath)


def saveBill():
    global billNumber
    confirmation = messagebox.askyesno(confirmText, saveBillYesOrNo)
    if confirmation:
        billContent = textarea.get(1.0, END)
        with open(billPath + str(billNumber) + billSavingExtension, 'w') as f:
            f.write(billContent)
        messagebox.showinfo(successText, billSavingConfirmation)
        billNumber += 1


def printBill():
    billContent = textarea.get(1.0, END)
    if billContent:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tempFile:
            tempFile.write(billContent.encode())
            tempFile.close()
            os.startfile(tempFile.name, printCommandText)
    else:
        messagebox.showerror(errorText, printValidation)


def sendEmail():
    senderEmailId = senderEmailIdEntry.get()
    senderEmailKey = senderEmailKeyEntry.get()
    receiverEmailId = receiverEmailIdEntry.get()
    emailContent = textarea.get(1.0, END)

    if not senderEmailId:
        messagebox.showerror(errorText, senderEmailIdTextEmptyMessage)
        return

    if not senderEmailKey:
        messagebox.showerror(errorText, senderEmailKeyTextEmptyMessage)
        return

    if not receiverEmailId:
        messagebox.showerror(errorText, receiverEmailIdTextEmptyMessage)
        return

    if not emailContent.strip():
        messagebox.showerror(errorText, emailContentEmptyMessage)
        return

    try:
        with smtplib.SMTP(emailSmtp, emailSmtpPort) as server:
            server.starttls()
            server.login(senderEmailId, senderEmailKey)
            message = f"Subject: {emailSubject}\n\n{emailContent}"
            server.sendmail(senderEmailId, receiverEmailId, message)
            messagebox.showinfo(successText, mailSentSuccessMessage + receiverEmailId)
    except:
        messagebox.showerror(errorText, somethingWentWrongMessage)


def searchBill():
    global searchBillStatus
    billNumber = searchFieldEntry.get()
    billFilePath = billPath + str(billNumber) + billSavingExtension
    if os.path.exists(billFilePath):
        with open(billFilePath, 'r') as file:
            billContent = file.read()
            textarea.delete(1.0, END)
            textarea.insert(1.0, billContent)
            searchBillStatus = True
    else:
        messagebox.showerror(errorText, str(billNumber) + searchBillNotFoundMessage)
        searchBillStatus = False


def clear():
    global globalTotal
    globalTotal = 0
    for entry in customerDetailsEntryList:
        entry.delete(0, END)
    for entry in cosmeticsEntryList:
        entry.delete(0, END)
    for entry in groceryEntryList:
        entry.delete(0, END)
    for entry in coolDrinksEntryList:
        entry.delete(0, END)
    deleteAllBillLevelFields()
    textarea.delete(1.0, END)
    searchFieldEntry.delete(0, END)
    global searchBillStatus
    searchBillStatus = False


root = Tk()
root.title(title)
root.geometry(size)
root.iconbitmap(iconFileName)
root.config(bg=backgroundColor)

headingLabel = Label(root, text=headingLabelTitle, font=(fontStyle, headerFontSize, boldFont), bg=backgroundColor, fg=fontColor)
headingLabel.pack()

# Customer Details Frame
customerDetailsFrame = LabelFrame(root, text=customerDetailsFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
customerDetailsFrame.place(x=5, y=70, width=600, height=130)

for i, title in enumerate(customerDetailsTitlesList):
    Label(customerDetailsFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=i, column=0, padx=10, pady=5)
    entry = Entry(customerDetailsFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=entryWidth)
    entry.grid(row=i, column=1, padx=10, pady=5)
    customerDetailsEntryList.append(entry)

searchButton = Button(customerDetailsFrame, text=searchButtonTitle, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=fieldBorderSize, command=searchBill)
searchButton.grid(row=0, column=2, padx=10, pady=5)

searchFieldEntry = Entry(customerDetailsFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=entryWidth)
searchFieldEntry.grid(row=0, column=3, padx=10, pady=5)

# Cosmetics Frame
cosmeticsFrame = LabelFrame(root, text=cosmeticsFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
cosmeticsFrame.place(x=5, y=210, width=600, height=290)

for i, title in enumerate(cosmeticsTitlesList):
    Label(cosmeticsFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=i, column=0, padx=10, pady=5)
    entry = Entry(cosmeticsFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=entryWidth)
    entry.grid(row=i, column=1, padx=10, pady=5)
    cosmeticsEntryList.append(entry)

# Grocery Frame
groceryFrame = LabelFrame(root, text=groceryFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
groceryFrame.place(x=620, y=210, width=600, height=290)

for i, title in enumerate(groceryTitlesList):
    Label(groceryFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=i, column=0, padx=10, pady=5)
    entry = Entry(groceryFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=entryWidth)
    entry.grid(row=i, column=1, padx=10, pady=5)
    groceryEntryList.append(entry)

# Cool Drinks Frame
coolDrinksFrame = LabelFrame(root, text=coldDrinksFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
coolDrinksFrame.place(x=620, y=500, width=600, height=290)

for i, title in enumerate(coolDrinksTitlesList):
    Label(coolDrinksFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=i, column=0, padx=10, pady=5)
    entry = Entry(coolDrinksFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=entryWidth)
    entry.grid(row=i, column=1, padx=10, pady=5)
    coolDrinksEntryList.append(entry)

# Bill Frame
billFrame = LabelFrame(root, text=billFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
billFrame.place(x=5, y=500, width=600, height=billFrameHeight*10)

textarea = Text(billFrame, font=(fontStyle, 12), bg='light yellow', height=20, width=billFrameWidth)
textarea.pack()

# Bill Menu Frame
billMenuFrame = LabelFrame(root, text=billMenuFrameTitle, font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
billMenuFrame.place(x=5, y=700, width=1215, height=60)

for i, title in enumerate(billMenuTitlesList):
    Label(billMenuFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=0, column=i*2, padx=10, pady=5)
    entry = Entry(billMenuFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=totalEntryWidth)
    entry.grid(row=0, column=i*2 + 1, padx=10, pady=5)
    billMenuEntryList.append(entry)

# Buttons
buttonsFrame = Frame(root, bg=backgroundColor)
buttonsFrame.place(x=5, y=780, width=1215, height=60)

buttonCommands = [total, saveBill, sendEmail, printBill, clear]
for i, title in enumerate(buttonsTitlesList):
    button = Button(buttonsFrame, text=title, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=fieldBorderSize, command=buttonCommands[i])
    button.pack(side=LEFT, padx=5)

# Email Frame
emailFrame = LabelFrame(root, text='Email Sender', font=(fontStyle, fontSize, boldFont), bg=backgroundColor, fg=fontColor, bd=labelBorderSize)
emailFrame.place(x=5, y=850, width=1215, height=150)

Label(emailFrame, text=senderEmailIdText, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=0, column=0, padx=emailLabelPadx, pady=emailLabelPady)
senderEmailIdEntry = Entry(emailFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=emailIdEntryWidth)
senderEmailIdEntry.grid(row=0, column=1, padx=emailLabelPadx, pady=emailLabelPady)

Label(emailFrame, text=senderEmailKeyText, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=1, column=0, padx=emailLabelPadx, pady=emailLabelPady)
senderEmailKeyEntry = Entry(emailFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=emailIdEntryWidth, show='*')
senderEmailKeyEntry.grid(row=1, column=1, padx=emailLabelPadx, pady=emailLabelPady)

Label(emailFrame, text=receiverEmailIdText, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=labelBorderSize).grid(row=2, column=0, padx=emailLabelPadx, pady=emailLabelPady)
receiverEmailIdEntry = Entry(emailFrame, font=(fontStyle, fontSize), bg=fieldFontColor, bd=fieldBorderSize, width=emailIdEntryWidth)
receiverEmailIdEntry.grid(row=2, column=1, padx=emailLabelPadx, pady=emailLabelPady)

Button(emailFrame, text=sendButtonText, font=(fontStyle, fontSize), bg=backgroundColor, fg=fontColor, bd=fieldBorderSize, command=sendEmail).grid(row=3, column=0, columnspan=2, padx=emailLabelPadx, pady=emailLabelPady)

root.mainloop()
