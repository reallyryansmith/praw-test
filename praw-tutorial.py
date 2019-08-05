import praw

reddit = praw.Reddit('bot1', user_agent='myredditapp:v0.1 (by /u/AlbertoDorito)')

keepchoosing = "y"
while keepchoosing.lower() == "y":
    choice = int(input("Would you like to see?: \n "
                   "the top comments from one thread where a guy wears a fire Ness inspired outfit (Press 1 and hit enter)\n "
                   "or would you rather see the top 10 HOT submissions from /r/learnpython? (Press 2 and hit enter)\n "))
    submission2 = reddit.submission(
        url='https://www.reddit.com/r/streetwear/comments/c3sj01/wdywt_low_quality_ness_cosplay/')

    if choice == "1":
        for top_level_comment in submission2.comments:
            print(top_level_comment.body)
        keepchoosing = input("Would you like to choose again? (Y/N): ")

    elif choice == "2":
        for submission in reddit.subreddit('learnpython').hot(limit=10):
            print(submission.title)
        keepchoosing = input("Would you like to choose again? (Y/N): ")
    else:
        print("Not even a choice bro")
        keepchoosing = input("Would you like to choose again? (Y/N): ")
else:
    print("Okay bye")
