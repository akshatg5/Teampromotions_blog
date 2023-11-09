var data = {
    labels: [
        "Sales Increase",
        "Brand Awareness",
        "Customer Retention",
        "Sales Increase"
    ],
    datasets: [
        {
            data: [25, 25, 25, 25],
            backgroundColor: [
                "#4cc2c0",
                "#3cb878",
                "#fcb03b",
                "#f15b26"
            ]
        }]
};
var ctx = document.getElementById("myChart");
$(document).ready(function () {

    $('#myChart').waypoint(function () {
        var myDoughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: data,
            options: {
                legend: {
                    display: false
                }
            },
            animation: {
                animateScale: true
            }
        });
        this.destroy();
    }, {offset: '75%'});
});
