# Write your code here
sentence = input("Sentence:")
wht = sentence.strip()
low = wht.lower()
substr = input("Word to look for in sentence:")
num = low.count(substr)
print(f"There are {num} occurrences of \'{substr}\' in the sentence.'")
