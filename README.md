# ロボットシステム学2017 課題1

## 動作の説明

ロボットシステム学2017の課題2で、ROSを用いたボトル検出を行いました。

以下のように動作しています。

- GPU搭載マシンで!(YOLO)[https://pjreddie.com/darknet/yolo/]を用いてボトルを検出
- 検出したオブジェクトの数ををpublish
- Raspberry Piで検出したオブジェクトの数をsubscribe
- 何かしらを検出していればLEDを点灯させる

YOLOをリアルタイムで動作させるのにあたり処理能力が必要であったのでGPUを搭載したマシンで動かしました。

YOLOは[公開](https://github.com/leggedrobotics/darknet_ros)されているROS版の実装を使用しました。

使用した重みはYOLOの作者が公開している学習済みのものです。[重み](http://pjreddie.com/media/files/yolo-voc.weights)

LEDを点灯する低レベルな制御はRaspberry Piの得意なことであるのでYOLOを動作させているマシンと同じLANにRaspberry Piを接続しました。

Raspberry PiでGPIOを動作させるのにWiringPiを使用しました。

`roscore`はGPU搭載マシンで動かし、Raspberry Piはネットワーク越しにROSのノードを接続して動作しています。

## デモムービー

https://www.youtube.com/watch?v=6AreTU5fd1U

## ライセンス

MIT License

Copyright (c) 2018 Satoshi Shimada

## 作成者

Satoshi Shimada (@satoshishimada)

