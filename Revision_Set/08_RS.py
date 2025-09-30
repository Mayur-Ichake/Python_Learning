# 3.Spam comment is  defined as a text containing following keyword. write a program to detect this spams

fake_msg = input("Enter your msg to check spam or not: ")

spam_comments = {
    "make a lot of money",
    "click this",
    "buy this",
    "send me otp",
    "send your email"
}

# Flag to check spam
is_spam = False

# Check if any spam phrase is present in message
for spam in spam_comments:
    if spam in fake_msg.lower():   # check phrase inside full message
        is_spam = True
        break

if is_spam:
    print("This msg is spam,\nPlease contact above helpline number\nLoading....")
else:
    print("This msg is not a spam,\nThanks for visiting our website")
