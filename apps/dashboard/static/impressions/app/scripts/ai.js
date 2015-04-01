'use strict';
console.log(document['adomattic']);

var data;

// read the cookie function
var readCookie = function(a){
    var d=[],
        e=document.cookie.split(";");
    a=RegExp("^\\s*"+a+"=\\s*(.*?)\\s*$");
    for(var b=0;b<e.length;b++){
        var f=e[b].match(a);
        f&&d.push(f[1])
    }
    return d
};

console.log(readCookie('customer'));

var addUnits = function (data, p) {
  console.log(data);
  console.log(p);
  var layer = document.createElement('div');
  layer.innerHTML = data
  var unit = document.getElementsByClassName('magneto-unit')[p];
  unit.appendChild(layer);
};

//addUnits();

axios({
  //url: 'http://localhost:8000/api/impressions/i/',
  url: 'http://app.adomattic.com/api/impressions/i/',
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
  };
});

readCookie('customer');
