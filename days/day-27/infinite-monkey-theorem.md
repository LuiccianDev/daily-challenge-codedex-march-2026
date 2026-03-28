[Day 26 challenge](https://www.codedex.io/daily-challenge/2026-03-27)

The Infinite Monkey Theorem is one of math's most beloved thought experiments!

Picture this: If a monkey sits at a typewriter and randomly hits keys forever, it will eventually type the complete works of Shakespeare!

Obviously we can't wait forever 🤨, so we're going to measure just how close our monkey is getting. But here's the twist, our monkey types a string of text much longer than the target. Shakespeare might be hiding somewhere in the middle without the monkey even knowing it!

For each valid starting position in the attempt, we check a window of characters the same length as the target and calculate a similarity score — the percentage of characters that match the target in the exact same position.

For an example with target = "hamlet":

attempt = "xxhamxet"
           |||
           ||└─── window at index 2: "hamxet" → 83.33% ✅ Best!
           |└─── window at index 1: "xhamxe" → 0% ❌ Closer, but matches are off by one
           └─── window at index 0: "xxhamx" → 0% ❌ Too early, so nothing lines up
Slide the window across every valid position and find the highest similarity score. From that score, estimate how many attempts it would take the monkey to stumble onto that window at 100%:

a
t
t
e
m
p
t
s
=
1
(
s
i
m
i
l
a
r
i
t
y
100
)
l
e
n
g
t
h
attempts= 
( 
100
similarity
​
 ) 
length
 
1
​
 
Given a target string and a longer attempt string, return a dictionary/object with:

best_index : the starting index of the most similar window.
similarity : the highest similarity percentage rounded to 2 decimal places, if needed.
attempts : theoretical attempts to hit 100% at that rate, rounded to the nearest whole number. If the best similarity is 0%, set attempts to null. 🐒
*Round similarity to 2 decimal places for the final output only. Use the unrounded similarity value when calculating attempts.

If two windows have the same similarity, return the first one.

Examples

Example 1

Input: target = 'hamlet', attempt = 'xxhamxetxxxx'
Output:
{
  'best_index': 2,
  'similarity': 83.33,
  'attempts': 3
}
The window starting at index 2 is 'hamxet' — 5 out of 6 characters match (h✅ a✅ m✅ x❌ e✅ t✅). The best window in the whole string! 🎭

Example 2

Input: target = 'To be, or not to be.', attempt = '7q$To be, or not to bug?9x'
Output:
{
  'best_index': 3,
  'similarity': 90.0,
  'attempts': 8
}
The window at index 3 is "To be, or not to bug" — 18 out of 20 characters match. The monkey was very close, but there was a bug in the final stretch. 👀