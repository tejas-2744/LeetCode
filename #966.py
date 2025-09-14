class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_perfect = set(wordlist)
        words_cap={}
        words_vow={}

        for word in wordlist:
            word_lower=word.lower()
            if word_lower not in words_cap:
                words_cap[word_lower]=word
            
            word_devowel=self.devowel(word_lower)
            if word_devowel not in words_vow:
                words_vow[word_devowel]=word

        ans=[]

        for query in queries:
            if query in words_perfect:
                ans.append(query)
                continue
            
            query_lower=query.lower()
            if query_lower in words_cap:
                ans.append(words_cap[query_lower])
                continue
            
            query_devowel=self.devowel(query_lower)
            if query_devowel in words_vow:
                ans.append(words_vow[query_devowel])
                continue

            ans.append("")

        return ans

    def devowel(self,word):
        return "".join('*' if c in 'aeiou' else c for c in word)