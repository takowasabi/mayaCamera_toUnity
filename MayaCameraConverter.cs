using UnityEngine;
using System.Collections;

//add Assets/Scripts

public class MayaCameraConverter : MonoBehaviour{
  Camera _camera;

  void Awake()
  {
  _camera = GetComponentInChildren<Camera>();
  }

 void LateUpdate()
 {
   _camera.nearClipPlane =transform.localScale.x;
   _camera.farClipPlane =transform.localScale.y;
   _camera.fieldOfView =transform.localScale.z;
 }
}
