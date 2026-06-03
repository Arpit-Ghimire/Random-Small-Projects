import time
import random as r

def calculate_time(start, end):
    total_seconds = end - start
    total_minutes = total_seconds / 60
    return total_seconds, total_minutes

def measure_accuracy(original, typed):
    if not typed:
        return 0.0
    
    matches = 0
    # Pairing up the letters for comparison
    for a, b in zip(original, typed):
        if a == b:
            matches = matches + 1  # Adding a point if they match together

    accuracy = (matches / len(original)) * 100
    return accuracy

def display_results(speed, acc, duration):

    print("\n" * 3)
    print("=" * 40)
    print("           TYPING STATS           ")
    print("=" * 40)
    print(f" > Speed    : {speed:.2f} WPM")
    print(f" > Accuracy : {acc:.2f}%")
    print(f" > Time     : {duration:.2f} sec")
    print("=" * 40)

def start_typing_test():
    paragraphs = [
        "The green forest was very quiet. A light breeze moved the leaves of the old trees.",
        "Modern computers are incredibly fast today. Most people carry a smartphone.",
        "Writing clean code requires patience. You must remember to close your brackets."
    ]
    
    print("\n" * 5, "........... Typing Speed Calculator ...........".center(50))
    target = r.choice(paragraphs)
    print("-"*150)
    print(f"\nTARGET TEXT:\n{target}")
    print("-"*150)
    input("\n[ Press Enter to Start ]")
    
    t_start = time.time()
    user_text = input("\nTYPE HERE: ")
    t_end = time.time()
    
    duration_sec, duration_min = calculate_time(t_start, t_end)
    
    # WPM Calculation (Standard: 5 chars = 1 word)
    wpm = (len(user_text) / 5) / duration_min if duration_min > 0 else 0
    
    accuracy_score = measure_accuracy(target, user_text)
    
    # Output
    display_results(wpm, accuracy_score, duration_sec)

if __name__ == "__main__":
    start_typing_test()
