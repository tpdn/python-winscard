python-winscard
===============

winscard.dll wrapper using ctypes

## 使い方の例
*※カードリーダーを１台接続していると仮定*

import winscard

sc = winscard.SCard()

readers = sc.list_readers() #カードリーダーを扱うためのインスタンスのリストが入る

r = readers[0] #１台なので

r.connect()

\# card IDを取得するためのAPDUコマンドを送信する。
\# 結果はint(0～255)のリストで帰ってくる。

cardid = reader.transmit((0xFF, 0xCA, 0x00, 0x00, 0x00), winscard.SCARD_PCI_T1)

print [hex(x) in cardid]

## 制限
* 現在仕様が未確定な部分が多い
    * 基本的にはなるべく高水準なライブラリにするつもりで考えている。低水準な操作ができるのはすでにいろいろあるし。
* 未実装部分がある
    * 特に、SCardGetStatusChangeにあたるものが実装されていないのが問題。whileループで頭の悪いポーリングをやるハメになる。

## 今後
* スマートカード遊び？を楽しく行う方向で実装を進める
* 仕様が固まったらPyPIへ登録
* リーダーが複数台ある環境でのテストができていないのでそのうち行う