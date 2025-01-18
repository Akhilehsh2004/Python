with open("Names.txt", 'r') as names_file, open("Body.txt", 'r') as body_file:
    text = body_file.read()
    for name in names_file:
        with open(name.strip() + ".txt", 'w') as file:
            file.write(f"Hello {name.strip()} {text}")
