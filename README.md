# Talker & Listener ROS 2
## robosys2023 mypkg
千葉工業大学 未来ロボティクス学科 2023年度 ロボットシステム学内で行った内容をROS 2パッケージにしたものです。

[![test](https://github.com/kentotutui/robosys2023_mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kentotutui/robosys2023_mypkg/actions/workflows/test.yml)

## テスト環境
  * Ubuntu 22.04 LTS

## ブランチの説明
  * master branch
    * lesson9の内容を除いた、lesson11までを実装したパッケージです。
    * talker・listenerをclassで記述しました。

  * lesson9 branch
    * lesson9の内容はブランチを分けています。

## トピックについて
  * master branch
    * master内で使われるトピック(countup)は、Int16型で整数を扱います。

## talkerの使い方
0.5秒ずつカウントアップしてトピック(countup)を送信するノードです。

単体で動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg talker
#画面には何も表示されません
```

## listenerの使い方
トピック(countup)を受信するノードです。

単体で動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 run mypkg listener
[INFO] [1703314540.253223410] [listener]: Listen: 0
[INFO] [1703314540.732753899] [listener]: Listen: 1
[INFO] [1703314541.231645432] [listener]: Listen: 2
・・・
```

## launchの使い方
talkerとlistenerを同時に動かせるようにしたファイルです。

動作させるときは以下のコマンドを打ち込んでください。

```shell
$ ros2 launch mypkg talk_listen.launch.py 
[listener-2] [INFO] [1703315431.311982248] [listener]: Listen: 0
[listener-2] [INFO] [1703315431.792204733] [listener]: Listen: 1
[listener-2] [INFO] [1703315432.292378318] [listener]: Listen: 2
・・・
```

## 著作権・ライセンス
  * このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
  * © 2023 Kento Tsutsui