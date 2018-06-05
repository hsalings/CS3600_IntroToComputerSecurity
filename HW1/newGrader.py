import random
import caesarCipher as solution

#Replace miner_12345678 with your file name

ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("dictionary.txt") as f:
    WORDS = f.read().split()

with open("./l33t.txt") as f:
    LEET = f.read().split()

with open("./otherwords.txt") as f:
    OTHER = f.read().upper().split()

def generate_sentence():
    l = random.getrandbits(1)
    count = random.randint(10,15)
    oc = random.randint(0,4)

    out = []

    for i in range(count):
        out.append(random.choice(WORDS))

    for i in range(oc):
        out.append(random.choice(OTHER))

    if l:
        out.append(random.choice(LEET))

    random.shuffle(out)

    return " ".join(out)

def rot(sentence):
    shift = random.randint(1,25)
    out = ""

    for letter in sentence:
        if letter not in ALPHA:
            out += letter
        else:
            i = ALPHA.index(letter)
            i = (i+shift)%26
            out += ALPHA[i]
    return out
    

def main():
    score = 0

    for i in range(100):
        original = generate_sentence()
        encrypted = rot(original)

        sol,lastname,num = solution.bruteforce(encrypted)

        if sol.upper() == original:
            score += 1
        else:
            print("You missed one!\nThe sentence was '" + original + "'")

    print("Completed! You got " + str(score) + " out of 100 right.")


if __name__ == "__main__":
    main()
    
