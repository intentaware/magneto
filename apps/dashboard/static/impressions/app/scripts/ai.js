'use strict';

var addUnits = function(data, p) {
  console.log(data);
  console.log(p);
  var layer = document.createElement('div');
  layer.className = 'adomattic';
  layer.innerHTML = data.template;
  var unit = document.getElementsByClassName('adomattic-y')[p];
  unit.onclick = function () {
    var self = this;
    console.log(self.id);
  };
  unit.id = 'adomattic' + data.id;
  unit.appendChild(layer);
};

var styleSheet = document.createElement('link');
styleSheet.href = 'styles/main.css';
styleSheet.type = 'text/css';
styleSheet.rel = 'stylesheet';
document.getElementsByTagName('head')[0].appendChild(styleSheet);

axios({
  url: 'http://localhost:8000/api/impressions/i/',
  //url: 'http://app.adomattic.com/api/impressions/i/',
  method: 'GET',
  headers: {
    'PUBLISHER-KEY': document['adomattic']
      //'Access-Control-Allow-Credentials' : true,
      //'Access-Control-Allow-Origin': window.location.origin
  },
  withCredentials: true
}).then(function(response) {
  console.log(response.data);
  for (var i = 0; i < response.data.length; i++) {
    addUnits(response.data[i], i);
  }
});

//readCookie('customer');
