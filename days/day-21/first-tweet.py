def tweet_balance(tweet: str) -> int:

    MAX_LEN = 140

    # Validation 
    if not isinstance(tweet, str):
        raise TypeError("tweet must be a string")

    if tweet == "":
        return MAX_LEN

    words = tweet.split()
    used = 0

    for word in words:
        # Username 
        if word.startswith("@"):
            used += 20
        # URL 
        elif word.startswith("http://") or word.startswith("https://"):
            used += 23
        # Emoji detection (simple) 
        elif any(ord(c) > 10000 for c in word):
            # count each emoji as 2
            used += 2 * len(word)
        #  Normal text 
        else:
            used += len(word)

    # add spaces (split removed them)
    spaces = max(len(words) - 1, 0)
    used += spaces

    return MAX_LEN - used