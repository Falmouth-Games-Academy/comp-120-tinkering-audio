using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;



/* Script written by Adrian Tofan for Tinkering Audio assignment.

 The button audio manipulation script.
 Steven Yau's 'CreateToneAudio' method was used as a reference for this script. His GitHub repo can be found in the README file. His method was modified in order to satisfy our needs.

 */
public class ButtonSound : MonoBehaviour
{
    private AudioSource audioSource;
    private AudioClip outAudioClip;
    public int freq_click=300;  //D4 key note
    public int freq_hover=200; // G3 key note
    public int newClick=300;
    public int newHover=200;
    private float volume;
    public float volume_multiplier=1f;
    private int A = 440;
    
   
    private Button button { get { return GetComponent<Button>(); } }


    




    // Start is called before the first frame update
    void Start()
    {
        
        audioSource = GetComponent<AudioSource>();
        audioSource.playOnAwake = false;
        button.onClick.AddListener(() => click_sound());
        setVolume();
        
   

    }

    //Updating the volume constantly to apply changes.
    void Update()
    {
        volume_multiplier = volume * volume_multiplier;
        freq_click = newClick;
        freq_hover = newHover;
    }

    // We set the start volume to 1.
    void setVolume()
    {
        volume = 1f;
    }
    
    //Increase the volume by 1 each time the designer clicks.
    public void increaseVolume()
    {
        volume_multiplier++;
    }

    //Dividing the current volume by 2 each time the designer scrolls. Would have used right click instead, but there is no such function in the 'Event trigger' component.
    public void decreaseVolume()
    {
        volume_multiplier=volume_multiplier/2;
    }

    /*Update the click frequency and hover frequency once a piano note is pressed.
     * I aimed to always have the frequency of 'freq_hover' 100hZ lower than 'freq_click' in order to have a diference between hovering and
     * clicking.
     * */

    public void updateFreq(double clickFreq)
    {
        newClick = (int)clickFreq;
        newHover = (int)clickFreq - 100;
    }


    //Converting notes to frequencies formula.
    public double noteFreq(int note_num)
    {
        return 440f * Math.Pow(2, note_num / 12f);
    }

    //Based on the number of the note, calculate the frequency based on the number of the key.
   public void keyA()
    {
        updateFreq(noteFreq(0));
    }

    public void keyB()
    {
        updateFreq(noteFreq(2));
    }

    public void keyC()
    {
        updateFreq(noteFreq(-9));
    }

    public void keyD()
    {
        updateFreq(noteFreq(-7));
    }

    public void keyE()
    {
        updateFreq(noteFreq(-5));
    }

    public void keyF()
    {
        updateFreq(noteFreq(-4));
    }

    public void keyG()
    {
        updateFreq(noteFreq(-2));
    }







    // This method is calling the 'CreateToneAudioClip' method with the specified frequency of the 'A' key note as a parameter.
    // That sound plays whenever the user's pointer is over the button.
    public void hover_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_hover, volume_multiplier);
        audioSource.PlayOneShot(outAudioClip);
    }

    // This method is calling the 'CreateToneAudioClip' method with the specified frequency of a higher pitch than the one for hovering over a button.
    // That sound plays whenever the user's pointer is clicking the button.
    public void click_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_click, volume_multiplier);
        PlayOutAudio();
    }

  
    //Method used to play audio.
    public void PlayOutAudio()
    {
        audioSource.PlayOneShot(outAudioClip);
    }

    //Method used to stop audio.
    public void StopAudio()
    {
        audioSource.Stop();
    }

    
    // The sample length was changed for a shorter time for the sound instead of using the sampleRate * sampleDurationSecs formula.
    private AudioClip CreateToneAudioClip(int frequency, float volume_multiplier)
    {
        int sampleDurationSecs = 1;
        int sampleRate = 44100;
        int sampleLength = 15000;
        float maxValue = 1f / 4f;

        var audioClip = AudioClip.Create("tone", sampleLength, 1, sampleRate, false);

        float[] samples = new float[sampleLength];
        for (var i = 0; i < sampleLength; i++)
        {
            float s = Mathf.Sin(2.0f * Mathf.PI * frequency * ((float)i / (float)sampleRate));
            float v = s * maxValue;
            samples[i] = v* volume_multiplier;
        }

        audioClip.SetData(samples, 0);
        return audioClip;
    }



}