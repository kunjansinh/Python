import random
import time


def run_reaction_test():
    print("========== REACTION TIME TEST ==========")
    print("Wait for GO, then press Enter as quickly as possible.")
    print("Do not press Enter before the signal!")

    input("\nPress Enter when you are ready...")

    delay = random.uniform(2, 5)

    print("\nGet ready...")
    time.sleep(delay)

    print("GO!")

    start_time = time.perf_counter()
    input()
    end_time = time.perf_counter()

    reaction_time = end_time - start_time

    print(f"\nYour reaction time: {reaction_time:.3f} seconds")

    if reaction_time < 0.25:
        print("Excellent reaction!")
    elif reaction_time < 0.40:
        print("Good reaction!")
    else:
        print("Keep practising!")


run_reaction_test()