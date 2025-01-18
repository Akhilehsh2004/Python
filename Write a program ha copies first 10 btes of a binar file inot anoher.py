with open("file1.txt", "rb") as file1:
    with open("file2.txt", "wb") as file2:
        buf = file1.read(10)
        file2.write(buf)
print("File Copied")