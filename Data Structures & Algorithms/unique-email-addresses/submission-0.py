class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res_set = set()
        for email in emails:
            at_splits = email.split('@')
            plus_split = at_splits[0].split('+')[0]
            plus_string = plus_split.split('.')
            temp_string = ""
            for n in plus_string:
                temp_string += n
            res_set.add(f'{temp_string}@{at_splits[1]}')
        return len(res_set)