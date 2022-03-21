import random

class Game():

    def __init__(self):
        print("Podaj liczbę graczy: ")
        while True:
            try:
                self.liczba_graczy = int(input())
            except ValueError:
                print('Wartość nieprawidłowa')
            else:
                if 1<= self.liczba_graczy <=2:
                    break
                else:
                    print('Wartość spoza zakresu')
    def _play(self):
        print('Gra rozpoczęta')

class Hangman(Game):

    def __init__(self):
        super().__init__()
        print("Podaj poziom trudności:\n1 -- begginer\n2 -- intermediate\n3 -- advanced")
        while True:
            try:
                self.difficulty = int(input())
            except ValueError:
                print('Wartość nieprawidłowa')
            else:
                if 1<= self.difficulty <=3:
                    break
                else:
                    print('Wartość spoza zakresu')
        if self.difficulty == 1:
            self.chances = 8
        elif self.difficulty == 2:
            self.chances = 5
        elif self.difficulty == 3:
            self.chances = 3

    def pick_word(self):
        words = ['Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass', 'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input', 'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel', 'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 'Queen', 'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene', 'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill', 'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage', 'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste', 'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust', 'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White', 'Whole', 'Woman', 'World', 'Youth']
        word = random.randint(1,len(words))
        return words[word]

    def play(self):
        super()._play()
        if self.liczba_graczy == 1:
            word = self.pick_word().lower()
        else:
            print("Podaj słowo do odgadnięcia:")
            word = input().lower()
        word = list(word)
        letters = []
        for i in range(0,len(word)):
            letters.append("_")
        print(F"Twoje słowo:\n{letters}")
        while True:
            try:
                print("Podaj znak: ")
                letter = str(input()).lower()
                assert len(letter) == 1
                assert letter.isalpha()
            except AssertionError:
                print("Podaj tylko jedną literę\n")
            else:
                if letter in word:
                    for i in range (0,len(word)):
                        if letter == word[i]:
                            letters[i] = letter
                    
                else:
                    self.chances -= 1
                    print(F'Litery nie ma w słowie')
                    
            print(F"Twoje słowo:\n{letters}\nPozostała liczba szans: {self.chances}")
            if self.chances == 0:
                print(F'Koniec gry, przegrałxś\nSłowo to {word}')
                break
            if "_" not in letters:
                print('Brawo, wygrałxś!')
                break
            

new_game = Hangman()
new_game.play()