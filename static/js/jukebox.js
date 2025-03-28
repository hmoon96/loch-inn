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
    }
});