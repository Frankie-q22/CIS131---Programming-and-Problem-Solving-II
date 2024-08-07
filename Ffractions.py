#Frankie Quintero
#CIS131
#3/8/2023

from fractions import Fraction 
Numerator1 = int(input("Enter Numerator for Fraction 1: "))
Denominator1 = int(input("Enter Denominator for Fraction 1: "))

while Numerator1 == 0:
    print('This fraction becomes a ZERO, try another fraction')
    Numerator1 =int(input("Enter Numerator for Fraction 1: "))
    Denominator1 = int(input("Enter Denominator for Fraction 1: "))
while Denominator1 == 0:
    print('This fraction is Undefined, try another fraction') 
    Numerator1 = int(input("Enter Numerator for Fraction 1: "))
    Denominator1 = int(input("Enter Denominator for Fraction 1: "))

else:
    
    Fraction1 = Fraction(Numerator1,Denominator1)
    Dec1 = float(Fraction1)
    print("Your second fraction is: "+"\n", Fraction1 ,"in Fraction form" +"\n"  , Dec1, "In Decimal Form")

Numerator2 = int(input("Enter Numerator for Fraction 2: "))
Denominator2 = int(input("Enter Denominator for Fraction 2: "))

while Numerator2 == 0:
    print('This fraction becomes a ZERO, try another fraction')
    Numerator2 =int(input("Enter Numerator for Fraction 2: "))
    Denominator2 = int(input("Enter Denominator for Fraction 2: "))
while Denominator2 == 0:
    print('This fraction is Undefined, try another fraction') 
    Numerator2 = int(input("Enter Denominator for Fraction 2: "))
    Denominator2 = int(input("Enter Denominator for Fraction 2: "))

else:
    
    Fraction2 = Fraction(Numerator2,Denominator2)
    Dec2 = float(Fraction2)
    
    print("Your second fraction is: "+"\n", Fraction2 ,"in Fraction form" +"\n"  , Dec2, "In Decimal Form")

FractionAdd = Fraction1 + Fraction2
FractionAddDec = float(Fraction1) + float(Fraction2)
FractionSub = Fraction1 - Fraction2
FractionSubDec = float(Fraction1) - float(Fraction2)
FractionMult = Fraction1 * Fraction2
FractionMultDec = float(Fraction1) * float(Fraction2)
FractionDiv = Fraction1/Fraction2
FractionDivDec = float(Fraction1)/float(Fraction2)
print("\n")
print("Math Functions:")
print("\n")
print("Addition" + "\n" + "==============================")
print(Fraction1, "+" ,Fraction2, "=" , FractionAdd,"\n" +  "   or "+"\n"   + str(Dec1), "+", str(Dec2), "=",FractionAddDec)
print("\n") #=============================================================================================================
print("Subtraction" + "\n" + "==============================")
print(Fraction1, "-" ,Fraction2, "=" , FractionSub,"\n" +  "   or "+"\n"   + str(Dec1), "-", str(Dec2), "=",FractionSubDec)
print("\n")#===============================================================================================================
print("Multiplication" + "\n" + "==============================")
print(Fraction1, "*" ,Fraction2, "=" , FractionMult,"\n" +  "   or "+"\n"   + str(Dec1), "*", str(Dec2), "=",FractionMultDec)
print("\n")#================================================================================================================
print("Division" + "\n" + "==============================")
print(Fraction1, "/" ,Fraction2, "=" , FractionDiv,"\n" +  "   or "+"\n"   + str(Dec1), "/", str(Dec2), "=",FractionDivDec)
print("\n")
print("================================================================================================================================================================")


print("\nThe Complex Numbers: ", complex(4, 7), "and", complex(3, 4), "\n------------------------------------------------------")
ComNum1 = complex(4, 7)
ComNum2= complex(3, 4)

    
AddComNum = ComNum1 + ComNum2

    
SubComNum = ComNum1 - ComNum2


print("The sum of the 2 complex numbers is : ", AddComNum)
print("\n")   
print("The real number of the new complex number is: ", AddComNum.real)
print("\n")
print("The imaginary number of the new complex number is: ", AddComNum.imag)
print("\n")
print("The Difference of complex numbers is : ", SubComNum)
print("\n")
print("\n")
