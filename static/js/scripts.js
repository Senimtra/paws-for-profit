// Create pawfolio mini-chart
const miniChart = () => {
    const perfEl = document.getElementById("performanceValue");
    const performanceValue = parseFloat(perfEl.dataset.performance);

    // Set text and color
    perfEl.textContent = parseFloat(perfEl.dataset.performance) + "%";
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
                            ? [
                                  0,
                                  1,
                                  2,
                                  2.5,
                                  3.2,
                                  3.8,
                                  4.1,
                                  4.3,
                                  4.2,
                                  performanceValue,
                              ]
                            : [
                                  0,
                                  -0.5,
                                  -1,
                                  -1.4,
                                  -2,
                                  -2.2,
                                  -3,
                                  -3.5,
                                  -4,
                                  performanceValue,
                              ],
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
