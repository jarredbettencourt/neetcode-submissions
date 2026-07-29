class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort_list = [(height, name) for name, height in zip(names, heights)]
        sort_list.sort(reverse=True)
        return [name for height, name in sort_list]