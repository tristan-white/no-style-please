d3.csv('/assets/visited_countries.csv', function(err, rows){
      function unpack(rows, key) {
          return rows.map(function(row) { return row[key]; });
      }

    var data = [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: unpack(rows, 'location'),
        z: unpack(rows, 'visited'),
        //text: unpack(rows, 'location'),
        autocolorscale: true,
        showscale: false,
        hoverinfo: "location",
    }];

    var layout = {
      title: {
        text: "countries i've visited",
        y: 0.8,
      },
      geo: {
          projection: {
              type: 'robinson'
          }
      },
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});
    console.log(unpack(rows, 'alcohol'));

});

