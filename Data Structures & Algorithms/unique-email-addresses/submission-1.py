class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res_set = set()
        for email in emails:
            at_splits = email.split('@')
            plus_split = at_splits[0].split('+')[0]
            plus_string = "".join(plus_split.split('.'))
            res_set.add(f'{plus_string}@{at_splits[1]}')
        return len(res_set)