print("Welcome to loan interest rate calculator\n") #สวัสดีผู้ใช้
print("Notice: Under Thai law, you cannot be charged more than 15% per annum interest!\n") #อธิบายเกี่ยวกับกฎหมายไทย
y = int(input("How many times do you want to process this program? : "))#ถามว่าจะรันโปรแกรมกี่ครั้ง

if y <= 0: #ถ้า y น้อยกว่าหรือเท่ากับ 0
    y = int(input("How many times do you want to process this program? (Don't enter number less than 0): ")) #ให้ถามว่าจะใช้กี่ครั้งใหม่

print("\nFirst, choose what you want to calculate by entering the choice number") #อธิบายผู้ใช้
print("1.Total interest pay on loan\n2.Monthly interest pay on Amortizing loans") #ตัวเลือก

count = 0 #ตั้งตัวแปร count = 0

while count < y: #ให้รันถ้าตัวแปร count น้อยกว่าตัวแปร y
    x = int(input("Enter your choice: ")) #ถามว่าผู้ใช้จะเลือกทำในข้อไหน
    
    def input_choice(value): #ตั้ง function ในการตรวจสอบว่าตัวแปร x เท่ากับ 1หรือ2 ไหม
        if value != 1 and value != 2: #ตรวจสอบว่า value ไม่เท่ากับ 1 หรือ 2 ไหม
            return False #ส่งค่ากลับเป็น false
        else: #อื่นๆ
            return True #ส่งค่ากลับเป็น true
        
    
    if input_choice(x) != False: #ถ้าตัวเลือกของผู้ใช้ไม่เท่ากับ False
        if x == 1: #ถ้าตัวแปร x เท่ากับหนึ่ง
            print("Second, enter your information") #บอกให้ผู้ใช้กรอกข้อมูล
            loan_amount = float(input("Enter principal loan amount: ")) #ถามผู้ใช้เกี่ยวกับยอดหนี้โดยเก็บในตัวแปร loan_amount
            interest_rate = float(input("Enter loan interest rate: ")) #ถามผู้ใช้เกี่ยวกับ interest rate และเก็บในตัวแปล interest_rate
            years_in_term = float(input("Enter number of years in term: ")) #ถามผู้ใช้เกี่
            print("Thrid, Do you want us to show you how to calculate?") #บอกผู้ใช้ขั้นตอนที่สาม
            show_cal = input("Enter y for yes enter other characters for no! :") #ถามผู้ใช้ว่าจะให้บอกวิธิการคำนวณไหมโดยเก็บค่าในตัวแปร show_cal
            
            paid = loan_amount*interest_rate/100*years_in_term #คำนวณแบะเก็บในตัวแปร paid
            
            if show_cal == "y": #ถ้าตัวแปร show_cal มีค่าเท่ากับ y
                print("This is how we calculate your total loan interest pay amount!") #บอกผู้ใช้ว่าคำนวณยังไง
                print("Your principal loan time (Interest rate divide by 100) times Number of years in term") #บอกผู้ใช้ว่าคำนวณยังไง
                print("For you:",loan_amount,"x",interest_rate/100,"x",years_in_term,"=",paid) #บอกผู้ใช้ว่าคำนวณยังไง
                print("In total you need to pay interest at",paid,"Baht") #บอกผู้ใช้ว่าคำนวณยังไง
            else: #อื่นๆ
                print("You need to pay interest at",paid,"Baht") #บอกคำตอบผู้ใช้
                
        if x == 2: ถ้า ตัวแปร y เท่ากับ 2
            print("Second, enter your information") #บอกขั้นตอนที่สองกับผู้ใช้
            interest_rate = float(input("Enter loan interest rate: ")) #ถามผู้ใช้เกี่ยวกับอัตราดอกเบี้ยและเก็บในตัวแปร interest_rate
            numberofpayment = float(input("Enter number of payments that year: ")) #ถามผู้ใช้เกี่ยวกับ number of payments that year และเก็บในตัวแปร numberofpayments
            remain_balance = float(input("Enter remaining balance: ")) #ถามผู้ใช้เกี่ยวกับเงินที่เหลิอจ่ายแบะเก็บในตัวแปร remain_balance
            print("Thrid, Do you want us to show you how to calculate?") #บอกขัเนตอนที่ 3 กับผู้ใช้
            show_cal = input("Enter y for yes enter other characters for no! :") #ถามผู้ใช้ว่าจะให้บอกวิธิการคำนวณไหมโดยเก็บค่าในตัวแปร show_cal

            
            paid = ((interest_rate/100) / numberofpayment)*remain_balance #คำนวณและเก็บตัวแปร paid
            
            if show_cal == "y": #ถ้าตัวแปร show_cal มีค่าเท่ากับ y
                print("This is how we calculate your monthly interest pay on amortizing loans!") #บอกวิธีคำนวณกับผู้ใช้
                print("((Interest rate divide by 100) divide by number of payments that year) time remaining balance") #บอกวิธีคำนวณกับผู้ใช้
                print("For you:",(interest_rate/100)/numberofpayment,"x",remain_balance,"=",paid) #บอกวิธีคำนวณกับผู้ใช้
                print("You need to pay interest at",paid,"Baht per month") #บอกคำตอบผู้ใช้
            else: #อื่นๆ
                print("You need to pay interest at",paid,"Baht per month") #บอกคำตอบผู้ใช้
    
    
            
    else: #อื่นๆ
        print("Please enter correct choice number!") #บอกให้ผู้ใช้ใส่เลจให้ถูก
        
    count = count + 1 #บวกตัวแปร count ไป 1
    

print("\nFor more information check out https://www.bankrate.com/loans/personal-loans/how-to-calculate-loan-interest/ !") #บอกแหล่งข้อมูลเพิ่มเติม

print ("Member : 10 13 24 28") #บอกสมาชิก


