# Inventory Management System in Python (Electronic Store)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4118113.svg)](https://doi.org/10.5281/zenodo.4118113)

***

[back to repo](https://github.com/indraoli429/Billing-System-In-Python)

***

## (Full Documentation)
It is tied in with composing a program in python of an electronic store that offers electronic machines like phone, laptop and HDD etc.

## Purpose
The primary motivation behind composing this coursework is to build up a program in python, utilizing loop concept as well as file read and write for the given scenario of an electronic store. It ought to likewise module algorithm, pseudocode, flowchart and data structure of the program.
## Problem statement
The issue offered was to build up an application which read the text document and show the data accessible. After that the program should to create a invoice for a customer or consumer, with each purchase of the given item. Likewise, after each purchase of some products the stock should be refreshed in same text file.
## Aim and objectives
The fundamental focus of this coursework is to take in the idea of programming in python and can compose a program for the given command. Similarly, another target of this coursework is learning the concept of file read and write in python programming language and know almost data structure in python. To achieve this aim will be made to finish all the work in the given time frame. Additionally, more research and study relating with this errand will be made.
## Purposed approach
To solve all the given work in this coursework, certain methodologies will be made which are follows.
1. At the primary, study and research will be done to take care of the issue of building up a program and its related point. 
2.  Then a program will be made in python which will coordinate the given instruction. 
3. Data structures required for composing the program will be chosen according to requirement of the given instruction of program.
4. An algorithm of the program will be built where everything the program wills be considered. 
5. A flowchart will be drawn to indicate how a code execute and work in the program. It is easy to understand how our program work in the real time.
6. Pseudocode will be made to demonstrate the normal understanding way of the program. It is look like a program but actual it is concept of program it does not execute. Pseudocode is just English language but structure is program. 
7. Finally, testing will be improved the situation the composed program so error and bugs will be settled and it can convey the right wanted outcome.
## Target audience
This task will be useful for understudies, programmer, software engineers, analysts and particularly for those students who look for premium and need to learn python programming dialect. As well as it is useful for those commercials propose which is required billing system store for individual customer.
## Hardware and software requirements
Adjacent to PC, no an equipment is required however in programming we utilize python IDLE which ought to be installed in computer.
## Scope of the project 
This undertaking outlines the thoughts and techniques for composing programs in pythons utilizing loop concept. It additionally comprises algorithm, pseudocode, flowchart and data structure of the program. therefore, this undertaking will be extremely useful for every one of those understudies, programmer, software engineers and python learner students to discover how the code execute and work in the program. Similarly, It will instruct the strategy of different data structure which has been utilized as a part of the program. At last, as the program is composed with great clarification in each progression so it will help every one of those students who discover trouble in python.

## Features of the project
The features of this program as follows;
1. To build a program which work in loop statement and show accessible items which are stored in text file. The program should wait for user to enter purchase details of interest. Program should not close or stop until and unless the user chooses to do as such.
2. Program had user interacts features which is request every question with customer and react that answer provide by customer.
3. Program had exception handling feature which is used when unexpected entered from user. Like, program expect to the integer value from customer but customer entered a string value then program request for integer value.
4.Interconnect the different module in main module for easy to run the full program. Like, read, write, and purchase module are connect with main module.
5. Program can read text file and overwrite or write new text file. In this program, I used products.txt file for store a data and read and overwrite on it.
6. Similarly, program create a unique invoice in text file format and its naming from current device date and time.

## Discussion and analysis
This program was developed by using python official IDLE as name ‘Python IDLE’. In the overall program, I create a four-different module ‘read’, ‘write’, ‘purchase’ are connected to ‘main module’. All module has own work and finally main module call value and instruction from remaining three modules. In the processing of the program I used text file for read data and work on it.
After the coding part of the program we construct the flowchart for easier to understand how the program works. Flowchart is the graphical representation of the program, I construct the flowchart using Microsoft Visio 2010, alternatively I used the online tool which link is '[draw.io](www.draw.io "Draw.io Homepage")'

## Stepwise algorithm
- Step 1:	 Start 
- Step 2:	 products.txt file from given folder.
- Step 3: 	txt file is displayed in the screen with products available.
- Step 4:	Inputs customers name.
- Step 5: 	Inputs products name.
- Step 6: 	If product name is correct then go to next step or else remain in same step until valid name is provided.
- Step 7: 	Input quantity of the product.
- Step 8: 	If the input number of quantity is available then go to next step or else display Sorry!! a_name !, product is out of stock.
We will add stock of product later. 
Lets hope, you will get this product after next shopping
- Step 9: 	Ask customer do you want buy more products?(Y/N) If they select Y, go back to step 6, If they select no, then it won’t go to any steps.
- Step10: 	Price of the product with total amount is displayed.
- Step 11: 	The percentage to be discounted is asked.
- Step 12: 	Total price after the discount is calculated and display updated amount.
- Step 13:	Invoice is printed with customer name, date and time purchase. Products details, Grand total and at last Thank You customer for your shopping. See you again!
- Step 14: 	If more customers are there to purchase item ‘Y’ should be clicked and go to step or else end.
- Step 15:	 End.

## Flowchart
![Flowchart](https://github.com/khillsman3/Electronic_Store_Python_Program/raw/master/Flowchart "Flowchart")

## Pseudocode for write.py
```python
Algorithm write(List,Dictionary):
   L is set to List # list was assigned to 'L' variable
    d is set to Dictionary 
    for keys in d.keys():
        If keys is equals to"PHONE" then
            L[0][2] is set to str(int(L[0][2])-d['PHONE']) 
        else if  keys is equals to"LAPTOP" then
            L[1][2] is set to str(int(L[1][2])-d['LAPTOP']) 
        else:
            L[2][2] is set to str(int(L[2][2])-d['HDD'
    output(L)
        
    files is set to open("products.txt","w")  
    for each in L:
        write on files(str(",".join(each)))
        write on files ("\n")        
    write on files () 
```
## gorithm read():
```python
    file is set to open("products.txt","r") 
    lines is set to file.readlines() 
    L is set to [] 
    for line in lines:
        L.append(line.replace("\n","").split(","))
    file.close() 
    for i in range(len(L)):
        output(L[i][0],"\t PRICE: ",L[i][1],"\t QUANTITY: ",L[i][2]) #  the availability, price and quantity of the product will output 
    return L 
```
## Pseudocode for Main.py
```python
import  from read
import from purchase
import from write
again is set to "Y"
while again in upper case is equals to"Y":
    a is set to read.readfile()
    b is set to purchase.purchase(a)
    	write.over_write(a,b)
    	again is set to input(" ")
output("")
```

## Pseudocode for purchase.py
```python
algorithm purchase(List): 
    L is set to List 
    name is set to input proper message 
    q is set to create dictionary
    flag is set to "Y"
    while answer in upper case is equals to "Y":  
        product is set to input  proper message
        product_name is set to product_type in upper case
        
        If product_name is equals to L[0][0] in upper case or product_type1 is equals to      L[1][0] in upper case or product_name is equals to L[2][0] in upper case: 
            p is set to True
            while p is equals to True:
                try:
                    p_quantity is set to int(input("How many "+product+" do you want to buy: "))
                    p is set to False
                except:
                    output ("Error!!!,Please enter correct integer value!! ") 
            If product_name is equals to L[0][0] in upper case and p_quantity is less than or equals to int(L[0][2]):       
                q[product_name] is set to p_quantity   
            else If  product_name is equals to L[1][0] in upper case and p_quantity is less than or equals to int(L[1][2]):
                    q[product_name] is set to p_quantity
            else If  product_name is equals to L[2][0] in upper case and p_quantity is less than or equals to int(L[2][2]):
                    q[product_name] is set to p_quantity
            else:
                output ("\nSorry!! "+a_name+"!, "+product+" is out of stock.\nWe will add stock of "+product+" later. \nLets hope, you will get this product after next shopping.\n.")    
             end If   
            answer is set to (input("a_name+" do you want buy more products?(Y/N)" ))
        else:
            output ("sorry!! "+product+" is not available in our store..")
	output ("\nChoose from following products please!")
	output ("PRODUCT\t\tPRICE\t\tQUANTITY")
            for i in range(len(L)):
           end while
                output ("PRODUCT AVAILABLE: ",L[i][0],"\t PRICE: ",L[i][1],"\t QUANTITY: ",L[i][2]) 
     
        output  (\nYou Choosed Items and it's Quantity respectively:\n")       
    output  (q)
    
    #for invoice
    f_amount is set to 0
    for keys in q.keys():
        If keys is equals to L[0][0] in upper case: 
            p_price is set to int(L[0][1])
            p_num is set to int(q[keys])
            p_amount is set to (p_price *number1)
            f_amount+ is set to (p_price *number1)
            output ("\nTotal cost for phone: ",p_amount) 
        else If  keys is equals to L[1][0] in upper case: 
            l_price  is set to int(L[1][1])
            l_num is set to int(q[keys])
            l_amount is set to (l_price *number2)
            f_amount + is set to (l_price *number2)
            output ("Total cost for laptop: ",l_amount)
        else:                        .
            h_price is set to int(L[2][1])
            h_num is set to int(q[keys])
            h_amount is set to (h_price *number3)
            f_amount + is set to (h_price *number3)
            output ("\nYour discountable total amount is: ", f_amount)
          end If
    disc is discount(float(input("Please enter your expected discount (%): ")))
   dis is inatilized with 0.0
if f_amount is greater than 5000 and less than 10000
	put the value of discount disc 
	if discount is less than 5.0
		dis is calculate (discount*f_amount)/100
		total is float(f_amount-dis)	
    		output ("You got your expected "+str(disc)+"% discount and amount is: ",dis)     
	else discount is greater than 5.0  
		discount is similar to 5.0 
		dis is calculate (discount*f_amount)/100
		total is float(f_amount-dis)	
    		output ("You did not got your expected "+str(disc)+"% discount\nBecause, your totel purchase is not meet the minimum criteria for "+str(disc)+"% discount.")
		output("You got basic 5% discount and discounted amount is:",dis)
    elif (f_amount>=10000):     

if f_amount is greater 10000
	put the value of discount disc 
	if discount is less than 10.0
		dis is calculate (discount*f_amount)/100
		total is float(f_amount-dis)	
    		output ("You got your expected "+str(disc)+"% discount and amount is: ",dis)     
	else discount is greater than 10.0  
		discount is similar to 10.0 
		dis is calculate (discount*f_amount)/100
		total is float(f_amount-dis)	
    		output ("You did not got your expected "+str(disc)+"% discount\nBecause, your totel purchase is not meet the minimum criteria for "+str(disc)+"% discount.")
		output("You got basic 10% discount and discounted amount is:",dis)
else 
discount is 0.0
 total is float(f_amount)
import date and time from current device
open file (invoice+" ("+a_name+").txt","w")  #unique file name open it on writing mode
write in file for invoice
    write on a file ("\nELECTRONIC STORE\t\t\t\tINVOICE")
    write on a file ("\n\nInvoice: "+invoice+"\t\tDate: "+d+"\n\t\t\t\t\tTime: "+e+"")
    write on a file ("\nName of Customer: "+str(a_name)+"")
    write on a file ("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")                               
    for keys in q.keys():           #In this loop, write in a file only those product which is purchase by user.
        if key is equal to "PHONE":
            write on a file (str("\n"+str(keys)+" \t\t "+str(q['PHONE'])+" \t\t "+str(L[0][1])+" \t\t "+str(p_amount)))
        elif keys is equal to "LAPTOP":
            write on a file (str("\n"+str(keys)+" \t\t "+str(q['LAPTOP'])+" \t\t "+str(L[1][1])+" \t\t "+str(l_amount)))
        else: 
            write on a file (str("\n"+str(keys)+" \t\t "+str(q['HDD'])+" \t\t "+str(L[2][1])+" \t\t "+str(h_amount)))
    write on a file ("\n\t\t\tYour discountable amount: "+str(f_amount))
    write on a file ("\n\t\t   Your "+str(discount)+"% discounted amount is: "+str(dis))
    write on a file ("\n\t\t\t Your payable amount is: "+str(total))
    write on a file("\n\n\tThank You "+a_name+" for your shopping.\n\t\tSee you again!")
    closed the file
    generate bill using unique code, customer’s name,total and discount , 
    write bill in newly generated file
output  invoice
```
## Data structures
A data structure is a way of organizing and storing data in a program, and it can be modified and accessed easily later. Basically, data structures have two types one is primitive data types like, integer, float, string. And another is collection data types like, list, tuples, dictionary etc. But this program the following data structure which has been used; list, dictionaries, string, integer and float.
### Primitive data types
In this program, I used some primitive data types, which are as follows with description.
#### Integer: 
Integer represent the whole number and integer is denoted by ‘int’ in program. In this program integers are used for many purpose, like, in the purchase module ask the quantity of product with customer and there except integer value from customer. Similarly, for calculate the quantity stock of product also used integer value.
#### Float: 
Float represent the decimal number and float is denoted by ‘float’ in program. In this program float are used some special calculation like, when customer except some discount percentage from store then there will be calculated in float and final customer payable amount also calculate in float data types. 
#### String: 
String represent or carry the alphabet value and in the program, it is initialized by ‘str’.in this program strings are used mainly file write process because text file is not support integer, float or any data types except string. When creating an invoice or update a stock of store there will need to be convert any data into string.
### Collection data types
In this program, I used some collection data types, which are as follows with description.
#### List: 
List is the mostly used collection data types it is an ordered sequence of items where it consists different data types. List are mutable data types it has modified easily after assign. In this program, I used list in ‘read’ module for storing a data from given text file. And there is another module ‘purchase’ where I used a list for calling the value form ‘read’ module. Similarly, in the ‘write’ module I also used same list for the update stock of store after each purchase.
#### Dictionaries: 
Dictionaries are unordered collection data types where it consists various data types. It has different indexing style like, key and value, where key represent the cross-ponding value. In this program, I used a dictionary in ‘purchase’ module for add every product customer want to buy and display after chosen. In the ‘write’ module for updating a stock of product after each purchase.
## Program
This python program creating an invoice after every purchase an it can update inventory stock after each purchase. In the time when I was doing this program, many problems were created but after continuity of research and with help of our module leader and instructor, that problems were done as a solution.
This is a modular programming method. This programming is done by creating a different module into functions and files. This helps to understand the program and easy to accessible. For this program, I divided four different module which are as follows;
- read.py: in this read module, read_file function works on file as read mode and it creates an empty list. In that empty list, stored data from text file which have some data of store.
- purchase.py: In this module, it brings a list from read module. And ask the question for what product do want to purchase customer. Similarly, ask for quantity for that product. When user entered value are matched in the list and execute the calculation for choose product. After than ask the discount percentage, when these all operation done then purchase module act on invoice. Finally, it creates a unique invoice for purchase. 
- write.py: In this module, after each purchase it collect data from purchase and update in stock file(products.txt). for example, customer purchase 10 laptop out of 50 then update stock file will must be remaining 40 laptops only.
- Main.py: This module collects all information and data from remaining three modules and execute from here.

## Testing
Testing is the technique where we check our program for program gives the expected output or not as well as the program has any error or bugs or not. Now it is complete by black box testing method. And following are demonstrate of black box testing.
+ test case not found

## Conclusion
This coursework has helped me to explore more in python programming language. I learnt that python programming is a great degree valuable apparatuses to manufacture and create many projects and programming. The stock administration framework is valuable as it keeps the record of the item in the electronic store and in addition it causes client to screen their buy. 

Similarly, it has helped me to achieve the new level of the imagination and have given me the certainty to grow more projects and to improve my programming abilities and skills as well as to improve my programming understanding level. After a great deal of diligent work and research, at long last calculation and flowchart were made which would give the peruse a basic perception of the program, clear comprehension of the code and how the program is running. After the consummation of the coursework it was important to guarantee that it was bug and mistake free, such a significant number of test were done which affirmed that the projects were prepared to use in the genuine situation and can be refreshed if necessary in future. 

From the overall coursework, it gives me a knowledge about not only python programming language, flowchart and pseudocode also helps to Java programming language as well. This coursework is quite tough then I expect, In the first week of this coursework I feel it is easy to create a program as a requirement. But , this  is hard to finish. Finally, it happens good and program is also done with the help of teachers as well as senior friends.  

Hence indisputably, the coursework has been an amazing help to learn and get the more information about the python programming language. Moreover, it has helped me in additionally creating distinctive different ability and educated numerous things which will help in my profession life in future. This undertaking has still got spaces for the change. At long last, I foresee accomplishing more undertakings in coming future


## Picture Evidence
![Picture Evidence (Testing sample)](https://github.com/khillsman3/Electronic_Store_Python_Program/raw/master/py.JPG "Black Box Testing")

![Picture Evidence (Black Box Testing)](https://github.com/khillsman3/Electronic_Store_Python_Program/raw/master/pyy.JPG "Generated invoice")

****
[back to repo](https://github.com/indraoli429/Billing-System-In-Python)