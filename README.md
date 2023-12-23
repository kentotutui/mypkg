# Talker & Listener ROS 2
## robosys2023 mypkg
千葉工業大学 未来ロボティクス学科 2023年度 ロボットシステム学内で行った内容をROS 2パッケージにしたものです。

[![test](https://github.com/kentotutui/robosys2023_ROS-2/actions/workflows/test.yml/badge.svg)](https://github.com/kentotutui/robosys2023_ROS-2/actions/workflows/test.yml)

## テスト環境
  * Ubuntu 22.04 LTS

## ブランチの説明
  * master
    * lessen9の内容を除いた、lessen11までを実装したパッケージです。
    * talker・listenerをclassで記述しました。

  * lessen9
    * 講義内で独自のメッセージ型を作成しました。
    * 独自のメッセージ型(Person)は、`name`と`age`を送受信します。
    * パッケージは、リポジトリを分けて置いてあります。([こちら](https://github.com/kentotutui/person_msgs))

## talkerの使い方
0.5秒ずつカウントアップしてトピック(countup)を通じて送信するノードです。

単体で動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg talker
```

## listenerの使い方
トピック(countup)を受信するノードです。

単体で動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg listener
```

## launchの使い方
talkerとlistenerを同時に動かせるようにしたファイルです。

動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 launch mypkg talk_listen.launch.py 
```


## 著作権・ライセンス
  * このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
  * © 2023 Kento Tsutsui