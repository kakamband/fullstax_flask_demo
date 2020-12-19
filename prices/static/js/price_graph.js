

d3.json(`/btc_data/${JSstart}/${JSclose}`, data =>{
    objects = Object.values(data)

    console.log(objects)

    time = objects.map(x => x.unix)
    openn = objects.map( x => x.open)
    console.log(openn)


var trace1 = {
    x: time,
    y: openn,
    type: 'scatter'
  };
  
//   var trace2 = {
//     x: [1, 2, 3, 4],
//     y: [16, 5, 11, 9],
//     type: 'scatter'
//   };
  
  var traces = [trace1];
  
  Plotly.newPlot('pricePlot', traces);

})