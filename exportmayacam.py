# -*- coding: utf-8 -*-

# mayaのカメラをunityに持っていくため，
# unityの環境に準じたcameraのみのFBXをmaがあるディレクトリに出力する

import maya.cmds as cmds

# 選択されたcameraがcameraかどうかチェック。
# cameraではない場合、nullを返す。
def checkCam():
    pass

# 選択されたcameraをセッティングする
# Film resolution gateをverticalに、
# Focal lengthにキーが打たれているかチェック。
# angle of view にキーが打たれていないかチェック。
# （unityに持っていけないため）
def settingCam():
    pass


# ロケーターを作成し、選択されたcameraにpoint&orientでコンストする。
def createNull():
    pass

# locatorのスケールXYZにエクスプレッションを仕込む。
def setExpression():
    pass


# ロケーターのtransとscaleをﾍﾞｲｸする。
def locatorBake():
    pass


# コンストをbreakしてロケーターのみをmaファイルと同ディレクトリにFBXとして出力。
def exportFBX():
    pass
