# auto_lock

## これはなに？

人感センサーを使った鍵のオートロックを実現します。

- 人がいるのを検知すると鍵を開ける
- 人がいなくなったのを検知すると鍵を閉める

玄関と廊下との間に扉がある等、独立した玄関に人感センサーと Raspberry Pi を置くことを想定しています。

## 必要なもの

- Raspberry Pi
  - 手元で使ったのは Raspberry Pi 4 Computer Model B
- 人感センサー
  - 手元で使ったのは HiLetgo の HC-SR501
- ジャンプワイヤー (メス-メス) 3本
- Sesame
  - 手元で使ったのは Sesame mini
  
## 準備

Raspberry Pi の初期設定等は済んでいる前提です。

### Sesame の device_id と auth_token を取得

- auth_token
  - [CANDY HOUSE Dashboard](https://my.candyhouse.co/) から取得
  - 詳しくは [こちら](https://docs.candyhouse.co/#authentication)
- device_id
  - auth_token を取得して API が叩けるようになったら、 `GET /sesames` で取得
  - 詳しくは [こちら](https://docs.candyhouse.co/#sesame-api)

取得したら、`.env.sample` のファイル名を `.env` に書き換え、 `SESAME_AUTH_TOKEN`, `SESAME_DEVICE_ID` の値をそれぞれ書き換えます。

### Raspberry Pi と人感センサーの接続

#### 動作モードの変更

HC-SR501 はデフォルトで再検知しないモードになっているようなので、再検知するモード(検知エリア内に対象物がある間は検知出力が継続される)に切り替えます。
人がいるのを検知した後も再検知し続けてくれないと、まだ人がいるのに鍵が閉まるという挙動になってしまうためです。

画像左下の黄色いショートプラグを H 側に挿入することで再検知するモードに切り替わります。

再検知しないモード(L)

<img src="https://user-images.githubusercontent.com/34127161/87215303-5222fe80-c370-11ea-8080-c42dbce5f243.jpg" width="320px">

再検知するモード(H)

<img src="https://user-images.githubusercontent.com/34127161/87215311-6ebf3680-c370-11ea-879e-3ce10768dc85.jpg" width="320px">

### 配線

[こちらの記事](https://chasuke.com/motionsensor/) を丸っと参考にワイヤー3本を配線します。

`.env` の `GPIO_PIN` は、配線した GPIO PIN の番号に書き換えてください。(上の記事のとおりに配線した場合、書き換える必要はありません)

## 使い方

準備が整えば依存パッケージをインストールして、実行するだけです。

```
$ pipenv install
$ nohup pipenv run start &
```

pipenv がなければ事前に

```
$ pip install pipenv
```
