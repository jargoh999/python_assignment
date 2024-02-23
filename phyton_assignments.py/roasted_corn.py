Sample_string = 'google.com'
sample = {}
for char in Sample_string:
    sample[char] = Sample_string.count(char)
print(sample)

print({k: Sample_string.count(k) for k in Sample_string})