# -*- coding: utf-8 -*-

# mayaのカメラをunityに持っていくため，
# unityの環境に準じたcameraのみのFBXをmaがあるディレクトリに出力する

import maya.cmds as cmds
import sys,os
sys.dont_write_bytecode = True

# 選択されたcameraがcameraかどうかチェック。
# cameraではない場合、nullを返す。
def checkCam():
    try:
        camShape =cmds.listRelatives(type="camera",s=True)[0]
        return camShape
    except TypeError as e:
        print e

# 選択されたcameraをセッティングする
# Film resolution gateをverticalに、focalLengthにkeyが打たれてなかったら1fr目にkeyを打つ
def settingCam(camShape):
    cmds.setAttr("%s.filmFit"%camShape ,2)
    FocallengthKeycount =cmds.keyframe(camShape,at='focalLength',q=True,kc=True )
    if FocallengthKeycount==0:
        cmds.setKeyframe(camShape,t=1,at='focalLength')



# ロケーターを作成し、選択されたcameraにpoint&orientでコンストする。
def createNull(camShape):
    loc =cmds.spaceLocator(p=(1, 1, 1),n="locator_Camera" )[0]
    camtrans =cmds.listRelatives(camShape,p=True)
    cmds.pointConstraint(camtrans,loc,offset=(0,0,0),weight=1)
    cmds.orientConstraint(camtrans,loc,offset=(0,0,0),weight=1)

# locatorのスケールXYZにエクスプレッションを仕込む。
def setExpression(camShape):
    loc =cmds.ls("locator_Camera")[0]
    expressionXString = "float $ncp;\n$ncp = `getAttr\n%s.nearClipPlane`;\nsetAttr %s.scaleX $ncp;"%(camShape,loc)
    cmds.expression(o=loc,s=expressionXString)
    expressionYString = "float $fcp;\n$fcp = `getAttr\n%s.farClipPlane`;\nsetAttr %s.scaleY $fcp;"%(camShape,loc)
    cmds.expression(o=loc,s=expressionYString)
    expressionZString="float $fl;\nfloat $vfa;\nfloat $FoV;\n\n$fl =`getAttr %s.focalLength`;\n$vfa = `getAttr %s.verticalFilmAperture`;\n\n$FoV =2.0 * atan((0.5*$vfa)/($fl*0.03937))*57.29578;\n\nsetAttr %s.scaleZ $FoV;"%(camShape,camShape,loc)
    cmds.expression(o=loc,s=expressionZString)


# ロケーターのtransとscaleをﾍﾞｲｸする。
def locatorBake():
    endTime =int(cmds.playbackOptions(query=1, maxTime=1))
    cmds.bakeResults( 'locator_Camera*', t=(1,endTime), simulation=True )

# コンストをbreakしてロケーターのみをmaファイルと同ディレクトリにFBXとして出力。
def exportFBX():
    fbxDir = cmds.file()
    cmds.delete("locator_Camera_pointConstraint1")
    cmds.delete("locator_Camera_orientConstraint1")

    maPath =cmds.file(q=1,expandName=1)
    Dirname=os.path.dirname(maPath)
    savePath =os.path.join(Dirname,"mayaCamera.fbx")
    cmds.file(savePath,force=True,options="v=0;",typ="FBX export",pr=True,es=True)

def main():
    camShape =checkCam()
    if camShape==None:
        print "=========================================="
        print "plese select camera"
        print "=========================================="
    if camShape!=None:
        settingCam(camShape)
        createNull(camShape)
        setExpression(camShape)
        locatorBake()
        exportFBX()
    pass
