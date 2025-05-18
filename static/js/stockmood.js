// Start values catnip, tuna, laser
let catnip = 4.1; // range: 3.00 – 8.00
let tuna = 2.8; // range: 1.50 – 4.50
let laser = 11.9; // range: 10.00 – 20.00

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

            catnip = updatePrice(catnip, 3.0, 8.0);
            tuna = updatePrice(tuna, 1.5, 4.5);
            laser = updatePrice(laser, 10.0, 15.0);

            const cards = [
                {
                    emoji: "😻",
                    label: "Up",
                    value: `${up.toFixed(1)}%`,
                    arrow: "↑",
                },
                {
                    emoji: "🙀",
                    label: "Down",
                    value: `${down.toFixed(1)}%`,
                    arrow: "↓",
                },
                {
                    emoji: "💤",
                    label: "Flat",
                    value: `${flat.toFixed(1)}%`,
                    arrow: "↔",
                },
                {
                    emoji: "🌿",
                    label: "Catnip",
                    value: `$${catnip.toFixed(2)}`,
                    arrow: "",
                },
                {
                    emoji: "🐟",
                    label: "Tuna",
                    value: `$${tuna.toFixed(2)}`,
                    arrow: "",
                },
                {
                    emoji: "🔴",
                    label: "Laser Dot",
                    value: `$${laser.toFixed(2)}`,
                    arrow: "",
                },
            ];

            const container_xl = document.querySelector(".ticker-cards");
            const container_mobile = document.querySelector(".tickers-mobile");
            container_xl.innerHTML = ""; // clear existing cards
            container_mobile.innerHTML = "";
            cards.forEach(({ emoji, label, value, arrow }) => {
                const createCard = () => {
                    const card = document.createElement("div");
                    card.className = "ticker-card";
                    card.innerHTML = `
                        <span class="emoji">${emoji}</span>
                        <span class="label">${label}:</span>
                        <span class="value">${value}</span>
                        <span class="arrow">${arrow}</span>
                    `;
                    return card;
                };
                container_xl.appendChild(createCard());
                container_mobile.appendChild(createCard());
            });
        } catch (error) {
            console.error(error);
            // Handle error gracefully
        }
    }
    updateStockMood();
    setInterval(updateStockMood, 1 * 60 * 1000); // Refresh every 1 min
};

// Update Catnip, Tuna, Laser dot
const updatePrice = (current, min, max) => {
    const step = 0.05 * (Math.floor(Math.random() * 9) + 1); // 1–9 → 0.05–0.45
    const direction = Math.random() < 0.5 ? -1 : 1;
    let next = current + direction * step;

    // Clamp within range
    next = Math.max(min, Math.min(max, next));

    // Round to 2 decimals
    return Math.round(next * 100) / 100;
};
