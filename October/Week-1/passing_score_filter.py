def separate_scores(scores, pass_mark):
    passed = []
    failed = []

    for score in scores:
        if score >= pass_mark:
            passed.append(score)
        else:
            failed.append(score)

    return passed, failed


scores = [35, 72, 48, 91, 64, 27, 83, 55]

passed, failed = separate_scores(scores, 40)

print("--- Score Report ---")
print(f"All scores: {scores}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Number passed: {len(passed)}")
print(f"Number failed: {len(failed)}")