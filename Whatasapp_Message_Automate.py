import pywhatkit as py

number = input("Enter the number you want to send message with country code : ")

message= input("Enter the message you want to send : ")

hours=int(input("Enter the hours in 24 hrs format : "))

min=int(input("Enter the minute : "))

py.sendwhatmsg(number,message,hours,min)
 
