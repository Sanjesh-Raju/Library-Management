frappe.pages['live-chart'].on_page_load = function (wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Live Bitcoin Price Chart',
        single_column: true
    });

    // Chart container
    $('<div id="live-chart" style="height: 300px;"></div>').appendTo(page.body);

    // Initialize chart
    let chart = new frappe.Chart("#live-chart", {
        title: "BTC Price (USD)",
        data: {
            labels: [],
            datasets: [
                {
                    name: "BTC/USD",
                    chartType: "line",
                    values: []
                }
            ]
        },
        type: 'axis-mixed',
        height: 300,
        colors: ['#f39c12'],
        axisOptions: {
            xAxisMode: 'tick',
            xIsSeries: true
        }
    });

    // Data storage
    let labels = [];
    let values = [];

    function fetchData() {
        fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            .then(response => response.json())
            .then(data => {
                const btcPrice = data.bitcoin.usd;
                const timestamp = new Date().toLocaleTimeString();

                // Limit to last 10 entries
                labels.push(timestamp);
                values.push(btcPrice);
                if (labels.length > 10) {
                    labels.shift();
                    values.shift();
                }

                chart.update({
                    labels: labels,
                    datasets: [
                        {
                            name: "BTC/USD",
                            chartType: "line",
                            values: values
                        }
                    ]
                });
            })
            .catch(error => {
                console.error("Error fetching price:", error);
            });
    }

    fetchData();
    setInterval(fetchData, 5000);
};
