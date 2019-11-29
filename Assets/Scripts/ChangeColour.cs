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
      
        // Get random colours for the button change option.
        red = Random.Range(0.0f, 3.0f);
        green = Random.Range(0.0f, 3.0f);
        blue = Random.Range(0.0f, 3.0f);


        
    }


    public void change_colour()
    {

        newColor = new Color(red, green, blue);

      
        //Change the colour of the buttons that have the DynamicColourObject script attached.

        foreach (GameObject dynamicColourObject in DynamicColourObject.list)
            dynamicColourObject.GetComponent<UnityEngine.UI.Image>().color = newColor;

    }
    
}
