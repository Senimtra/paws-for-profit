// Get pawfolio pawformance
const getPawformance = () => {
    async function updatePawformance() {
        try {
            const response = await fetch("/pawformances/");
            if (!response.ok) {
                throw new Error(
                    `Error fetching pawformance: ${response.status}`
                );
            }
            const data = await response.json();

            const leaderboardItems =
                document.getElementsByClassName("leaderboard-item");

            // Update leaderboard item pawformance
            for (i = 0; i < leaderboardItems.length; i++) {
                const item = leaderboardItems[i];
                const pawfolioName = item.dataset.name;
                const performance = data[pawfolioName][0];
                const perfSpan = item.querySelector(".leaderboard-pawformance");
                perfSpan.textContent = `${performance.toFixed(2)}%`;
            }
        } catch (error) {
            console.error(error);
            // Handle error gracefully
        }
    }
    updatePawformance();
    setInterval(updatePawformance, 1 * 60 * 1000); // Refresh every 1 min
};
