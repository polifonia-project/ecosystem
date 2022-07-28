# Similarities Pairs

In the folder [split_global](https://github.com/polifonia-project/harmonic-similarity/tree/main/similarities/split_global) you can find more than 400 files, each of which containing 15 similarity pairs. 

The files are all ```.xlsx``` and their structure is the following:

![Screenshot 2021-10-07 at 20 03 14](https://user-images.githubusercontent.com/44606182/136439284-73e9b792-4d41-4dbb-ad1d-00c154514c78.png)

* ```track_1``` and ```track_2``` columns: contain the id of the two tracks among which the similarity was calculated;

* ```pattern_track_1``` and ```pattern_track_2``` columns: contain the longest harmonic sequence that the two tracks have in common. If there are more than one longest sequence in common they are represented in different comma separated lists;

* ```time_pattern_track_1``` and ```time_pattern_track_2``` columns: contain the time information about the longest harmonic sequence that the two tracks have in common. For each common sequence the time information is described as a tuple composed as follows ```(start_time, end_time)```. Both the time stamps are formatted as ```h:mm:ss:mmmmmmm```;

*  ```sonification_pattern_track_1``` and ```sonification_pattern_track_2``` columns: contain the link to the audio file (hosted on [SoundCloud](https://soundcloud.com/)) of the track's chords sonification. The links lead to the exact timestamp where the different patterns start within the audio track;

*  ```spotify_uri_track_1``` and ```spotify_uri_track_2``` columns: contain URI to the respective tracks on the [Spotify](https://spotify.com) streaming platform. To listen to the track, simply copy and paste the uri into your browser address bar. To listen to the common patterns, you must manually position yourself at the timestamp indicated in the ``time_pattern_track`` column. Tracks that do not have a Spotify URI can be searched for on any music streaming service: however, in this case, the accuracy of the timestamps provided is NOT guaranteed.


## Criteria for populating the split files

The files containd in the [split_global](https://github.com/polifonia-project/harmonic-similarity/tree/main/similarities/split_global) folder were populated according to the following criteria:

* similarities are not calculated between tracks with the same name;
* similarities are not calculated between tracks of the same author;
* there are no inverse similarities within the same file (if similarity is calculated between x and y it will not be calculated between y and x);
* the similarity values have been hidden to avoid biased ratings.

