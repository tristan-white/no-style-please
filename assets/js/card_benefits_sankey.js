var data = {
  type: "sankey",
  orientation: "h",
  node: {
    pad: 15,
    thickness: 30,
    line: {
      color: "black",
      width: 0.5
    },
   label: ["Amex Platinum", "Amex Gold", "Saphire Reserve", "travel", "food", "misc","intro bonus"],
   color: "blue"
      },

  link: {
    source: [0,1,2,2,1,0],
    target: [6,6,6,3,4,3],
    value:  [1250,800,900,300,10,40]
  }
}

var data = [data]

var layout = {
  title: "Basic Sankey",
  font: {
    size: 10
  }
}

Plotly.react('myDiv', data, layout)
