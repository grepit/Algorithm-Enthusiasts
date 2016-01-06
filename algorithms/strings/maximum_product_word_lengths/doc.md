# Maximum Product Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. You may assume that each word will 
contain only lower case letters. If no such two words exist, return 0.

##Example 1:

Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

##Example 2:

Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

##Example 3:

Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

## brute force

compare each pair of words and keeps track of max product if two words have no common characters.
