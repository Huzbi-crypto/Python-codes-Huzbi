for _ in range(16):

    # Let the user input the greeting
    greetings = input("Greeting: ")


    # Check to see if the greeting input is Hello, give 0$ if so
    if greetings == ("Hello") or greetings == ("hello") or greetings == ("Hello there") or greetings == ("hello there") or greetings == ("Hello there, Huzbi") or greetings == ("hello there, Huzbi") :
        print("0$")

    # Check to see if the greeting starts with 'h' but isn't 'hello' and give 20$    
    elif greetings == ("Hey") or greetings == ("Hi") or greetings == ("How's it going") or greetings == ("hey") or greetings == ("hi") or greetings == ("how's it going") or greetings == ("how are ya") or greetings == ("How are ya") or greetings == ("How are you") or greetings == ("how are you") or greetings == ("How do you do") or greetings == ("how do you do"):
        print ("20$")

    # If the greeting is something else or blank then give 100$    
    else:
        print ("100$")



