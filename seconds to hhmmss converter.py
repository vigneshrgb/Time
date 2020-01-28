seconds = int(input("Enter seconds: "))
ss = seconds % 60
mm = (seconds // 60) % 60
hr = (seconds // 3600)
print("HR:" + str(hr) + "   " + "MM:" + str(mm) + "   " + "SS:" + str(ss))
