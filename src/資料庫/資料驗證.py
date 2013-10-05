from 資料庫.整合.整合入言語 import 用流水號揣文字
from 資料庫.整合.整合入言語 import 用流水號揣關係
from 資料庫.整合.整合入言語 import 用流水號揣演化
from 資料庫.欄位資訊 import 版本正常

class 結構測試(object):

	def __init__(self):
		pass
	
	def 編修檢查(self):
		全部編修資料 = []
		流水號種類對照表 = {}
		for 編修目標流水號, 資料種類, 版本, 結果 in 全部編修資料:
			if 編修目標流水號 in 流水號種類對照表:
				print("無應該有重覆的流水號:{0}".format(編修目標流水號))
			流水號種類對照表[編修目標流水號] = 資料種類
		for 編修目標流水號, 資料種類, 版本, 結果 in 全部編修資料:
			# 資料種類愛著
			# 結果佮本身愛仝一个種類
			
			if 資料種類 == '文字':
				目標資料 = 用流水號揣文字(編修目標流水號)
			elif 資料種類 == '關係':
				目標資料 = 用流水號揣關係(編修目標流水號)
			elif 資料種類 == '演化':
				目標資料 = 用流水號揣演化(編修目標流水號)
			else:
				目標資料 = None
			if 目標資料 == None:
				print("資料種類毋著:{0}，{1}".format(編修目標流水號, 資料種類))
			if 結果!=None:
				if 結果 not in 流水號種類對照表:
					print("結果編號毋記著:{0}，{1}，結果：{2}"
						.format(編修目標流水號, 資料種類, 結果))
				if 資料種類 != 流水號種類對照表[結果]:
					print("結果資料種類佮本身無合:{0}，{1}，結果：{2}，{3}"
						.format(編修目標流水號, 資料種類, 結果, 流水號種類對照表[結果]))
			if 版本!=版本正常:
				print("版本無正常，無定義:{0}"	.format(版本))
		# 閣愛檢查是毋是全部攏有佇編修內底
	
	def 文字基本檢查(self):
		# 閩南語有對齊無
		# 國語會使無音標，但是有音標嘛愛對齊
		# 無應該有--存在
		pass
	
	def 文字組合檢查(self):
		# 有字典拄仔匯出組合猶袂全好
		# 佮組過組點攏做好矣
		# 兩種攏愛檢查
		# 組合可能會參考關係
		pass
		
	def 關係詞性檢查(self):
		# 愛看有走出奇怪的詞性無
		pass
		
	def 關係演化流水號檢查(self):
		# 流水號攏愛是文字的（查編修就好矣）
		pass
