var xValues = ["Engg. Maths 1", "Engg. Physics 1", "Engg. Chemistry 1", "Basic Elec. Engg.", "Mechanics"];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["#8C0000", "#F90716","#018383","#04009A","#851DE0"];

new Chart("barGraphSem1", {
  type: "horizontalBar",
  data: {
  labels: xValues,
  datasets: [{
    backgroundColor: barColors,
    data: yValues
  }]
},
  options: {
    legend: {display: false},
    title: {
      position:'bottom',
      display: true,
      text: "Semester 1"
    },
    scales: {
      xAxes: [{ticks: {min:0, max:100}}],
      yAxes: [{display:false}],
    }
  }
});
var xValues = ["Engg. Maths 1", "Engg. Physics 1", "Engg. Chemistry 1", "Basic Elec. Engg.", "Mechanics"];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["#8C0000", "#F90716","#018383","#04009A","#851DE0"];

new Chart("donutGraphSem1", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  legend:{display:false},
});


// Sem 2 ke liye
var xValues = ["Engg. Maths 2", "Engg. Physics 2", "Engg. Chemistry 2", "Pro. Comm. Ethics", "Engg. Drawing", "SPA"];
var yValues = [55, 49, 44, 24, 15, 50];
var barColors = ["#8C0000", "#F90716","#018383","#04009A","#851DE0","#42E6A4"];

new Chart("barGraphSem2", {
  type: "horizontalBar",
  data: {
  labels: xValues,
  datasets: [{
    backgroundColor: barColors,
    data: yValues
  }]
},
  options: {
    legend: {display: false},
    title: {
      position:'bottom',
      display: true,
      text: "Semester 2"
    },
    scales: {
        xAxes: [{ticks: {min:0, max:100}}],
        yAxes: [{display:false}],
    }
  }
});
var xValues = ["Engg. Maths 2", "Engg. Physics 2", "Engg. Chemistry 2", "Pro. Comm. Ethics", "Engg. Drawing", "SPA"];
var yValues = [55, 49, 44, 24, 15, 50];
var barColors = ["#8C0000", "#F90716","#018383","#04009A","#851DE0","#42E6A4"];

new Chart("donutGraphSem2", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  legend:{display:false},
});