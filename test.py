def longestValidParentheses(s: str) -> int:
        longest=0
        recent=""
        x=0
        curr=0
        while(x<len(s)):
            if(s[x])==")" and recent=="(":
                recent=""
                curr+=2
            elif s[x]=="(" and recent=="":
                recent="("
            else:
                recent=s[x]
                longest=max(longest,curr)
                curr=0
            x+=1
        return longest
print(longestValidParentheses("(()"))