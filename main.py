import tkinter as tk
from tkinter import ttk
import sv_ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import time
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

time_ranges = 'long_term'


def all_time():
    global time_ranges
    all_time_button .configure(text='All Time ✅')
    medium_time_button .configure(text='Last 6 months')
    short_time_button .configure(text='Last 4 weeks')
    time_ranges='long_term'

def medium_time():
    global time_ranges
    medium_time_button .configure(text='Last 6 months ✅')
    all_time_button .configure(text='All Time')
    short_time_button .configure(text='Last 4 weeks')
    time_ranges='medium_term'
    
def short_time():
    global time_ranges
    short_time_button .configure(text='Last 4 weeks ✅')
    all_time_button .configure(text='All Time')
    medium_time_button .configure(text='Last 6 months')
    time_ranges='short_term'
   




sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope='user-top-read',
    show_dialog=False
))



def switch_acc():
    cache_path = '.cache'
    if os.path.exists(cache_path):
        os.remove(cache_path)
        
    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="68211539cfad494e840eff2b78b467e5",
        client_secret="c72b85417bda40b38d910c424751ce44",
        redirect_uri='http://127.0.0.1:8888/callback',
        scope='user-top-read',
        show_dialog=True
    
        ))
    
    output.delete(1.0, tk.END)
    output.insert(tk.END,('Cache cleared. Login window should reopen shortly.'))
    window.after(3000, show_artists)
        

    


window = tk.Tk()
window.geometry('800x600')
window.title('Spotipy.Stats')

output = tk.Text()
output.place(relx=0.5, rely=0.5, anchor='center')




def show_artists():
    global time_ranges
    global sp
    tracks_button.configure(text='Show top tracks')
    artists_button.configure(text='Show top artists ✅')
    top_artists = sp.current_user_top_artists(limit=10, time_range=time_ranges)
    output.delete(1.0, tk.END)
    for i, artist in enumerate(top_artists['items']):
        output.insert(tk.END,(f"{i+1}.  {artist['name']}\n"))
        
def show_tracks():
    global time_ranges
    global sp
    tracks_button.configure(text='Show top tracks ✅')
    artists_button.configure(text='Show top artists')
    top_tracks = sp.current_user_top_tracks(limit=10, time_range=time_ranges)
    output.delete(1.0, tk.END)
    for i, track in enumerate(top_tracks['items']):
        output.insert(tk.END,(f"{i+1}.  {track['name']}\n"))
        

artists_button = ttk.Button(text='Show top artists', command=show_artists)
artists_button.place(relx=0.6, rely=0.15, anchor='center')

tracks_button = ttk.Button(text='Show top tracks', command=show_tracks)
tracks_button.place(relx=0.4, rely=0.15, anchor='center')

login_button = ttk.Button(text='Switch Accounts', command=switch_acc)
login_button.place(relx=0.5, rely=0.9, anchor='center')

 


all_time_button = ttk.Button(text='All Time ✅', command=all_time)
all_time_button.place(relx=0.5, rely=0.05, anchor='center')

medium_time_button = ttk.Button(text='Last 6 months', command=medium_time)
medium_time_button.place(relx=0.3, rely=0.05, anchor='center')

short_time_button = ttk.Button(text='Last 4 weeks', command=short_time)
short_time_button.place(relx=0.7, rely=0.05, anchor='center')

sv_ttk.set_theme("dark")


window.mainloop()