import fresh_tomatoes
import media

leader = media.Movie("Leader", "about young politician", "http://www.tirakita.com/Movie_VCD_DVD2/BD/Photos/bd_20b.jpg", "https://www.youtube.com/watch?v=ddAAjFJBeZM")
#print(leader.title)

titanic = media.Movie("Titanic", "The journey of Titanic begins in the present, at the site of the ship's watery grave, two-and-a-half miles under the ocean surface. An ambitious fortune hunter (Bill Paxton) is determined to plumb the treasures of this once-stately ship, only to bring to the surface a story left untold", "http://2.bp.blogspot.com/-eCYb5Qi7dwU/VT0TTXB811I/AAAAAAAAArQ/WANnu2tatW0/s1600/titanic.24590.jpg", "https://www.youtube.com/watch?v=kVrqfYjkTdQ")

rang_de_basanti = media.Movie("Rang De Basanti", "The story is about a British documentary filmmaker who is determined to make a film on Indian freedom fighters based on diary entries by her grandfather, a former officer of the Indian Imperial Police. Upon arriving in India, she asks a group of five young men to act in her film.", "http://www.impawards.com/intl/india/2006/posters/rang_de_basanti_ver2_xlg.jpg", "https://www.youtube.com/watch?v=Dms-mPxc1SU")
#basha = media.Movie("Basha","story about gangster", "https://i.ytimg.com/vi/BRE-WI6nQOs/maxresdefault.jpg", "https://www.youtube.com/watch?v=UK6BCUThq34")
#print(basha.storyline)

avatar = media.Movie("Avatar", "Avatar is the story of an ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

sankarabharanam = media.Movie("Sankarabharanam","Musical Drama","http://4.bp.blogspot.com/-Plm9V4y9VOY/Vc6wyTm81QI/AAAAAAAABLg/CP42w2XQcF4/s640/chaganti%2Bgaru%2Bon%2Bsankarabharanam.png","https://www.youtube.com/watch?v=d-0ZcoBnhoQ")

chak_de_india = media.Movie("Chak De India", "It explores religious bigotry, the legacy of the partition of India, ethnic and regional prejudice in contemporary India in a fictional story about the Indian women's national field-hockey team", "http://www.gstatic.com/tv/thumb/dvdboxart/168383/p168383_d_v8_aa.jpg", "https://www.youtube.com/watch?v=6a0-dSMWm5g")
#basha.show_trailer()
#sankarabharanam.show_trailer()


movies = [leader, titanic, rang_de_basanti, avatar, sankarabharanam, chak_de_india]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)