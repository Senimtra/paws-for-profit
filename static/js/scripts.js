// Create pawfolio mini-chart
const miniChart = () => {
    const perfEl = document.getElementById("performanceValue");
    const performanceValue = parseFloat(perfEl.dataset.performance);

    // Set text and color
    perfEl.textContent = performanceValue.toFixed(2) + "%";
    perfEl.style.color = performanceValue >= 0 ? "#00ff91" : "#ff5555";

    // Draw the chart
    const ctx = document.getElementById("miniChart").getContext("2d");
    const gradient = ctx.createLinearGradient(0, 0, 0, 50);
    gradient.addColorStop(0, "rgba(255, 255, 255, 0.21)");
    gradient.addColorStop(1, "rgba(255, 255, 255, 0.08)");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: Array.from({ length: 10 }, (_, i) => i),
            datasets: [
                {
                    data:
                        performanceValue > 0
                            ? [0, 0.8, 1, 2, 1.8, 3.2, 3.8, 3.4, 4.3, 4.7]
                            : performanceValue < 0
                            ? [
                                  0, -1.4, -1, -1.7, -2, -3.2, -3, -3.7, -3.6,
                                  -4.7,
                              ]
                            : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    fill: true,
                    backgroundColor: gradient,
                    borderColor: "#7848cc",
                    tension: 0.3,
                    pointRadius: 0,
                },
            ],
        },
        options: {
            responsive: false,
            plugins: { legend: { display: false } },
            scales: { x: { display: false }, y: { display: false } },
        },
    });
};
