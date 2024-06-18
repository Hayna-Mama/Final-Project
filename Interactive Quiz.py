def load_questions():
    # For demonstration, using a small set of questions.
    # Extend this dictionary to include 100 questions.
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the capital of Italy?", "answer": "Rome"},
        {"question": "What is the largest planet in our Solar System?", "answer": "Jupiter"},
        {"question": "What is the boiling point of water?", "answer": "100"},
        # Add more questions as needed.
    ]
    return questions

def ask_question(question_dict):
    question = question_dict["question"]
    correct_answer = question_dict["answer"]
    
    user_answer = input(f"{question}\nYour answer: ")
    return user_answer.strip(), correct_answer

def interactive_quiz():
    questions = load_questions()
    user_answers = []
    correct_count = 0
    
    for i, question_dict in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        user_answer, correct_answer = ask_question(question_dict)
        user_answers.append({"question": question_dict["question"], "user_answer": user_answer, "correct_answer": correct_answer})
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    print("\nQuiz completed!")
    print(f"Your score: {correct_count} out of {len(questions)}")

    print("\nReview your answers:")
    for i, ans in enumerate(user_answers, start=1):
        print(f"Question {i}: {ans['question']}")
        print(f"Your answer: {ans['user_answer']}")
        print(f"Correct answer: {ans['correct_answer']}")
        print("")

if __name__ == "__main__":
    interactive_quiz()
