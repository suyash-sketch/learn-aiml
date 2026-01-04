import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Suyash Khandagale"

tokens = enc.encode(text)

print('Tokens', tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 336, 3731, 1229, 658, 5172, 348, 1167])
print(decoded)