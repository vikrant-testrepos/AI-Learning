success = False
for number in range(3):
    print("Attempt")
    if success:
        print("Attempt successful")
        break
else:
    print("Failed 3 attempts")