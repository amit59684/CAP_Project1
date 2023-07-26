import instaloader
from pytube import YouTube



def audio_from_youtube(url):
    yt = YouTube(url)
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    audio_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(filename_prefix='video_')
    audio_stream.download(filename_prefix='audio_')
    print("🥳🥳Audio & Video downloaded successfully.🥳🥳")
def instagram_profile(url):
    insta = instaloader.Instaloader()
    insta.download_profile(url, profile_pic_only=True)
    profile = instaloader.Profile.from_username(insta.context, url)
    posts = list(profile.get_posts())
    latest_post = posts[0]
    insta.download_post(latest_post, target=profile.username)
    print("🥳🥳Instagram profile downloaded successfully.🥳🥳")


Youtube_URL=input("Please Enter Youtube URL-->")
Instagram_URL = input("Please Enter Instagram URL-->")

if Youtube_URL.strip():     # Check if the input is not empty
    audio_from_youtube(Youtube_URL)
else:
    instagram_profile(Instagram_URL)    