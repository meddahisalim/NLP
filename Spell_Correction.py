from textblob import TextBlob

text = "i havvd i goood speling"

correct_text = TextBlob(text).correct()

print(correct_text)