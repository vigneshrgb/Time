seconds = int(input("Enter seconds: "))
ss = seconds % 60
mm = (seconds // 60) % 60
hr = (seconds // 3600) % 24
day = (seconds // 86400) #Technically incorrect - Leap seconds need to be added
print("Day: " + str(day) + "   " + "HR:" + str(hr) + "   " + "MM:" + str(mm) + "   " + "SS:" + str(ss))
