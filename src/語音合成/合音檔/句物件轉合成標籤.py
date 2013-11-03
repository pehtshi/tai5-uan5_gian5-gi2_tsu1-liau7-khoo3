from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 語音合成.合音檔.臺羅變調暫時處理 import 臺羅變調暫時處理
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

def 臺羅聲韻轉辨識合成型(聲, 韻):
	if 聲 == 'm' or 聲 == 'n' or 聲 == 'ng':
		if 'm' not in 韻 and 'n' not in 韻:
			if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
				韻 = 韻[:-1] + 'nn' + 韻[-1]
			else:
				韻 += 'nn'
			if 韻 == 'oonnh':
				韻 = 'onnh'
	if 聲 == '':
		聲 = 'H'  # 喉塞
	return (聲, 韻)

# a-b+c/tiau7:t1/su5:s1!s2@s3/ku3:k1^k2_k3
# 前音-此音+後音/調：調類/詞：第幾字!上尾第幾字@攏總字/句：第幾字^上尾第幾字_攏總字
class 句物件轉合成標籤:
	安靜符號 = 'sil'
	安靜調 = 'x'
	安靜標籤 = 'x-sil+x/tiau3:x/su5:x!x@x/ku3:x^x_x'
	譀鏡 = 物件譀鏡()
	變調處理 = 臺羅變調暫時處理()
	def 句物件轉標籤(self, 拼音型態, 句物件):
		if 拼音型態 == 臺灣閩南語羅馬字拼音:
			字陣列 = self.變調處理.變調(句物件)
			音標 = self.譀鏡.看音(詞(字陣列))
		else:
			音標 = self.譀鏡.看音(句物件)
		return self.拼音轉合成標籤佮聲韻資料(拼音型態, 音標)[0]
	def 拼音轉合成標籤佮聲韻資料(self, 拼音型態, 臺羅音標):
		print(臺羅音標)
		聲韻標籤 = [self.安靜符號]
		調標仔 = []  # 橫直 調標仔[-1] 嘛是安靜
		for 詞 in 臺羅音標.split(' '):
			for 字 in 詞.split('-'):
				if 字=='sil':
					聲韻標籤.append(self.安靜符號)
					調標仔.append(self.安靜調)
				else:
					臺羅拼音 = 拼音型態(字)
					if 拼音型態 == 臺灣閩南語羅馬字拼音:
						聲, 韻 = self.臺羅聲韻轉辨識合成型(臺羅拼音.聲, 臺羅拼音.韻)
					else:
						聲, 韻 = (臺羅拼音.聲, 臺羅拼音.韻)
					if 聲 != '' and 聲 != None:
						聲韻標籤.append(聲)
					if 臺羅拼音.音標==None:
						raise 解析錯誤('{0}：無著！！'.format(字))
					聲韻標籤.append(韻)
					調標仔.append(臺羅拼音.調)
		聲韻標籤.append(self.安靜符號)
		調標仔.append(self.安靜調)
		合成標籤 = [self.安靜標籤]
		這馬第幾標籤 = 1
		句攏總字數 = 臺羅音標.count(' ') + 臺羅音標.count('-') + 1
		句中第幾字 = 0
		for 詞 in 臺羅音標.split(' '):
			詞攏總字數 = 詞.count('-') + 1
			詞中第幾字 = 0
			for 字 in 詞.split('-'):
				臺羅拼音 = 拼音型態(字)
				if 拼音型態 == 臺灣閩南語羅馬字拼音:
					聲, 韻 = self.臺羅聲韻轉辨識合成型(臺羅拼音.聲, 臺羅拼音.韻)
				else:
					聲, 韻 = (臺羅拼音.聲, 臺羅拼音.韻)
				if 聲 != '' and 聲 != None:
					聲標籤 = self.產生合成標籤(聲韻標籤[這馬第幾標籤 - 1], 聲韻標籤[這馬第幾標籤], 聲韻標籤[這馬第幾標籤 + 1],
						調標仔[句中第幾字 - 1], 調標仔[句中第幾字], 調標仔[句中第幾字 + 1],
						詞中第幾字, 詞攏總字數, 句中第幾字, 句攏總字數)
					這馬第幾標籤 += 1
					合成標籤.append(聲標籤)
				韻標籤 = self.產生合成標籤(聲韻標籤[這馬第幾標籤 - 1], 聲韻標籤[這馬第幾標籤], 聲韻標籤[這馬第幾標籤 + 1],
					調標仔[句中第幾字 - 1], 調標仔[句中第幾字], 調標仔[句中第幾字 + 1],
					詞中第幾字, 詞攏總字數, 句中第幾字, 句攏總字數)
				這馬第幾標籤 += 1
				if 字=='sil':
					合成標籤.append(self.安靜標籤)
				else:
					合成標籤.append(韻標籤)
				詞中第幾字 += 1
				句中第幾字 += 1
		合成標籤.append(self.安靜標籤)
		return (合成標籤, 聲韻標籤)
	def 拼音轉合成標籤(self, 臺羅音標):
		return self.拼音轉合成標籤佮聲韻資料(臺羅音標)[0]
	def 拼音轉聲韻資料(self, 臺羅音標):
		return self.拼音轉合成標籤佮聲韻資料(臺羅音標)[1]
	def 臺羅聲韻轉辨識合成型(self, 聲, 韻):
		return 臺羅聲韻轉辨識合成型(聲, 韻)
	def 產生合成標籤(self, 前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞攏總字數, 句中第幾字, 句攏總字數):
		return '{0}-{1}+{2}/tiau3:{3}<{4}>{5}/su5:{6}!{7}@{8}/ku3:{9}^{10}_{11}'.format(
			前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞攏總字數 - 詞中第幾字, 詞攏總字數,
			句中第幾字, 句攏總字數 - 句中第幾字, 句攏總字數)


if __name__ == '__main__':
	合成標籤工具 = 句物件轉合成標籤()
	分析器 = 拆文分析器()
	# [我 gua2, 愛 ai3, 蔡 tshua3, 文 bun5, 莉 ni7, , ,]
	# [政 tsing3, 源 guan5, 足 tsiok4, 緣投 ian5-tau5, , ,]
	標籤 = 合成標籤工具.句物件轉標籤(臺灣閩南語羅馬字拼音,
		分析器.產生對齊句('gua1 ai2 tshua3-bun7-le7', 'gua2 ai3 tshua3-bun5-e7'))
# 	標籤=合成標籤工具.拼音轉合成標籤佮聲韻資料('tsing2-guan7 tsiok8 ian7-tau5')
# 	標籤=合成標籤工具.拼音轉合成標籤佮聲韻資料('lau3-pe7 bo7-si7-kan1')
# 	for 標籤 in 標籤[0]:
	print(標籤)
	標籤 = 合成標籤工具.句物件轉標籤(臺灣客家話拼音,
		分析器.產生對齊句('tienˊ-dangˋ labˋ-suiˋ','tienˊ-dangˋ labˋ-suiˋ'))
	print(標籤)
