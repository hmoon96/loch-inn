  // List of video IDs for the playlist
  const playlist = ['kfihbSkGX2g', 'XQ2r1XRAmZE', 'knZlD5uXNEw', 'upPl9mZW_zw'];
  console.log("Current Playlist:", playlist);
  let currentVideoIndex = 0; // Start with the first video in the playlist

  // Load the IFrame Player API code asynchronously
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  var player;

  function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
      height: '390',
      width: '640',
      videoId: playlist[currentVideoIndex], // Load the first video in the playlist
      playerVars: {
        'playsinline': 1,
        'origin': 'http://127.0.0.1:8000' // Add your local server's origin
      },
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange,
        'onError': onPlayerError
      }
    });
  }

  function onPlayerReady(event) {
    event.target.playVideo(); // Automatically play the video when ready
  }

  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
      playNextVideo(); // Play the next video when the current one ends
    }
  }

  function onPlayerError(event) {
    console.error('Error occurred:', event.data);
    if (event.data === 150 || event.data === 101) {
      console.log("This video is restricted and cannot be embedded. Skipping to the next video.");
      playNextVideo(); // Skip to the next video if there's an error
    }
  }

  function playNextVideo() {
    currentVideoIndex = (currentVideoIndex + 1) % playlist.length; // Loop back to the start if at the end
    player.loadVideoById(playlist[currentVideoIndex]); // Load the next video
  }

  // Optional: Function to play a specific video by index
  function playVideoByIndex(index) {
    if (index >= 0 && index < playlist.length) {
      currentVideoIndex = index;
      player.loadVideoById(playlist[currentVideoIndex]);
    }
  }

  // Next button event listener
  document.getElementById('nextButton').addEventListener('click', function() {
    playNextVideo(); // Play the next video in the playlist
  });

  // Previous button event listener
  document.getElementById('previousButton').addEventListener('click', function() {
    currentVideoIndex = (currentVideoIndex - 1 + playlist.length) % playlist.length; // Loop back to the end if at the start
    player.loadVideoById(playlist[currentVideoIndex]); // Load the previous video
  });