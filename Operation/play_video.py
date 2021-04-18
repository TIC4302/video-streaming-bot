import vlc
import pafy
import urllib.request
import sys, getopt

def main(argv):
	#url = "https://www.youtube.com/watch?v=Yw6u6YkTgQ4"
	#url = "https://www.youtube.com/watch?v=FUiu-cdu6mA" #25 sec video, for quick test
	#url = "https://www.youtube.com/watch?v=Xk24DMOInnQ" #30 min video, use to test start and stop at specfic timing for video
	#opt = " --stats"
	inputURL = ''
	video_start_time = '0.0'
	video_run_time = ''
	try:
		opts, args = getopt.getopt(argv,"hi:s:r:")
	except getopt.GetoptError:
		print ('wrong option')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-i':
			inputURL = arg
		elif opt == '-s':
			video_start_time = arg
		elif opt == '-r':
			video_run_time = arg
		elif opt == '-h':
			print ('help')
			exit(2)
	url = inputURL
	video = pafy.new(url)
	best = video.getbest()
	playurl = best.url
	ins = vlc.Instance()
	player = ins.media_player_new()

	code = urllib.request.urlopen(url).getcode()
	if str(code).startswith('2') or str(code).startswith('3'):
	    print('Stream is working')
	else:
	    print('Stream is dead')
	Media = ins.media_new(playurl)
	Media.get_mrl()
	print (f"Title of video: {video.title}")
	print (f"Author of video: {video.author}")
	print (f"video duration: {video.duration}")
	print (f"video viewcount: {video.viewcount}")
	print (f"no of likes: {video.likes}")
	print (f"video dislikes: {video.dislikes}")
	Media.add_option('start-time={}' .format(video_start_time)) #used to set start time of video in sec
	Media.add_option('run-time={}' .format(video_run_time)) #used to set run time of video in sec
	player.set_media(Media)
	player.audio_set_volume(50)

	player.play()

	good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
	end_states = "State.Ended"
	while str(player.get_state()) in good_states:
		if (player.get_state() == end_states):
			break

	#get metadata of video
	print (f"Length of video in ms: {Media.get_duration()}")
	player.stop()
	
if __name__ == "__main__":
	main(sys.argv[1:])
