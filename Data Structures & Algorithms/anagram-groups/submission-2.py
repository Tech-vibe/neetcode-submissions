class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_list= []
        anagram_list = []
        
        for idj,j in enumerate(strs):
            anagram_list = []
            word = j
            if word not in anagram_list:
                anagram_list.append(word)
            for idx,i in enumerate(strs):
                if sorted(word) == sorted(i) and idj != idx:
                    anagram_list.append(i)
            if not any(word in inner_list for word in anagram_list for inner_list in result_list):
                result_list.append(anagram_list)

        return result_list

