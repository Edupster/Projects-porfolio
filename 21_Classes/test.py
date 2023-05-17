class Email():
    def __init__(self,from_address, email_contents):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
    
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True  
    
inbox=[]

def add_email(email,contents):
    new_email = Email(email,contents)
    inbox.append(new_email)

def get_count():
    
    return len(inbox)

def get_email(i):
    inbox[i].mark_as_read()
    print(f"From:{inbox[i].from_address} Content: {inbox[i].email_contents}")

def get_unread_emails():
    for i in inbox:
        if i.has_been_read == False:
            print(f"From:{i.from_address} Content: {i.email_contents}")

def get_spam_emails():
    for i in inbox:
        if i.is_spam == True:
            print(f"From:{i.from_address} Content: {i.email_contents}")

def delete():
    inbox=[]
    return inbox

add_email("edu@kdjk","ksaldjfaf")
add_email("k;alsdjf;a","jf")
get_email(0)
