def ask_question(question, options, correct_answer):
    print(question)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    user_choice = int(input("Enter your choice (1-4): "))
    if user_choice == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print("Incorrect.\n")
        return 0

questions = [
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], 2),
    ("In which country was the composer Wolfgang Amadeus Mozart born?", ["Italy", "France", "Germany", "Austria"], 4),
    ("What famous speech begins with the words \"I have a dream\"?", ["Gettysburg Address", "Emancipation Proclamation", "Martin Luther King Jr.'s \"I Have a Dream\" speech", "Declaration of Independence"], 3),
    ("The Great Wall of China was primarily built to protect against invasions from which group of people?", ["Vikings", "Mongols", "Romans", "Egyptians"], 2),
    ("Who wrote the novel \"1984,\" which depicts a dystopian future?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien"], 1),
    ("The ancient city of Rome is located in which modern-day country?", ["Greece", "Italy", "Turkey", "Egypt"], 2),
    ("What is the largest ocean on Earth?", ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"], 3),
    ("The famous play \"Hamlet\" was written by which playwright?", ["William Shakespeare", "Samuel Beckett", "Oscar Wilde", "Tennessee Williams"], 1),
    ("Mount Everest, the highest mountain in the world, is located in which mountain range?", ["Rocky Mountains", "Andes Mountains", "Himalayas", "Alps"], 3),
    ("Which historical figure is known for his contributions to the field of physics, including the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], 2),
]

def run_quiz(questions):
    total_score = 0
    for question, options, correct_answer in questions:
        total_score += ask_question(question, options, correct_answer)

    print(f"Quiz complete! Your total score is: {total_score}/{len(questions)}")

run_quiz(questions)
