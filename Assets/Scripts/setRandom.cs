using System.Collections;
using System.Collections.Generic;
using UnityEngine;


namespace randomFrequency
{
    public class setRandom
    {
        public int freq_click;  //277-311 (D note) a higher pitch whenever the button is clicked.300
        public int freq_hover;
        

        void Awake()
        {
            
            freq_click = UnityEngine.Random.Range(290, 311);
            freq_hover = UnityEngine.Random.Range(190, 207);
        }

        public int getRandomClick()
        {
            return freq_click;
        }

        public int getRandomHover()
        {
            return freq_hover;
        }
    }
}
