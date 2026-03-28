[Day 11 challenge](https://www.codedex.io/daily-challenge/2026-03-12)

It's the World Wide Web's birthday! On March 12, 1989, British scientist Tim Berners-Lee submitted a proposal titled “Information Management: A Proposal” while working at CERN.

The proposal described a network of documents that could link to each other. His manager famously described it as “vague but exciting”, LOL. That idea became WWW!

Tim Berners-Lee

One part of the proposal is about URLs. URL stands for Uniform Resource Locator. It is the unique address used to identify and locate a webpage, image, or document on the internet. Frequently referred to as a web address".

Given a string representing a web address, determine if it's a valid URL or not.

For our validator, make sure it follows these rules:

It starts with http:// or https://
The domain must contain at least one dot .
The domain only contains letters, digits, hyphens -, or dots .
Return the string "valid" if it is, or "invalid" if it isn't.

Example 1

- Input: https://codedex.io
- Output: valid
Example 2

- Input: https://netflixcom
- Output: invalid
Example 3

- Input: http://en.wikipedia.org
- Output: valid
Fun fact: Berners-Lee has expressed regret over the "clumsy" syntax, specifically the ://. 🤭

Fun fact #2: https came about five years after the original proposal (which only had http).