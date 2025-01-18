def result(num):
    if num >= 90:
        return "Topper"
    elif num >= 80:
        return "Great"

    elif num >= 70:
        return "Good"

    elif num >= 60:
        return "fair"

    elif num >= 50:
         return "Needs Improvement"
    else:
         return "Fail"
number=int(input("Enter Your Marks = ")) 

print(result(number))