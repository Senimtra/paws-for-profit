// Update pawfolio info card
const pawfolioCard = () => {
    const leaderboardLinks = document.querySelectorAll(".leaderboard-item");
    const performanceSpan = document.getElementById("performanceValue");
    const leaderCard = document.querySelector(".leaderboard-item");
    const leaderName = leaderCard.innerHTML.trim().split(" ")[0];

    // Show leader manager card
    const managerElements = document.getElementsByClassName("manager-name");
    let targetSection = null;
    for (let el of managerElements) {
        if (el.textContent.trim() === leaderName) {
            targetSection = el.closest("section");
            targetSection.classList.remove("d-none");
        }
    }

    leaderboardLinks.forEach((link) => {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Remove 'active' class from all links
            leaderboardLinks.forEach((l) => l.classList.remove("active"));

            // Add 'active' class to the clicked link
            this.classList.add("active");

            // Get the new performance value from data attribute
            const newPerformance = this.getAttribute("data-performance");

            // Switch pawfolio manager cards
            targetSection.classList.add("d-none");
            for (let el of managerElements) {
                if (el.textContent.trim() === this.getAttribute("data-name")) {
                    targetSection = el.closest("section");
                    targetSection.classList.remove("d-none");
                }
            }

            // Update the performance value text
            performanceSpan.textContent =
                parseFloat(newPerformance).toFixed(2) + "%";
        });
    });
};
