with open("./Day24/Input/Names/invited_names.txt") as f:
    for name in f.read().split("\n"):
        with open("./Day24/Input/Letters/starting_letter.txt") as l:
            contents = l.read().replace("[name]", name).replace("[your name]", "YOUR NAME HERE")
            with open(f"./Day24/Output/ReadyToSend/letter_to_{name}.txt", "w") as final:
                final.write(contents)