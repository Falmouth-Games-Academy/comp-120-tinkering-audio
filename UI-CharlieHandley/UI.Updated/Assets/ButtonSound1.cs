using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

#if UNITY_EDITOR
using UnityEditor;
#endif
// used to generate the audio
public class ButtonSound1: MonoBehaviour
{
    private AudioSource audioSource;
    private AudioClip outAudioClip;
   
    public System.Random randomized = new System.Random();
    public int freq_click = 400;
    public int freq_hover = 200; 
    public float timer = 0f;
    private Button button { get { return GetComponent<Button>(); } }
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        audioSource.playOnAwake = false;
        button.onClick.AddListener(() => click_sound());
                audioSource.playOnAwake = false;

    }

    // Sound will play when hovering over it
    public void hover_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_hover);
        audioSource.PlayOneShot(outAudioClip);
    }

   
    public void click_sound()
    {
        outAudioClip = CreateToneAudioClip(freq_click);
        PlayOutAudio();
    }
    public void PlayOutAudio()
    {
        audioSource.PlayOneShot(outAudioClip);
    }
    public void StopAudio()
    {
        audioSource.Stop();
    }
    private AudioClip CreateToneAudioClip(int frequency)
    {
        
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