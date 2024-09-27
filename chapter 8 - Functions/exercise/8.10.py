def show_messages(text_messages):
    """ Print text messages """
    for text in text_messages:
        print(text)

def send_messages(text_messages, sent_messages):
    """ Send messages """
    while text_messages:
        current_text = text_messages.pop()
        sent_messages.append(current_text)

text_messages = ['I will stick to my goals', 'I will do it', 'Ill eat healthy']
sent_messages = []
send_messages(text_messages[:] , sent_messages)
show_messages(text_messages)
show_messages(sent_messages)