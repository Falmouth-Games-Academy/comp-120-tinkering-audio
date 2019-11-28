using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;


/* Script written by Adrian Tofan

// The button audio manipulation script.
 Steven Yau's methods were used as a reference for this script. His GitHub repo can be found in the README file.

 */
public class ButtonSound : MonoBehaviour
{
    private AudioSource audioSource;
    private AudioClip outAudioClip;
    public int freq_click=300; // a higher pitch whenever the button is clicked.
    public int freq_hover = 200; // The frequency of key 'A'
    private Button button { get { return GetComponent<Button>(); } }

    // Start is called before the first frame update
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        
        

        audioSource.playOnAwake = false;
        button.onClick.AddListener(() => click_sound());
    }

    
    // This method is calling the 'CreateToneAudioClip' method with the specified frequency of the 'A' key note as a parameter.
    // That sound plays whenever the user's pointer is over the button.
    public void hover_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_hover);
        audioSource.PlayOneShot(outAudioClip);
    }

    // This method is calling the 'CreateToneAudioClip' method with the specified frequency of a higher pitch than the one for hovering over a button.
    // That sound plays whenever the user's pointer is clicking the button.
    public void click_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_click);
        PlayOutAudio();
    }

    // Public APIs
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


    // Private
    // The sample length was changed for a shorter time for the sound instead of using the sampleRate * sampleDurationSecs formula.
    private AudioClip CreateToneAudioClip(int frequency)
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
            samples[i] = v;
        }

        audioClip.SetData(samples, 0);
        return audioClip;
    }



}