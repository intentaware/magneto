'use strict';

angular.module('adomattic.dashboard')
  .service('Helper', function() {
    var self = this;

    self.toIDs = function(array) {
      return array.map(function(s) {
        s = s.id;
        return s;
      });
    };

    self.toObjects = function(idArray, objectArray) {
      return idArray.map(function(id) {
        var index = _.findIndex(objectArray, function(object) {
          return parseInt(object.id) === parseInt(id);
        });
        return objectArray[index];
      });
    };

    self.getPixel = function(publisherKey, campaignID) {
      campaignID = campaignID || null;
      var assetRoot = (window.location.hostname === 'app.intentaware.com' || 'live.intentaware.com') ? window.location.protocol + '//' + window.location.host + '/magneto' : 'http://' + window.location.host + '/static/impressions/dist/';
      var pixel;

      if (campaignID) {
        pixel = '<script>(function(){document.intentaware="' + publisherKey + '";document.campaignID="' + campaignID + '";var b=document.currentScript.parentNode,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="' + assetRoot + '/aware.js";b.appendChild(a)})();</script>';
      } else {
        pixel = '<script>(function(){document.intentaware="' + publisherKey + '";var b=document.currentScript.parentNode,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="' + assetRoot + '/aware.js";b.appendChild(a)})();</script>';
      }

      return pixel;
    };
  });
