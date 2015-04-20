# -*- encoding: utf-8 -*-
import wx
import time

N = 10000

# 円柱率小数点以下の算出
def ppii(n) :
	a , b , i = 10 ** n , 10 ** n , n * 8 + 1
	while i >= 3 :
		a , i = (a + b + b ) * (i / 2) / i , i - 2
	return a - b

# アプリケーションの初期化
app = wx.App()

# フレームの初期化
frame = wx.Frame(None , -1 , 'superπをwxPythonで作ってみる')

# パネル作成
panel = wx.Panel(frame , -1)

# ファイルへの書き出し
start = time.time()
f = open('result.txt' , 'w')
f.write('3.\n' + str(ppii(N)) + '\n')
f.close()
elapsed_time = time.time() - start

# 計算結果をresultに格納
#result = wx.TextCtrl(panel , -1 , ('3.' + str(ppii(1000)) + '\n'))
result = wx.StaticText(panel , -1 , ('3.' + str(ppii(40)) + '...\n'))

# resultへの書き込みを拒否
#result.Disable()

st1 = wx.StaticText(panel , -1 , '\n\n' + str(N) + '桁の計算終了\n')
res = wx.StaticText(panel , -1 , '\n\n\n' + str(elapsed_time * 100) + 'ミリ秒')

# レイアウト作成
layout = wx.BoxSizer(wx.VERTICAL)
panel.SetSizer(layout)

# ステータスバー作成
frame.CreateStatusBar()
frame.SetStatusText('super_pi.appと同ディレクトリ内に結果ファイルを出力しました。')

frame.Show()
app.MainLoop()