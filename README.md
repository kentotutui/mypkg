# Talker & Listener ROS 2 (lesson9)

## robosys2023 ros2
千葉工業大学 未来ロボティクス学科 2023年度 ロボットシステム学内で行ったlesson9までの内容をROS 2パッケージにしたものです。


## テスト環境
  * Ubuntu 22.04 LTS

## ブランチの説明
  * lesson9 branch
    * 講義内で独自のメッセージ型を作成しました。
    * 独自のメッセージ型(Query)は、`name`と`age`を送受信します。
    * Query型の定義ファイルは、リポジトリを分けて置いてあります。([こちら](https://github.com/kentotutui/person_msgs))

## トピックについて
  * lesson9 branch
    * lesson9内で使われるトピック(query)は、string型とuint8型を扱います。

## talkerの使い方
Query型のトピックを送信するノードです。

動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg talker
#画面には何も表示されません
```

## listenerの使い方
トピック(query)を受信するノードです。

動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg listener
[INFO] [1703340715.167159511] [listener]: age: 20
```

## launchの使い方
talkerとlistenerを同時に動かせるようにしたノードです。

動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 launch mypkg talk_listen.launch.py
[listener-2] [INFO] [1703325539.355998965] [listener]: age: 20
```

## 著作権・ライセンス
  * このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
  * © 2023 Kento Tsutsui