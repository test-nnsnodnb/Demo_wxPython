# -*- encoding: utf-8 -*-
import wx
import time

# 円周率小数点以下
def ppii(n) :
  a , b , i = 10 ** n , 10 ** n , n * 8 + 1
  while i >= 3 :
      a , i = (a + b + b ) * ( i / 2 ) / i , i - 2
  return a - b

# CUI表示テキスト
#print "3."+str(ppii(100))

if __name__ == "__main__":
    # アプリケーションの初期化
    application = wx.App()

    # フレームの初期化
    frame = wx.Frame(None,wx.ID_ANY,"superπをwxPythonで作ってみる")

    # パネル作成
    panel = wx.Panel(frame,wx.ID_ANY)
    #panel.SetBackgroundColour("#AFAFAF")

    # 計算結果をresultに格納する
    start = time.time()

    result = wx.TextCtrl(panel , wx.ID_ANY , ("\n3." + str(ppii(1000)) + "\n"))

    elapsed_time = time.time() - start

    # resultへの書き込みを拒否
    result.Disable()

    # resultの表示についてのフォント調整
    result_font = wx.Font(14 , wx.FONTFAMILY_DEFAULT , wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_NORMAL)
    result.SetFont(result_font)


    st1 = wx.StaticText(panel, -1 , "計算終了")
    res = wx.StaticText(panel , -1 , "\n\n" + str(elapsed_time * 1000) + "ミリ秒")

    # レイアウト作成
    #layout = wx.BoxSizer(wx.VERTICAL)

    #panel.SetSizer(layout)

    # ステータスバー作成
    frame.CreateStatusBar()
    frame.SetStatusText("super_pi.appのディレクトリ内に結果ファイルを出力しました。")

    frame.Show()
    application.MainLoop()

    # ファイルへの書き出し
    f = open('result.txt' , 'w')
    f.write("3.\n" + str(ppii(1000)) + "\n")
    f.close()
