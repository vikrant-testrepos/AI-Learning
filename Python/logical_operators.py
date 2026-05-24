age = 22
citizenship = True
National = False

if age >= 18 and citizenship and National:
    print("Eligible for voting")
elif age <=18 and not citizenship and National:
    print("Minor and not eligible to vote")
elif age >= 18 or citizenship and not National:
    print("Foreigner!,not eligible for voting")
print("Done")