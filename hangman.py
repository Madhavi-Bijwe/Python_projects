import random

words=["python","java","c","javascript","html","css","php","kotlin","sql","c++","R","Ruby", "Swift","TypeScript"]

word=random.choice(words)
guessed=["_"]*len(word)
attempts=6
used_letters=[]

print("Welcome to Hangman!")
print("Guess the word (Programming languages:):", " ".join(guessed))

while attempts>0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue
    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
        print("Correct!")
    else:
        attempts-=1
        print("Wrong! Attempts left:",attempts)

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("🎉 You won! The word was:",word)
else:
    print("💀 You lost! The word was:",word)
