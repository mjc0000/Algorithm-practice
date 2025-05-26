def groupanalysis(strs):

    analysis_groups = {}

    for s in strs:

        sorted_s="".join(sorted(s))

        if sorted_s in analysis_groups:
            analysis_groups[sorted_s].append(s)

        else:
            analysis_groups[sorted_s]=[s]

    return list(analysis_groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupanalysis(strs))