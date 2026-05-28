import base64
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_message=""
        for s in strs:
            encoded_message+=f"{len(s)}*"+s
        return encoded_message

    def decode(self, s: str) -> List[str]:
        orginal_list = []
        index = 0
        while index < len(s) :
            # find the "*"
            k = index
            while s[k] != "*":
                k+=1
            
            length = s[index:k]
            length = int(length)
            orginal_list.append(s[k+1:k+1+length]) 
            index = k+length+1
                
        return orginal_list