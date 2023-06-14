from rouge import Rouge

# Initialize the Rouge object
rouge = Rouge()

# Example summaries and references
summary = "This is a sample summary."
reference = "This is a sample reference."

# Compute ROUGE scores
scores = rouge.get_scores(summary, reference)

# Print the ROUGE scores
print(scores)