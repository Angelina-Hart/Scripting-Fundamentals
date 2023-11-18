# Write your code here
word = input("Word to convert:")
count = int(input("How many letters at the end of the word should be converted?:"))
total_length = len(word)
start_length = total_length - count
start = word[0:start_length]
end = word[start_length:total_length]
end = end.upper()
word = start + end
print(word)
