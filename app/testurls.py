from genre import getInfoBox

urls = ['http://en.wikipedia.org/wiki/Pretty_Little_Liars_(TV_series)',
'http://en.wikipedia.org/wiki/The_big_bang_theory',
'http://en.wikipedia.org/wiki/Good_Wife',
'http://en.wikipedia.org/wiki/Doctor_Who http://en.wikipedia.org/wiki/The_big_bang_teory',
'http://en.wikipedia.org/wiki/Elementary_(TV_series)',
'http://en.wikipedia.org/wiki/Orange_Is_the_New_Black',
'http://en.wikipedia.org/wiki/New_Girl_(TV_series)',
'http://en.wikipedia.org/wiki/Benjamin_Franklin_(TV_miniseries)',
'http://en.wikipedia.org/wiki/Sesame_Street',
' http://en.wikipedia.org/TheBigBangTheor',
'http://en.wikipedia.org/wiki/Family_Guy',
'http://en.wikipedia.org/wiki/Freaks_and_Geeks',
'http://en.wikipedia.org/wiki/Full_House',
'http://en.wikipedia.org/wiki/CSI:_Crime_Scene_Investigation',
'http://en.wikipedia.org/wiki/Big_Brother_(TV_series)',
'http://en.wikipedia.org/TheBigBangTheor']



for u in urls:
	print '\n' + u
	print getInfoBox(u)
