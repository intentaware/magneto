(function() {
  'use strict';
  // get the parent node
  // TODO:
  //    this does not work in IE / Edge
  //    catch exception here and write a script for IE
  var parent = document.currentScript.parentNode;

  // defining the urls here
  var urls = {
    base: 'http://localhost:9050/api/',
    endPoints: {
      impression: function() {
        return (document['campaignID']) ? 'impressions/i/0/' + btoa(JSON.stringify({campaign: document['campaignID']})) + '/' : 'impressions/i/';
      },
      claim: function(id, email) {
        var b64 = btoa(JSON.stringify({
          email: email
        }));
        return 'impressions/i/' + id + '/' + b64 + '/';
      },
      meta: function(id, data) {
        var b64 = btoa(JSON.stringify({
          meta: data
        }));
        return 'impressions/i/' + id + '/' + b64 + '/';
      }
    }
  };

  // insert intentaware styles
  var insertStyles = function() {
    var styleSheet = document.createElement('link');
    styleSheet.href = (urls.base === 'http://localhost:9050/api/') ? 'styles/main.css' : 'http://live.intentaware.com/magneto/styles/main.css';
    styleSheet.type = 'text/css';
    styleSheet.rel = 'stylesheet';
    document.getElementsByTagName('head')[0].appendChild(styleSheet);
  };

  // populate page
  var populateCampaign = function(coupon) {
    //console.log(coupon);
    var child = document.createElement('div');
    child.className = 'adomattic';
    child.innerHTML = coupon.template;
    child.id = 'intentaware-' + coupon.id;

    parent.appendChild(child);
    appendActions(child, coupon.id);
  };

  // get the impression
  var getCampaign = function() {
    axios({
      url: urls.base + urls.endPoints.impression(),
      method: 'GET',
      headers: {
        'PUBLISHER-KEY': document['intentaware']
      },
      //withCredentials: true
    }).then(function(response) {
      //console.log(response.data[0]);
      populateCampaign(response.data[0]);
      postMeta(response.data[0].id);
    });
  };

  // append interaction to the populated add unit
  var appendActions = function(layer, impressionID) {
    layer.onclick = function() {
      // prevent furthur clicks on the layer in question
      layer.onclick = false;

      //defining adomattic layers on click
      var impressionLayer = layer.querySelectorAll('div.impression')[0];
      var infoLayer = layer.querySelectorAll('div.info')[0];
      var resultLayer = layer.querySelectorAll('div.result')[0];

      impressionLayer.classList.add('hide');
      infoLayer.classList.remove('hide');

      // form clicks
      var form = infoLayer.getElementsByTagName('form')[0];
      submitForm(form, infoLayer, resultLayer, impressionID);
    };
  };

  var submitForm = function(form, info, result, impressionID) {
    form.elements['submit'].addEventListener('click', function(event) {
      event.preventDefault();
    });

    form.elements['submit'].onclick = function() {
      var email = form.elements['email'].value;
      var tos = form.elements['tos'];
      if (tos.checked) {
        axios({
          url: urls.base + urls.endPoints.claim(impressionID, email),
          method: 'GET',
          headers: {
            'PUBLISHER-KEY': document['intentaware']
          }
        }).then(function() {
          info.classList.add('hide');
          result.classList.remove('hide');
        });
      } else {
        var tosContainer = info.querySelectorAll('div.tos-container')[0];
        tosContainer.classList.add('red');
      }
      //console.log(email, password);
    };
  };

  var getMachineInfo = function() {
    var nvgtr = {};
    var scrn = {};
    var unwantedKeys = [
      'plugins', 'mimeTypes', 'geolocation', 'webkitTemporaryStorage',
      'webkitPersistentStorage', 'serviceWorker', 'permissions'
    ];

    // get window.navigator property as a simple JSON object
    for (var key in navigator) {
      //console.log(typeof(navigator[key]));
      //console.log(navigator[key]);
      if (
        (typeof(navigator[key]) !== 'function') && (unwantedKeys.indexOf(key) == -1)
      ) {
        nvgtr[key] = navigator[key];
      }
    }

    for (key in screen) {
      if (key == 'orientation') {
        scrn['orientation'] = screen.orientation.type;
      } else {
        scrn[key] = screen[key];
      }
    }


    var out = {
      navigator: nvgtr,
      screen: scrn
    };
    return JSON.stringify(out);
  };

  var postMeta = function(impressionID) {
    var meta = getMachineInfo();
    axios({
      url: urls.base + urls.endPoints.meta(impressionID, meta),
      method: 'GET',
      headers: {
        'PUBLISHER-KEY': document['intentaware']
      }
    }).then(function(response) {
      console.log(response);
    });
  };


  // do the work
  insertStyles();
  getCampaign();
})();
