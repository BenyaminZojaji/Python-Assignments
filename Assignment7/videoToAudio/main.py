from moviepy import editor
video = editor.VideoFileClip('Mohsen Yeganeh - Behet Ghol Midam.mp4')
video.audio.write_audiofile('Mohsen Yeganeh - Behet Ghol Midam.mp3')