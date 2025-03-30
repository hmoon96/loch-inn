const toggleButton = document.getElementById("toggleSearchButton");
const searchMenu = document.getElementById("juke-search");


// Add event listener to the toggle button
toggleButton.addEventListener("click", () => {
    // Toggle the "open" class to slide the menu in/out
    searchMenu.classList.toggle("open");
});


// Ensure the menu is always visible for screens above 1000px
window.addEventListener("resize", () => {
    if (window.innerWidth > 1000) {
        searchMenu.classList.remove("open");
        searchMenu.style.display = "block"; // Always visible
    } else {
        searchMenu.style.display = ""; // Reset to CSS rules
    }});
    

// //const searchText = document.getElementById("search-text").innerText;//
// const searchInput = document.getElementById("search-text");

// const searchBar = document.getElementById("search-bar");

// searchBar.addEventListener("click", (e) => { 
//     e.preventDefault(); // Prevent form submission
//     // const searchQuery = searchText.trim(); // Get the search query from the input field
//     const searchQuery = document.getElementById(searchText.value.trim);

//     if (searchQuery) {
//         const baseURL = window.location.origin; // Get the base URL of the current page
//         const url = `${baseURL}/search/${encodeURIComponent(searchQuery)}`; // Construct the URL with the search query
//         window.location.assign(url); // Redirect to the search results page
//     }
// });