def main():
    FileName = input("File Name: ").strip().lower()

    if '.' in FileName:
        extension = FileName.rsplit('.', 1)[-1]
    else:
        extension = ''

    match extension:
        case 'gif':
          print("image/gif")
        case 'jpg':
           print("image/jpeg")
        case 'jpeg':
            print("image/jpeg")
        case 'png':
            print("image/png")
        case 'pdf':
            print("application/pdf")
        case 'txt':
             print("text/plain")
        case 'zip':
            print("application/zip")
        case _:
            print("application/octet-stream")

if __name__ == "__main__": main()



# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
