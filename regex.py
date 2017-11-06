rule_regex = r'(^\(*!?\(*\w(\s*[+|^](\s*\(*!?\(*\w\)*\s*[+|^])*(\s*\(*!?\(*\w\)*\s*))*)\s*(=>|<=>)\s*(\(*!?\(*\w(\s*[+|^](\s*\(*!?\(*\w\)*\s*[+|^])*(\s*\(*!?\(*\w\)*\s*))*)\)*\s*$'
fact_regex = r'^=\w*\s*$'
query_regex = r'^\?\w+\s*$'
and_regex = r'\w+\+\w+'
xor_regex = r'\w+\^\w+'
or_regex = r'\w+\|\w+'
