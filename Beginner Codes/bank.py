for _ in range(16):

    # Let the user input the greeting
    greetings = input("Greeting: ").lower()


    # Check to see if the greeting input is Hello, give 0$ if so
    if greetings in ("hello"):
        print("0$")

    # Check to see if the greeting starts with 'h' but isn't 'hello' and give 20$    
    elif greetings.startswith("h"):
        print ("20$")

    # If the greeting is something else or blank then give 100$    
    else:
        print ("100$")



