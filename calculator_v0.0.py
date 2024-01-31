#Calculator application code starts
##-------------------------------##
#Calculator performs a mathematical operation of two input numbers the user is giving
#User has to provide 3 inputs -two operands and an operator
declare x,y,operator,Result;
x=0;y=0;operator='';
print("Enter two numbers");
input(x);
input(y);
print("Enter the operator")
input(operator);
#Section 1.0 IMPLEMENTED ON DEVL branch
 #Switch logic to call the function
 switch(operator)
 {'+': call add(x,y);
  '-': call subtract(x,y);
  '*': call multiply(x,y);
  '/': call division(x,y);
         }
 #Switch logic ends here
#Section 1.1 
 #Addition code starts below
 #Br:Feature-Addition
 #Auth:Anish
 function add(x,y,operator)
 {sum=x+y;
  Result=sum;
  return Result
  }
 #Addition code ends above

#Section 1.2
 #Subtraction code starts below
 #Br:feature-subtract
 #Author:Narmad
 function subtract(x,y)
 {difference=x-y;
  difference=Result;
  return Result;  
 }
 #Subtraction code ends above
#Section 1.3 
 #Multiplication code starts below
 #Multiplication code ends above
#Section 1.4 
 #Division code starts below
 #Division code ends above
 
#Calculator application code ends
##-------------------------------##
