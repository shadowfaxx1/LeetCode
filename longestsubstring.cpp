#include <string>
#include <unordered_map>
#include <algorithm>
#include<iostream>
#include<stdlib.h>
#include<bits/stdc++.h>

using namespace std;

int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> mp;
        int left = 0;
        int right = 0;
        int len = 0;
        int mx = 0; // Initialize to 0

        while (right < s.length()) {
            if (mp.find(s[right]) == mp.end()) {
                mp[s[right]]++;
                len++;
                right++;
            } else {
                mx = max(len, mx);
                mp[s[left]]--;
                len--;
                left++;
            }
        }

        // Handle the last character separately
        mx = max(len, mx);

        return mx;
    }
int main() {

    std::string s1 = "abcabcbb";
    int result1 = lengthOfLongestSubstring(s1);
    std::cout << "Length of longest substring without repeating characters: " << result1 << std::endl;

    std::string s2 = "bbbbb";
    int result2 = lengthOfLongestSubstring(s2);
    std::cout << "Length of longest substring without repeating characters: " << result2 << std::endl;

    std::string s3 = "pwwkew";
    int result3 = lengthOfLongestSubstring(s3);
    std::cout << "Length of longest substring without repeating characters: " << result3 << std::endl;

    return 0;
}
