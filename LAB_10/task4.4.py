def process_scores(scores):
    if not scores:
        print("No scores to process.")
        return
    print("Average:", sum(scores)/len(scores))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

process_scores([70, 85, 90, 100, 65])
