#write a program to check leap year

year = int(input("enter the num: "))


#divided by 100 means century year (ending with 00)
#century year divided by 400 is leap year
if (year % 400== 0) and (year % 100 == 0):{
   print(f"{year} is a leap year and also century year")
   }


# Not divided by 100 means not  century year
#century year divided by 4 is leap year
elif (year % 4 == 0) and (year % 100!=0):{
    print(f"{year} is  leap year and not century year")
    
}
    
#if not divided by 100 and not  divided by 4 both are not century year or not leap year 
else:{
    print(f"{year} is not leap year")
   

}
 