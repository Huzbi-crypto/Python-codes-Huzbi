for _ in range(16):

    # Ask user for the file name with or without extension (depends on them)
    filename = input("File Name: ")


    # Check to see whch extension it has or there isn't any .gif .jpg .jpeg .png .pdf .txt .zip .webp .mp3 .mp4
    # Output the result according to it
    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".webp"):
        print("image/webp")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    elif filename.endswith(".mp3"):
        print("audio/mpeg")
    elif filename.endswith(".mp4"):
        print("video/mp4")
    else:
        print("application/octet-stream")


