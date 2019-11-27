using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//using System;


public class ChangeColour : MonoBehaviour
{
   
    private System.Random randomized = new System.Random();
    private float red;
    private float green;
    private float blue;
    private float divisor;
    Color newColor;
    

    void Update()
    {
        // divisor = Convert.ToInt32(randomized.Next(2, 5));
        red = Random.Range(0.0f, 3.0f);
        green = Random.Range(0.0f, 3.0f);
        blue = Random.Range(0.0f, 3.0f);


        //Convert.ToSingle(randomized.Next(0, 1));
    }


    public void change_colour()
    {

        newColor = new Color(red, green, blue);

        //GetComponent<UnityEngine.UI.Image>().color = Color.green;

        /* foreach (GameObject dynamicColourObject in DynamicColourObject.list)
             dynamicColourObject.GetComponent<UnityEngine.UI.Image>().color = Color.green;
             */

        foreach (GameObject dynamicColourObject in DynamicColourObject.list)
            dynamicColourObject.GetComponent<UnityEngine.UI.Image>().color = newColor;

    }
    
}
