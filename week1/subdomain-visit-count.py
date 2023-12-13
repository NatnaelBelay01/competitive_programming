class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        total_count = {}
        for vals in cpdomains:
            count , domain1 = vals.split()
            total_count[domain1] = int(count) + total_count.get(domain1, 0)
            domain = domain1.split('.')
            total_count[domain[-1]] = int(count) + total_count.get(domain[-1], 0)
            if (len(domain) > 2):
                temp = '.'.join(domain[1:])
                total_count[temp] = int(count) + total_count.get(temp, 0)
 
        result = []

        for vals in total_count:
            result.append(" ".join([str(total_count[vals]), vals]))
        return result
