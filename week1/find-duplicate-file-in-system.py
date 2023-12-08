class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directory = {}
        total_content_count = {}
        for path in paths:
            temp_list = path.split()
            for idx in range(1, len(temp_list)):
                name_n_content = temp_list[idx].split('(')
                if (name_n_content[1] not in directory):
                    directory[name_n_content[1]] = []
                directory[name_n_content[1]].append(temp_list[0] + '/' + name_n_content[0])
                total_content_count[name_n_content[1]] = 1 + total_content_count.get(name_n_content[1] , 0)
        ans = []
        for val in total_content_count:
            if total_content_count[val] > 1:
                ans.append(directory[val])
        return ans