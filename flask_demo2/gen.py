import time
import hashlib
import base64

app_code = ''
app_key = ''


timestamp = str(int(round(time.time() * 1000)))
src = app_code + app_key + timestamp
md5_result = hashlib.md5()
md5_result.update(src.encode("utf-8"))
base64_res = base64.b64encode(md5_result.digest())
check_word_result = base64_res.decode()

print("check_word", check_word_result)
print("timestamp", timestamp)
print(time.strftime('%Y-%m-%d', time.localtime()))