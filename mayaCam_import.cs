using UnityEngine;
using UnityEditor;

public class TestSelectedObject : Editor
{
    [MenuItem("SAPPTools/set_MayaCamera")]
    static void Create()
    {
			if (Selection.gameObjects.Length>1)
      EditorUtility.DisplayDialog("１つだけえらんで", "please select one cameraobject", "OK");
			Debug.Log("////////////////////////////////////////\nplease select one cameraobject");

			if (Selection.gameObjects.Length==1)
			if(NameCheck()=="mayaCamera")
			{
			GameObject mayaCam =Selection.gameObjects[0];
			GameObject mainCam = GameObject.Find("Main Camera");

			mainCam.transform.parent = Selection.activeTransform;
      setDefaultvalue();
      mayaCam.AddComponent<MayaCameraConverter>();
		}
    }

		static string NameCheck()
		{
			GameObject go;
			go=Selection.gameObjects[0];

			if(go.name!="mayaCamera")
      EditorUtility.DisplayDialog("ほかのえらんで", "please select mayaCamera", "OK");

			Debug.Log("////////////////////////////////////////\nplease select mayaCamera");
			return go.name;
		}


		static void setDefaultvalue(){
			GameObject mainCam = GameObject.Find("Main Camera");
      mainCam.transform.localPosition = Vector3.zero;
      mainCam.transform.localRotation = Quaternion.identity;
      mainCam.transform.localRotation = Quaternion.Euler(0,180,0);
      mainCam.transform.localScale = Vector3.one;
		}
}
