with open("invited_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        strip_line = line.strip()
        with open("starting_letter.txt") as letter:
            content = letter.read()
            replaced_content = content.replace("[name]", strip_line)
            with open(f"ReadyToSend/{strip_line}.txt", "w") as nf:
                nf.write(replaced_content)

