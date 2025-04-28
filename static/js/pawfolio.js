// Update pawfolio info card
const pawfolioCard = () => {
    const leaderboardLinks = document.querySelectorAll(".leaderboard-item");
    const performanceSpan = document.getElementById("performanceValue");

    leaderboardLinks.forEach((link) => {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Remove 'active' class from all links
            leaderboardLinks.forEach((l) => l.classList.remove("active"));

            // Add 'active' class to the clicked link
            this.classList.add("active");

            // Get the new performance value from data attribute
            const newPerformance = this.getAttribute("data-performance");

            // Update the performance value text
            performanceSpan.textContent =
                parseFloat(newPerformance).toFixed(2) + "%";
        });
    });
};
