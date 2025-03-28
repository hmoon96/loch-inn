const searchText = document.getElementById("search-text").innerText;

const searchBar = document.getElementById("search-bar");

searchBar.addEventListener("click", (e) => { 
    e.preventDefault(); // Prevent form submission
    const searchQuery = searchText.trim(); // Get the search query from the input field

    if (searchQuery) {
        const baseURL = window.location.origin; // Get the base URL of the current page
        const url = `${baseURL}/search/${searchQuery}`; // Construct the URL with the search query
        window.location.assign(url); // Redirect to the search results page
    }
});