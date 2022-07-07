
# Create a Question Class
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_q = Question("Is this true?", "False")
print(new_q.text)