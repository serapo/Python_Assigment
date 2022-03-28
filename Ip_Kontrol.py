number="367.123.123.345"
sayı=number.split(".")
#print (sayı[0],sayı[1])
  # print(i)         

for i in range(1,255): 
  if len(sayı[0])==3 and len(sayı[1])==3 and len(sayı[2])==3 and len(sayı[3])==3: 
          if sayı[0].isnumeric()==False or sayı[1].isnumeric()==False:
            print("Digit is not number {} {}".format(sayı[0],sayı[1]))
            break
          elif sayı[0].isnumeric()==False:
            print("First digit is not number".format(sayı[0]))
            break
          elif sayı[1].isnumeric()==False:
            print("Second digit is not number".format(sayı[0]))
            break
          elif i==int(sayı[0]) or i==int(sayı[1]) :
            print("IP address is available {}".format(number))
            break
  else:
      print("Your entering len is not available")
      break 
