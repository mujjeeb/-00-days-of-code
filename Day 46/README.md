# Day 46 of 100 Days of Code

## Musical Time Machine

![Musical Time Machine](https://example.com/musical_time_machine.jpg)

Welcome to Day 46 of the 100 Days of Code challenge! Get ready for a musical journey through time with the "Musical Time Machine." This project will take you back to the hit songs of the past. It's a fun project that scrapes the Billboard Hot 100 for a specific date, extracts artist and song names, and creates a Spotify playlist with the top 100 songs. Let's dive in and relive the music of yesteryears!

## Project Overview

![Billboard Hot 100](https://example.com/billboard_hot100.jpg)

- **main.py**:
  - The heart of the "Musical Time Machine," this script prompts the user to enter a date in 'YYYY-MM-DD' format.
  - It then scrapes the Billboard Hot 100 for that date, retrieving the top 100 songs.
  - The script formats the response, extracts artist names and song titles, and compiles them into a playlist.

- **spotipy.py**:
  - This module utilizes the Spotify API and the Spotipy library to create a Spotify playlist.
  - You will need to provide your Spotipy credentials to make it all work.

## Getting Started

To set up and run the "Musical Time Machine" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install spotipy beautifulsoup4
     ```

2. **Spotify Configuration:**
   - You will need to create a Spotify Developer App and obtain your Spotify API credentials (client ID and client secret).

3. **Project Setup:**
   - Clone this project repository and navigate to the project directory.

4. **Authentication:**
   - In the `main.py` script, provide your Spotify API credentials.

5. **Run the App:**
   - Execute the `main.py` script to start your musical journey.
   - Enter a date, and the script will create a Spotify playlist with the top 100 songs from that day.

![Spotify Playlist](https://example.com/spotify_playlist.jpg)

## Usage

![Enjoy the Music](https://example.com/enjoy_music.jpg)

- The "Musical Time Machine" project lets you travel back in time to the music of your chosen date.
- It's perfect for nostalgic music lovers and those who want to discover the hits of the past.

## Customization

- Modify the script to include additional functionalities or filters for your musical exploration.
- Add features to search for specific songs, artists, or genres to create custom playlists.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational and entertainment purposes. It's a delightful way to blend programming with your passion for music!


## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy your musical journey with the "Musical Time Machine." Feel the nostalgia, discover new tunes, and groove to the rhythms of the past! 🎵🕰️