import io
with io.open('/data3/bbdoffline/dp-wangjunyong/py_job/xzcf_rules.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
