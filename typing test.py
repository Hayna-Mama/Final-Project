import time

def calculate_accuracy(original_text, typed_text):
    correct_chars = 0
    for i in range(min(len(original_text), len(typed_text))):
        if original_text[i] == typed_text[i]:
            correct_chars += 1
    accuracy = correct_chars / len(original_text) * 100
    return accuracy

def typing_test():
    # Predefined text for typing
    text_to_type = (
        "The quick brown fox jumps over the lazy dog. "
        "This is a typing test to measure your speed and accuracy."
    )
    
    print("Typing Master Challenge")
    print("Type the following text as quickly and accurately as you can:\n")
    print(text_to_type, "\n")

    input("Press Enter to start...")

    # Record the start time
    start_time = time.time()

    # Get the user input
    typed_text = input("\nStart typing here:\n")

    # Record the end time
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate accuracy
    accuracy = calculate_accuracy(text_to_type, typed_text)

    # Calculate words per minute (WPM)
    words_typed = len(typed_text.split())
    minutes_taken = time_taken / 60
    wpm = words_typed / minutes_taken

    # Display results
    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {wpm:.2f} WPM")

if __name__ == "__main__":
    typing_test()
