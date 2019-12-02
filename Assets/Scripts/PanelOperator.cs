using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PanelOperator : MonoBehaviour
{
    //Script for opening and closing the pop-up window.

    public GameObject Panel;
   // public GameObject button;

    public void OpenPanel()
    {
        if(Panel != null)
        {
            Panel.SetActive(true);
          //  button.SetActive(true);
        }

    }

    public void ClosePanel()
    {
        if (Panel != null)
        {
            Panel.SetActive(false);

        }
    }
}
