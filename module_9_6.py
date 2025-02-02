def all_variants(text):
    for r in range(len(text)):
        for k in range(len(text) - r):
            yield text[k:r+1+k]




a = all_variants("abc")
for i in a:
    print(i)