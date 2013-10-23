"""
Created on 2013/2/21

@author: Ihc
"""
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣主條目
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣義倒詞的詞音
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣義近詞的詞音
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣詞別音
from 資料庫.整合.教育部閩南語常用詞辭典 import 俗音記號
from 資料庫.整合.教育部閩南語常用詞辭典 import 合音記號
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣詞合音
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣詞俗音
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典空白符號
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣字方言差
from 資料庫.整合.教育部閩南語常用詞辭典 import 字方言差欄位
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣詞方言差
from 資料庫.整合.教育部閩南語常用詞辭典 import 詞方言差欄位
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典隔開符號
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 資料佮語料匯入整合.教育部臺灣閩南語常用詞辭典.造字處理 import 共造字換做統一碼表示法
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.欄位資訊 import 版本正常
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典地區
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典年代
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典名
from 資料庫.整合.整合入言語 import 揣文字上大流水號
from 資料庫.整合.教育部閩南語常用詞辭典 import 設定來源
from 資料庫.整合.整合入言語 import 加演化
from 資料庫.整合.整合入言語 import 加關係
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 會當替換
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 資料庫.欄位資訊 import 偏泉優勢音腔口
from 資料庫.欄位資訊 import 混合優勢音腔口

class 整合到文字():
	def __init__(self):
		初胚工具 = 文章初胚工具()
		分析器 = 拆文分析器()
		轉音家私 = 轉物件音家私()
		譀鏡 = 物件譀鏡()

		# {'--tsi̍t-kuá'}
		# 13602因
		音空 = {''}
		for 主編號, 屬性, 文字, 音標, 方言差 in 揣主條目(22168):
# 			print(主編號)
			if 屬性 == 25:
				種類 = '語句'
			else:
				種類 = '字詞'
			腔口集 = {}
			腔口集[偏漳優勢音腔口] = {}
			腔口集[偏泉優勢音腔口] = {}
			腔口集[混合優勢音腔口] = {}

			主音 = {音標} | { 音[0] for 音 in 揣義倒詞的詞音(主編號)} | { 音[0] for 音 in 揣義近詞的詞音(主編號)} | { 音[0] for 音 in 揣詞別音(主編號)}
			俗音 = { 音[0] + 俗音記號 for 音 in 揣詞俗音(主編號)}
			合音 = { 音[0] + 合音記號 for 音 in 揣詞合音(主編號)}
			主音 |= 俗音
			主音 |= 合音
			主音 -= 音空
# 			print(主音)
			if 主音 == {'Si̍k-tsí(Si̍p-tsí)'}:
				主音 = {'Si̍k-tsí', 'Si̍p-tsí'}
			for 音 in 主音:
				if 文字 not in 腔口集[偏漳優勢音腔口]:
					腔口集[偏漳優勢音腔口][文字] = []
				if 文字 not in 腔口集[偏泉優勢音腔口]:
					腔口集[偏泉優勢音腔口][文字] = []
				if 文字 not in 腔口集[混合優勢音腔口]:
					腔口集[混合優勢音腔口][文字] = []
				if 音 == 'tsánn-tiū-á-bué/bé':
					音 = 'tsánn-tiū-á-bué/tsánn-tiū-á-bé'
				雙優勢音 = 音.split('/')
				if 音 == 'ke/kue-tshíng' and 主編號 == 12744 and len(主音) > 1:
					continue
				if 音 == 'Jû/Lû/Jî':
					腔口集[偏漳優勢音腔口][文字].append(雙優勢音[2])
					腔口集[偏泉優勢音腔口][文字].append(雙優勢音[0])
					腔口集[偏泉優勢音腔口][文字].append(雙優勢音[1])
					continue
				if len(雙優勢音) == 1:
					雙優勢音.append(雙優勢音[0])
# 				print(雙優勢音)
				偏漳優勢音, 偏泉優勢音 = [優勢音.strip(教育部閩南語辭典空白符號) \
					for 優勢音 in 雙優勢音]
				混合優勢音 = None
				if 偏漳優勢音 == 偏泉優勢音:
					混合優勢音 = 偏漳優勢音
		# 		print(文字)
# 				print(偏漳優勢音,偏泉優勢音,混合優勢音)
				if 文字 == '竿(菅)蓁林':
					腔口集[偏漳優勢音腔口]['竿蓁林'] = [偏漳優勢音]
					腔口集[偏泉優勢音腔口]['竿蓁林'] = [偏泉優勢音]
					腔口集[偏漳優勢音腔口]['菅蓁林'] = [偏漳優勢音]
					腔口集[偏泉優勢音腔口]['菅蓁林'] = [偏泉優勢音]
					if 混合優勢音 != None:
						腔口集[混合優勢音腔口]['竿蓁林'] = [混合優勢音]
						腔口集[混合優勢音腔口]['菅蓁林'] = [混合優勢音]
					文字 = '竿蓁林'
				elif 文字 == '苓仔寮、能雅寮':
					腔口集[偏漳優勢音腔口]['苓仔寮'] = [偏漳優勢音]
					腔口集[偏泉優勢音腔口]['苓仔寮'] = [偏泉優勢音]
					腔口集[偏漳優勢音腔口]['能雅寮'] = [偏漳優勢音]
					腔口集[偏泉優勢音腔口]['能雅寮'] = [偏泉優勢音]
					if 混合優勢音 != None:
						腔口集[混合優勢音腔口]['苓仔寮'] = [混合優勢音]
						腔口集[混合優勢音腔口]['能雅寮'] = [混合優勢音]
					文字 = '苓仔寮'
				else:
					腔口集[偏漳優勢音腔口][文字].append(偏漳優勢音)
					腔口集[偏泉優勢音腔口][文字].append(偏泉優勢音)
					if 混合優勢音 != None:
						腔口集[混合優勢音腔口][文字].append(混合優勢音)

# 			print(腔口集)
			if len(方言差) == 6 and 主編號 != 6089:
				# "主編號"=12239
				字方言差 = list(揣字方言差(方言差)[0])[3:]
				for i in range(len(字方言差欄位)):
					if 字方言差[i] != 'x' and 字方言差[i] != '暫無資料':
						腔口集[字方言差欄位[i]] = {}
						腔口集[字方言差欄位[i]][文字] = [ 方言.strip(教育部閩南語辭典空白符號) for 方言 in 字方言差[i].split(';')]
			elif len(方言差) == 8:
				# "主編號"=4368
				詞方言差 = list(揣詞方言差(方言差)[0])[3:]
				for i in range(len(詞方言差欄位)):
					if 詞方言差[i].strip() != 'x' and 詞方言差[i].strip() != '暫無資料':
						if 詞方言差[i] == '菅芒　kuann-bang, kuann-bâng':
							詞方言差[i] = '菅芒　kuann-bang; kuann-bâng'
						elif 主編號 == 2876:
							詞方言差[i] = 詞方言差[i].replace('tuē', 'tuē; tueh')
# 						print(詞方言差[i])
						字音集 = [一組字音.split(教育部閩南語辭典隔開符號, 1) for 一組字音 in 詞方言差[i].split(',')]
						字音對照 = {}
# 						print(字音集)
						for 字, 音 in 字音集:
							字音對照[字.strip(教育部閩南語辭典空白符號)] = [資料.strip(教育部閩南語辭典空白符號) for 資料 in 音.split(';')]
		# 				print(字音對照)
						腔口集[詞方言差欄位[i]] = 字音對照
# 			print(腔口集)
			流水號集 = []
			for 腔口, 字音 in 腔口集.items():
				for 字, 音集 in 字音.items():
					原本音流水號集 = []
					俗音流水號集 = []
					合音流水號集 = []
					組字式型 = 共造字換做統一碼表示法(字)
					#組字式型 = 初胚工具.符號邊仔加空白(組字式型).strip()
					for 音 in 音集:
						是俗音 = False
						是合音 = False
						print('前',主編號,腔口, 組字式型, 音)
						if 組字式型=='熟' and 音=='tînn-kha-puānn-tshiú':
							continue
						資料字型體 = 組字式型
						if 音 == "sai-kong-á (面稱)":
							音 = "sai-kong-á"
						elif 音 == "sai-sun-á (背稱)":
							音 = "sai-sun-á"
						elif 音 == "khioh-gín-á(產婆語)":
							音 = "khioh-gín-á"
						elif 音 == "tshâ-se(大)":
							音 = "tshâ-se"
						elif 音 == "luai̍h-á(小)":
							音 = "luai̍h-á"
						elif 音 == "hông-hun(書)":
							音 = "hông-hun"
						elif 音 == 'tsînn(中間有孔)':
							音 = 'tsînn'  # 鐳　lui (無空的)
						elif 音 == 'tshâ-se(大)':
							音 = 'tshâ-se'
						elif 音 == 'luai̍h-á(小)':
							音 = 'luai̍h-á'
						if 資料字型體 == "司孫(背稱)":
							資料字型體 = "司孫"

						if 資料字型體 == "竹圍" and 主編號 == 36014:
							資料字型體 = "竹圍仔"
						elif 資料字型體 == "石牌" and 主編號 == 36021:
							資料字型體 = "石牌仔"
						elif 資料字型體 == "拔林" and 主編號 == 34058:
							資料字型體 = "拔仔林"
						elif 資料字型體 == "蓮蕉花" and 音 == 'lân-tsiau' and 主編號 == 11353:
							資料字型體 = "蓮蕉"
						elif 資料字型體 == "瘦田" and 主編號 == 60344:
							資料字型體 = "瘦田𠢕欶水。"
						elif 資料字型體 == "䆀猴" and 主編號 == 60373:
							資料字型體 = "䆀猴𠢕欠數。"

						elif 音 == "bé" and 主編號 == 60373:
							音 = "tsánn-tiū-á-bé"
						elif 音 == "䆀猴" and 主編號 == 60373:
							音 = "䆀猴𠢕欠數。"
						elif 音 == "䆀猴" and 主編號 == 60373:
							音 = "䆀猴𠢕欠數。"

						# m7 tioh8
						if 組字式型 == 'xx姊仔' and 音 == 'xxtsé--á':
							資料字型體 = '姊仔'
							音 = 'tsé--á'
						if 音 == "niàu-ka-tsiah hit- ki":
							# love you~
							音 = "niàu-ka-tsiah hit-ki"
						型替換 = {'收瀾收予焦，予你生一个有':'收瀾收予焦，予你生一个有𡳞脬。'
							}

						if 組字式型 in 型替換:
							資料字型體 = 型替換[組字式型]
						im1the3uan7 = {'oo- liông':'oo-liông', 'guán(男)':'guán', 'gún(女)':'gún',
							'tsié-hu':'tsé-hu',
							'Tuā ba̍k sin-niû, bô khuànn-kìnn tsàu.':'Tuā ba̍k sin-niû bô khuànn-kìnn tsàu.',
							'Tshiú-khiau, khut-ji̍p, bô khut-tshut.':'Tshiú-khiau, khut-ji̍p bô khut-tshut.',
							'Tsīn jîn-sū sūn thinn-ì.':'Tsīn jîn-sū , sūn thinn-ì.',
							'Hè-sen-ná':'Hè-sian-ná',
							'jua̍h-- tio̍h':'jua̍h--tio̍h', 'lua̍h-- tio̍h':'lua̍h--tio̍h',
							'sh-á':'ah-á', 'óonn-káu':'ónn-káu',
							}
						if 音 in im1the3uan7:
							音 = im1the3uan7[音]
# 						if 組字式型 in 腔口集[偏漳優勢音腔口]:
# 							print(音 in 腔口集[偏漳優勢音腔口][組字式型])
# 							print((音+合音記號) in 腔口集[偏漳優勢音腔口][組字式型])
# 							print( 腔口集[偏漳優勢音腔口][組字式型])
						if 音.endswith(俗音記號):
							是俗音 = True
							音 = 音[:-len(俗音記號)]
						elif 音.endswith(合音記號):
							音 = 音[:-len(合音記號)]
						合音字表 = {('下昏暗', 'ing-àm'), ('下昏暗時', 'ing-àm-sî'), ('下昏時', 'ing-sî'),
							('下昏', 'i̋ng'), ('這陣', 'tsín'), ('這陣', 'tsún'),
							('佗位', 'tuē'), ('佗位', 'tueh'), ('嘿啦', 'hiàu'),
							('查某𡢃', 'tsőo-kán'), ('查某𡢃仔', 'tsőo-kán-á'),
							('查某囡仔', 'tsa̋-gín-á'), ('查某囡仔', 'tsa̋u-gín-á'),
							('查某孫', 'tsa̋u-sun'),

							('啥物人', 'siàng-n̂g'), ('啥物人', 'sáng-n̂g'), }
						if  (組字式型 in 腔口集[偏漳優勢音腔口] and (音 + 合音記號) in 腔口集[偏漳優勢音腔口][組字式型]) or \
							((組字式型, 音) in 合音字表):
							是合音 = True
						if 是合音:
							if 主編號 == 9440:  # 嫁查甫囝
								資料字型體 = 組字式型[:1] + '⿰' + 組字式型[1:]
							elif 主編號 == 8331 and '-' not in 音:  # tsua̋n
								資料字型體 = '⿰⿰' + 組字式型
							elif 主編號 == 5923 and '-' not in 音:  # tsha̋u
								資料字型體 = '⿰⿰' + 組字式型
							else:
								資料字型體 = '⿰' + 組字式型
						第二三字組合 = {('硩落去', 'teh--loih'), ('硩落去', 'teh--loi'),
							('嫁查某囝', 'kè-tsőo-kiánn'), ('嫁查某囝', 'kè-tsa̋u-kiánn'),
							('嫁查某囝', 'kè-tsőo-kiánn'), ('嫁查某囝', 'kè-tsa̋u-kánn'),
							}
						if ((組字式型, 音) in 第二三字組合):
							資料字型體 = 組字式型[:1] + '⿰' + 組字式型[1:]
						if (組字式型, 音) in {('阮厝的查某人', 'gún-tshù-ê-tsa̋u-lâng')}:
							資料字型體 = 組字式型.replace('查某', '⿰查某')
						日語替換 = {
							(10740, 'ロ—ス'):'⿰ロ—ス',
							(1114, 'メンス'):'⿰メンス',
							(1632, 'はしか'):'はしか',
							(1736, 'ブラジゃ—'):'ブラ⿰ジゃ—',
							(2041, 'ステンレス'):'ス⿰テンレス',
							(2572, 'レコード'):'レ⿰コード',
							(2731, 'じどうしゃ'):'じ⿰どうしゃ',
							(2993, 'じしゃく'):'じしゃく',
							(3085, 'おニンギョウ'):'お⿰ニンギョウ',
							(3087, 'まんが'):'⿰まんが',
							(3436, 'ロ—ス'):'⿰ロ—ス',
							(3524, 'みそ'):'みそ',
							(4467, 'わさび'):'わさび',
							(4574, 'とうさん'):'⿰とうさん',
							(5106, 'トマト'):'トマト',
							(5437, 'にんじん'):'⿰にん⿰じん',
							(6043, 'ホテル'):'ホテル',
							(6088, 'ホテル'):'ホテル',
							(6590, 'ガラ油'):'ガラ油',
							(6848, 'ミシン'):'ミシン',
							(7561, 'スリッパ'):'スリッパ',
							(7561, 'ぞうり仔'):'⿰ぞうり仔',
							(8124, 'ビル'):'ビル',
							(8124, 'ビ—ル'):'⿰ビ—ル',
							(8164, 'パチンコ'):'パ⿰チンコ',
							(8727, 'ガラ油'):'ガラ油',
							(9928, 'コレラ'):'コレラ',
							(10927, 'アルミ'):'アルミ',
							(10965, 'ネクタイ'):'ネク⿰タイ',
							(11252, 'ロ—ス'):'⿰ロ—ス',
							(11988, 'ステンレス'):'ス⿰テンレス',
							(12555, 'はしか'):'はしか',
							(13055, 'りんご'):'⿰りんご',
							(13091, 'パン'):'⿰パン',
							(25750, 'ながし'):'ながし',
							}
						if (主編號, 組字式型) in 日語替換:
							資料字型體 = 日語替換[(主編號, 組字式型)]
							音 = 音.replace('33', '7')
							音 = 音.replace('55', '1')
							音 = 音.replace('11', '3')
							音 = 音.replace('51', '2')
							音 = 音.replace('35', '5')
							音 = 音.replace('t5', 't8')
							音 = 音.replace('t3', 't4')
							音 = 音.replace('h3', 'h4')
							音 = '1' + 音.replace('-', '-1')
							
						print('後',主編號, 組字式型, 音)
		# 				print(腔口 + ' ' + 共造字換做統一碼表示法(字) + ' ' + str(解析器.解析語句佮顯示毋著字元(音)))
						音 = 初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音)
						音 = 初胚工具.符號邊仔加空白(音).strip()
						地區對應 = {'鹿港':偏泉優勢音腔口, '三峽':偏泉優勢音腔口, '臺北':偏泉優勢音腔口,
							'宜蘭':偏漳優勢音腔口, '臺南':混合優勢音腔口, '高雄':混合優勢音腔口, '金門':偏泉優勢音腔口,
							'馬公':偏泉優勢音腔口, '新竹':偏泉優勢音腔口, '臺中':偏漳優勢音腔口, }
						所在地區 = 教育部閩南語辭典地區
						for 對應地區, 對應腔口 in 地區對應.items():
							if 對應地區 in 腔口:
								腔口 = 對應腔口
								所在地區 = 對應地區
						if 腔口 not in {偏泉優勢音腔口, 偏漳優勢音腔口, 混合優勢音腔口}:
							raise RuntimeError('腔口無著！！{0}'.format(腔口))
# 						print(字方言差欄位)
						if True:
# 						try:
							原音句物件 = 分析器.產生對齊句(資料字型體, 音)
							上尾句物件 = 轉音家私.轉做標準音標(臺灣閩南語羅馬字拼音, 原音句物件)

							print(教育部閩南語辭典名, 種類, 腔口, 所在地區, 教育部閩南語辭典年代,
								譀鏡.看型(上尾句物件), 譀鏡.看音(上尾句物件), 版本正常)
# 							加文字佮版本(教育部閩南語辭典名, 種類, 腔口, 所在地區, 教育部閩南語辭典年代,
# 								譀鏡.看型(上尾句物件), 譀鏡.看音(上尾句物件), 版本正常)
# 						except:
# 							print(主編號, 組字式型, 音)

						流水號 = 揣文字上大流水號()
		# 				print("流水號＝" + str(流水號))
						流水號集.append(流水號)
						設定來源(流水號, 主編號)
						if 是俗音:
							俗音流水號集.append(流水號)
						elif 是合音:
							合音流水號集.append(流水號)
# 							設定合音遏袂處理(流水號)
						else:
							原本音流水號集.append(流水號)
					# 5923 and 4000
					for 原本音流水號 in 原本音流水號集:
						for 俗音流水號 in 俗音流水號集:
							加演化(原本音流水號, 俗音流水號, '俗音')
					for 原本音流水號 in 原本音流水號集:
						for 合音流水號 in 合音流水號集:
							加演化(原本音流水號, 合音流水號, '合音')
			while len(流水號集) > 0:
				頭前流水號, *流水號集 = 流水號集
				for 後壁流水號 in 流水號集:
					加關係(頭前流水號, 後壁流水號, 義近, 會當替換)
					加關係(後壁流水號, 頭前流水號, 義近, 會當替換)

if __name__ == '__main__':
	整合到文字()
