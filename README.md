# YahooMusic_Python
Yahoo Music recommendation system using python

For all the Python code, place data under "RawData" folder.
Create "Data" folder to store modified data, "Result" to store result.

1.g_Hierarchy.py

	Generate hierarchy structure for a list of track items.

2.g_TrainClass.py

	Generate the classification of each training entity. Label track as 1, album as 2, artist as 3, and genre as 4.
For example:
UserID|RatingCount
TrackID|Rating|1
ArtistID|Rating|3
GenreID|Rating|4
AlbumID|Rating|2

3.gscore_Hie.py
	
	Generate ratings for all the item in the hierarchy structure.

4.g_TrainMean.py

	Generate mean of each user's ratings.

The Following program require numpy.
