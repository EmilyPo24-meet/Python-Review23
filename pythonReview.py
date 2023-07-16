def create_youtube_video(title, description):
	new_youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}}
	return(new_youtube_video)

def likes(youtube_video):
	if likes in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def likes(youtube_video):
	if dislikes in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo[username] = comment_text
	return youtubevideo


youtube_video1 = create_youtube_video("AHH", "Very AHH")
likes(youtube_video1)
dislikes(youtube_video1)
add_comment(youtube_video1, "Emily", "Very Very AHH")
print(youtube_video1)
while youtube_video1["likes"] < 496:
	likes(youtube_video1)
print(youtube_video1)