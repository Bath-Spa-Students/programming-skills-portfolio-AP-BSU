# Statement of output using true or false commands then loop
while True:
    try:
        age = int(input("Enter your age or type 'end' to end program: "))
        if age < 3:
            print("The ticket is free.")
        elif 3 <= age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
            
 # Backup output and if user enters a abnormal input will end print lines. NOTE: Requires 'end' input entered again after reset to end program 
    except ValueError:
        if input() == 'end':
            break
