'use strict';

var activeImpression;

var urls = {
  base: 'http://localhost:9050/api/',
  endPoints: {
    impression: function() {
      return (document['campaignID']) ? 'impressions/i/0/' + btoa('campaign:' + document['campaignID']) + '/' : 'impressions/i/';
    },
    claim: function(id, email) {
      var b64 = btoa('email:' + email);
      return 'impressions/i/' + id + '/' + b64 + '/';
    }
  }
};

console.log(document.currentScript.parentNode);



var addUnits = function(data, p) {
  console.log(data);
  console.log(p);
  var layer = document.createElement('div');
  layer.className = 'adomattic';
  layer.innerHTML = data.template;
  var unit = document.getElementsByClassName('adomattic-y')[p];
  console.log(unit);
  unit.onclick = function() {
    unit.onclick = false;
    var self = this;
    activeImpression = this.id.replace('adomattic', '');
    console.log(activeImpression);

    //defining adomattic layers on click
    var impression = self.querySelectorAll('div.impression')[0];
    var info = self.querySelectorAll('div.info')[0];
    var result = self.querySelectorAll('div.result')[0];
    console.log(result);

    // hiding impression and showing info
    impression.classList.add('hide');
    info.classList.remove('hide');

    var f = info.getElementsByTagName('form')[0];
    f.elements['submit'].addEventListener('click', function(event) {
      event.preventDefault();
    });
    f.elements['submit'].onclick = function() {
      var email = f.elements['email'].value;
      var tos = f.elements['tos'];
      if (tos.checked) {
        axios({
          url: urls.base + urls.endPoints.claim(activeImpression, email),
          method: 'GET',
          headers: {
            'PUBLISHER-KEY': document['adomattic']
              //'Access-Control-Allow-Credentials' : true,
              //'Access-Control-Allow-Origin': window.location.origin
          },
          data: {
            email: email,
          }
        }).then(function() {
          info.classList.add('hide');
          result.classList.remove('hide');
        });
      } else {
        var tosContainer = self.querySelectorAll('div.tos-container')[0];
        tosContainer.classList.add('red');
      }
      //console.log(email, password);
    };

  };
  unit.id = 'adomattic' + data.id;
  unit.appendChild(layer);
};

var styleSheet = document.createElement('link');
styleSheet.href = (urls.base === 'http://localhost:9050/api/') ? 'styles/main.css' : 'http://app.intentaware.com/magneto/styles/main.css';
styleSheet.type = 'text/css';
styleSheet.rel = 'stylesheet';
document.getElementsByTagName('head')[0].appendChild(styleSheet);

axios({
  url: urls.base + urls.endPoints.impression(),
  //url: 'http://app.intentaware.com/api/impressions/i/',
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
