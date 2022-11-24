names_list = []
with open("./Input/Names/invited_names.txt") as receivers_names:
    names = receivers_names.readlines()
    for name in names:
        names_list.append(name.removesuffix("\n"))

with open("./Input/Letters/starting_letter.txt") as letter:
    template_letter = letter.read()

for name in names_list:
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as final_letter:
        new_letter = template_letter.replace("[name]", name)
        final_letter.write(new_letter)
