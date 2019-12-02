using UnityEngine;
using System.Collections.Generic;
public class DynamicColourObject : MonoBehaviour
{
    public static List<GameObject> list = new List<GameObject>();
    void Start()
    {
        list.Add(gameObject);
    }
    void OnDestroy()
    {
        list.Remove(gameObject);
    }
}