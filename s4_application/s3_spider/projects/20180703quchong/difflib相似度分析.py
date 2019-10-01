
import difflib

query_str = '市公安局'
s1 = '广州市邮政局'
s2 = '广州市公安局'
s3 = '广州市检查院'
print(difflib.SequenceMatcher(None, query_str, s1).quick_ratio())
print(difflib.SequenceMatcher(None, query_str, s2).quick_ratio())
print(difflib.SequenceMatcher(None, query_str, s3).quick_ratio())
