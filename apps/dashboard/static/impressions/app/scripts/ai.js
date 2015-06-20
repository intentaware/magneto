'use strict';

var activeImpression;
var urls = {
  base: 'http://localhost:9050/api/',
  endPoints: {
    impression: 'impressions/i/',
    claim: function (id, email) {
      return 'impressions/i/' + id + '/' + email +'/';
    }
  }
};



var addUnits = function(data, p) {
  console.log(data);
  console.log(p);
  var layer = document.createElement('div');
  layer.className = 'adomattic';
  layer.innerHTML = data.template;
  var unit = document.getElementsByClassName('adomattic-y')[p];
  unit.onclick = function() {
    unit.onclick = false;
    var self = this;
    activeImpression = this.id.replace('adomattic', '');
    console.log(activeImpression);

    //defining adomattic layers on click
    var impression = self.querySelectorAll('div.impression')[0];
    var loginForm = self.querySelectorAll('div.login-form')[0];
    var result = self.querySelectorAll('div.result')[0];
    console.log(result);

    // hiding impression and showing loginform
    impression.classList.add('hide');
    loginForm.classList.remove('hide');

    var f = loginForm.getElementsByTagName('form')[0];
    f.elements['submit'].addEventListener('click', function(event) {
      event.preventDefault();
    });
    f.elements['submit'].onclick = function() {
      var email = f.elements['email'].value;
      //console.log(email, password);
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
          password1: '1',
          password2: '1'
        }
      }).then(function() {
        loginForm.classList.add('hide');
        result.classList.remove('hide');
      });
    };

  };
  unit.id = 'adomattic' + data.id;
  unit.appendChild(layer);
};

var styleSheet = document.createElement('link');
styleSheet.href = (urls.base === 'http://localhost:9050/api/') ? 'styles/main.css': 'http://app.adomattic.com/static/impressions/dist/styles/main.css';
styleSheet.type = 'text/css';
styleSheet.rel = 'stylesheet';
document.getElementsByTagName('head')[0].appendChild(styleSheet);

axios({
  url: urls.base + urls.endPoints.impression,
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
