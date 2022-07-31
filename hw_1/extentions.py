def main():
    file_name = input("File Name: ")
    try:
        _, file_type = file_name.split(".")
    except:
        file_type = file_name
    
    if file_type == "gif":
        print("image/gif")
    elif file_type == "jpg" or file_type == "jpeg":
        print("image/jpeg")
    elif file_type == "png":
        print("image/png")
    elif file_type == "pdf":
        print("application/pdf")
    elif file_type == "txt":
        print("text/plain")
    elif file_type == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()