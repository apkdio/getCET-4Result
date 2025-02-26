import requests
import json
from urllib.parse import quote
name = input("输入姓名:")
id_card = input("输入身份证号:")
print()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
                "Referer": "https://cjcx.neea.edu.cn/html1/folder/21083/9970-1.htm"}
url = f"https://cachecloud.neea.cn/latest/results/cet?km=1&xm={quote(name)}&no={id_card}&source=pc"
response = json.loads(requests.get(url, headers=header).text)
if response["code"] == 404:
  print("查询失败！请检查信息是否正确以及是否报考该项考试！")
else:
  print(f"姓名:{response['xm']}\n"
        f"证件号:{response['sfz']}\n"
        f"准考证号:{response['zkzh']}\n"
        f"学校:{response['xx']}\n"
        f"------------------------\n"
        f"总分:{response['score']}\n"
        f"听力:{response['sco_lc']}\n"
        f"阅读:{response['sco_rd']}\n"
        f"写作:{response['sco_wt']}\n"
        f"------------------------")
print("完毕!")
