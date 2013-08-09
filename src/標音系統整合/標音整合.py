from 閩南資料.詞 import 詞
from 華語台語雙語語料庫系統.文章標點處理工具 import 文章標點處理工具
from 言語資料庫.公用資料 import 標點符號
from 標音資料庫工具.揣音標 import 揣言語層的字詞
from 標音資料庫工具.揣音標 import 揣腔口型體資料

class 標音整合:
	腔口 = '漢語族閩方言閩南語偏漳優勢音'
	文讀層 = '文讀層'
	白話層 = '白話層'
	標點處理工具 = 文章標點處理工具()
	def __init__(self, 腔口):
		self.腔口 = 腔口
		self.文讀字 = set()
		[self.文讀字.add(字詞[0]) for 字詞 in 揣言語層的字詞(self.腔口, '文讀層')]
		self.白話字 = set()
		[self.白話字.add(字詞[0]) for 字詞 in 揣言語層的字詞(self.腔口, '白話層')]
		self.標點處理工具.標點符號 = {}
# 		print(self.文讀字)
	def 標音(self, 台語字, 語言層):
# 		return self.產生標音結果(台語字, 語言層)
		return [選擇[0] for 選擇 in self.產生標音結果(台語字, 語言層)]
	def 產生標音結果(self, 台語字, 語言層):
		字=self.標點處理工具.分離漢字(台語字)
		標音結果 = []
		i = 0
		while i < len(字):
			for j in range(20, 0, -1):
				if i + j <= len(字):
					腔口型體資料 = 揣腔口型體資料(self.腔口, ''.join(台語字[i:i + j]))
					流水號 = set()
					[流水號.add(字詞[0]) for 字詞 in 腔口型體資料]
					if len(流水號) > 0:
						字詞選擇 = []
						if 語言層 == '文讀層':
							指定音 = 流水號 & self.文讀字
						elif 語言層 == '白話層':
							指定音 = 流水號 & self.白話字
						else:
							指定音 = 流水號
						for 流水號碼, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變 in 腔口型體資料:
							if len(指定音) == 0 or 流水號碼 in 指定音:
								字詞選擇.append(詞(型體, 音標, self.標點處理工具))
						標音結果.append(字詞選擇)
						i += j
						break
			else:
				if 台語字[i] in 標點符號:
					標音結果.append([詞(字[i], 字[i], None)])
				else:
					標音結果.append([詞(字[i], '', None)])
				i += 1
		return 標音結果

if __name__ == '__main__':
	標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
	音 = 標音.標音('台語字', 標音.文讀層)
	print(音)
	音 = 標音.標音('台語字', 標音.白話層)
	print(音)
	音 = 標音.標音('白日依山盡', 標音.文讀層)
	print(音)
	音 = 標音.標音('點仔膠', 標音.文讀層)
	print(音)
	音 = 標音.標音('好好鱟刣甲屎那流。', 標音.文讀層)
	print(音)
	音 = 標音.標音('好好鱟刣甲屎那流,', 標音.文讀層)
	print(音)
	音 = 標音.標音('好好鱟刣甲屎那流,', 標音.白話層)
	print(音)

