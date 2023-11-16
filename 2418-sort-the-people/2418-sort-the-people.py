class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = zip(heights, names)
        sorted_pairs = sorted(pairs, reverse = True)
        sorted_names = []
        for _, name in sorted_pairs:
            sorted_names.append(name)
            
        return sorted_names