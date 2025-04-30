// Get global indices
const getIndices = () => {
    async function updateIndices() {
        try {
            const response = await fetch("/indices/");
            if (!response.ok) {
                throw new Error(`Error fetching indices: ${response.status}`);
            }
            const data = await response.json();

            for (const id in data) {
                const indexDiv = document.getElementById(id);
                const item = data[id];

                if (item.error) {
                    indexDiv.innerHTML = "No data";
                    continue;
                }

                const change = item.change || 0;
                const percentageChange = item.percent_change || 0;

                indexDiv.innerHTML = `
                    <div class="name">${item.name}</div>
                    ${formatChange(change, percentageChange)}
                `;
            }
        } catch (error) {
            console.error(error);
            // Handle error gracefully
        }
    }

    function formatChange(change, percentage) {
        const arrow = change >= 0 ? "🔺" : "🔻";
        const className = change >= 0 ? "up" : "down";
        return `<span class="change ${className}">${arrow} ${change.toFixed(
            2
        )} (${percentage.toFixed(2)}%)</span>`;
    }

    updateIndices();
    setInterval(updateIndices, 1 * 60 * 1000); // Refresh every 1 min
};
