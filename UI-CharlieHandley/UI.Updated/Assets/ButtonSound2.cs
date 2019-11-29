using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player1 : MonoBehaviour
{
    private AudioSource a_source;
    public AudioClip[] a_clips;

    void Start()
    {
        a_source = gameObject.AddComponent<AudioSource>();
        //can also switch add to get if object already has an audio source
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
            PlayRandomSound();
    }

    public void PlayRandomSound()
    {
        int selection = Random.Range(0, a_clips.Length);
        a_source.PlayOneShot(a_clips[selection]);
    }
}