"""
Longest common subsequence implementation starter
"""
import lab_2.main

original = 'the cat is sleeping'
suspicious = 'the little cat is running'

original_tokens = main.tokenize_by_lines(original)
suspicious_tokens = main.tokenize_by_lines(suspicious)

print("Tokenized original text:", original_tokens)
print("Tokenized suspicious text:", suspicious_tokens)

lcs_length = main.find_lcs_length(original_tokens, suspicious_tokens, plagiarism_threshold=0.3)
print("Length of the longest common subsequence:", lcs_length)

matrix = main.fill_lcs_matrix(original_tokens, suspicious_tokens)

lcs = main.find_lcs(original_tokens, suspicious_tokens, matrix)
print("The longest common subsequence:", lcs)

plagiarism_score = main.calculate_plagiarism_score(lcs_length, suspicious_tokens)
print("The plagiarism score:", plagiarism_score)

text_plagiarism_score = main.calculate_text_plagiarism_score(original_tokens, suspicious_tokens, plagiarism_score)
print("Text average plagiarism:", text_plagiarism_score)

RESULT = text_plagiarism_score
assert RESULT, 'Not working'
