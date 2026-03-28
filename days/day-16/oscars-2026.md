[Day 15 challenge](https://www.codedex.io/daily-challenge/2026-03-16)

Last night was the Academy Awards! It’s time to see who’s got the best predictions. 🍿

Instead of placing bets on Kalshi, you and your friends organized an Oscars Pool, where everyone predicts the winners across several award categories.

oscars

After the ceremony, we now have two things:

A list of the actual winners:
Best Picture: One Battle After Another
Best Actor: Michael B. Jordan
Best Actress: Jessie Buckley
Best Director: Paul Thomas Anderson
Each friend’s predicted winners
Complete the function that calculates each friend’s prediction accuracy:

accuracy
=
correct predictions
total predictions
accuracy= 
total predictions
correct predictions
​
 
Which friend has the highest accuracy? Return their name. If there's a tie, return "Tie".

Examples

Example 1

Input:
predictions = [
  ["@sonny", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Ryan Cooger"],
  ["@adorkababe", "F1", "Timothée Chalamet", "Jessie Buckley", "Josh Safdie"],
  ["@tylerwhit", "Sinners", "Michael B. Jordan", "Rose Byrne", "Paul Thomas Anderson"]
]
Output: "@sonny"
@sonny got 3/4, @adorkababe got 1/4, and @tylerwhit got 2/4.

Example 2

Input:
predictions = [
  ["Kalshi", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"],
  ["Polymarket", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
]
Output: "Tie"
Both have a perfect score, so it's a tie.

Example 3

Input:
predictions = [
  ["Rotten Tomatoes", "The Secret Agent", "Wagner Moura", "Renate Reinsve", "Kleber Mendonça Filho"],
  ["IMDb", "One Battle After Another", "Timothée Chalamet", "Jessie Buckley", "Chloé Zhao"]
]
Output: "IMDb"
Rotten Tomatoes got 0/4 and IMDb got 2/4.