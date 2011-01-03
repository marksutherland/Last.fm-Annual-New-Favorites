# After coralling your last.fm stats into a dict called 'years' with the
# following structure, this code should allow you to generator a list of the
# artists you started listening to in each year. Less enlightening than I hoped.
#
# {2006:({'artist1' : n}, {'artist1' : n})}

for year in years:
    if year not in years2:
	years2[year] = dict()
    weeks = years[year]
    for week in weeks:
	print week
	for artist in week:
	    if artist in years2[year]:
		years2[year][artist] += week[artist]
	    else:
		years2[year][artist] = week[artist]

# {2006:{'artist1':n}, 2007:{'artist1':n}}

#get new artists for this year

new_artists = dict()
for year in sorted(years2.keys()):
    for artist in years2[year]:
	seen_artist = False
	for artist_year in new_artists:
	    if artist in new_artists[artist_year]:
		seen_artist = True
	if not seen_artist:
	    if year not in new_artists:
		new_artists[year] = {artist : years2[year][artist]}
	    else:
		new_artists[year][artist] = years2[year][artist]

new_artists_sorted = dict()
for year in new_artists:
    new_artists_sorted[year] = sorted(new_artists[year].iteritems(),
				      key=operator.itemgetter(1))
