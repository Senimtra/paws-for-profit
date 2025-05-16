// Get stock mood
const getStockMood = () => {
    async function updateStockMood() {
        try {
            const response = await fetch("/stockmood/");
            if (!response.ok) {
                throw new Error(`Error fetching indices: ${response.status}`);
            }
            const data = await response.json();
            const { up, down, flat } = data;
            const moodText = `🐾 Today's Stock Mood: 😻 ${up}% ↑ · 🙀 ${down}% ↓ · 💤 ${flat}% ↔`;
            document.getElementById("stock-mood").textContent = moodText;
        } catch (error) {
            console.error(error);
            // Handle error gracefully
        }
    }
    updateStockMood();
    setInterval(updateStockMood, 1 * 60 * 1000); // Refresh every 1 min
};
