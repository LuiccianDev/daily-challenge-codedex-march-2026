[Day 20 challenge](https://www.codedex.io/daily-challenge/2026-03-21)

On March 21, 2006 (exactly 20 years ago), Twitter co-founder Jack Dorsey sent the first tweet:


At that time, tweets were limited to 140 characters, inspired by the SMS standard.

Over time, Twitter has added different counting rules for things like username mentions, URL links, and emojis so they all take up a more consistent amount of space.

For this challenge, we’ll use a simplified version of that idea:

👤 Usernames (words starting with @) always count as 20 characters
🔗 URLs (words starting with http:// or https://) always count as 23 characters
😀 Emojis always count as 2 characters (though back in 2006, emojis were barely a thing, so don't worry about testing them!)
All other characters, including spaces and punctuation, will count normally.

Given a tweet string, return the number of characters left out of 140. If the tweet is too long, return the number of characters over the limit as a negative number.

Think of it like a bank account: You start with 140 and spend as you type! 🐦

Examples

Example 1

Input: "just setting up my twttr"
Output: 116
24 plain characters used, 116 remaining. ✅

Example 2

Input: "Check out this link https://www.averylongurlthatgoesonnnnnn.com and this one https://short.co too!"
Output: 55
Two URLs each count as exactly 23 characters regardless of length. 55 characters to spare!