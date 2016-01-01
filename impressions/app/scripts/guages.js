/**
 * @copyright IntentAware 2015
 * @license http://www.intentaware.com copyrighted
 */

(function() {
  'use strict';
  var urls = {
    base: 'http://localhost:9050/api/',
    endPoints: {
      guages: function() {
        return 'guages/g/' + document['assetID'] + '/';
      }
    }
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

    var origin = window.location.href;
    var out = {
      navigator: nvgtr,
      screen: scrn,
      origin: origin
    };

    return {
      meta: btoa(JSON.stringify(out))
    };
  };

  var postMatric = function () {
    var meta = getMachineInfo();
    console.log(meta);
    console.log(meta);
    console.log(document['intentaware']);
    axios({
      url: urls.base + urls.endPoints.guages(),
      headers: {
        'PUBLISHER-KEY': document['intentaware']
      },
      withCredentials: true,
      method: 'POST',
      data: meta
    });
  };

  postMatric();
})();
