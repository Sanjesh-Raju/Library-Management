frappe.pages['live-chart'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Live Sensor Chart',
        single_column: true
    });

    $('<div id="live-chart" style="height: 300px;"></div>').appendTo(page.body);
    let chart = new frappe.Chart("#live-chart", {
        title: "Sensor Live Data",
        data: {
            labels: [],
            datasets: [
                {
                    name: "Sensor Value",
                    chartType: "line",
                    values: []
                }
            ]
        },
        type: 'axis-mixed',
        height: 300,
        colors: ['#7cd6fd'],
        axisOptions: {
            xAxisMode: 'tick',
            xIsSeries: true
        }
    });

    function fetchData() {
        frappe.call({
            method: "library_management.library_management.doctype.sensor_data.sensor_data.get_live_sensor_data",
            callback: function(r) {
                console.log("Sensor data response:", r.message); 
                if (r.message) {
                    const data = r.message;
                    chart.update({

                        labels: data.labels,
                        datasets: [
                            {
                                name: "Sensor Value",
                                chartType: "line",
                                values: data.values
                            }
                        ]
                    });
                }
            }
        });
    }

    // Fetch data every 5 seconds
    fetchData();
    setInterval(fetchData, 5000);
};
