// Update pawfolio info card
const pawfolioCard = () => {
    const leaderboardLinks = document.querySelectorAll(".leaderboard-item");
    const performanceSpan = document.getElementById("performanceValue");
    const leaderCard = document.querySelector(".leaderboard-item");
    const leaderNameSpan = leaderCard.querySelector("span");
    const leaderName = leaderNameSpan.innerHTML.trim();

    // Show leader manager card
    const managerElements = document.getElementsByClassName("manager-name");
    let targetSection = null;
    for (let el of managerElements) {
        if (el.textContent.trim() === leaderName) {
            targetSection = el.closest("section");
            targetSection.classList.remove("d-none");
        }
    }

    // Show leader performance value
    const perfLeaderValue = document.querySelector(
        ".leaderboard-item.active .leaderboard-pawformance"
    );
    const rawPerfValue = perfLeaderValue.textContent;
    const rawPerfNumber = parseFloat(rawPerfValue);
    performanceSpan.textContent = rawPerfNumber + "%";

    // Leaderboard Event-Listeners
    leaderboardLinks.forEach((link) => {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Remove 'active' class from all links
            leaderboardLinks.forEach((l) => l.classList.remove("active"));

            // Add 'active' class to the clicked link
            this.classList.add("active");

            // Get the new performance value
            const newPerfLeaderValue = document.querySelector(
                ".leaderboard-item.active .leaderboard-pawformance"
            );
            const newRawPerfValue = newPerfLeaderValue.textContent;
            const newRawPerfNumber = parseFloat(newRawPerfValue);
            
            // Switch pawfolio manager cards
            targetSection.classList.add("d-none");
            for (let el of managerElements) {
                if (el.textContent.trim() === this.getAttribute("data-name")) {
                    targetSection = el.closest("section");
                    targetSection.classList.remove("d-none");
                }
            }

            // Update the performance value text
            performanceSpan.textContent = newRawPerfNumber.toFixed(2) + "%";
        });
    });
};
