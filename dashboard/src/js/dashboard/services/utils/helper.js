'use strict';

angular.module('adomattic.dashboard')
  .service('Helper', function () {
    var self = this;

    self.toIDs = function (array) {
      return array.map(function (s) {
        s = s.id;
        return s;
      });
    };

    self.toObjects = function (idArray, objectArray) {
      return idArray.map(function (id) {
        var index = _.findIndex(objectArray, function (object) {
          return parseInt(object.id) === parseInt(id);
        });

        return objectArray[index];
      });
    };

    /**
     * converts json to query params on a url
     * @param  {json} obj the json to be converted
     * @return {str}     string that is to be converted
     */
    self.jsonToURL = function (obj, prefix) {
      var str = [];

      _.each(obj, function (val, key) {
        str.push(encodeURIComponent(key) + '=' + encodeURIComponent(val));
      });

      str = str.join('&');
      str = prefix ? prefix + '?' + str : str;
      return str;
    };

    self.getPixel = function (publisherKey, campaignID) {
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

    self.getGuagePixel = function (publisherKey, assetID) {
      assetID = assetID || null;


      var assetRoot = ((window.location.hostname === 'app.intentaware.com') || (window.location.hostname === 'live.intentaware.com')) ? window.location.protocol + '//' + window.location.host + '/magneto' : 'scripts';

      var pixel;

      if (assetID) {
        pixel = '<script>(function(){document.intentaware="' + publisherKey + '";document.assetID="' + assetID + '";var b=document.currentScript.parentNode,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="' + assetRoot + '/guages.js";b.appendChild(a)})();</script>';
      } else {
        pixel = '<script>(function(){document.intentaware="' + publisherKey + '";var b=document.currentScript.parentNode,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="' + assetRoot + '/guages.js";b.appendChild(a)})();</script>';
      }

      return pixel;
    };

    self.mockDemographics = function (count) {
      return [{
        'name': 'Income',
        'children': [{
          'name': '200K +',
          'size': Math.floor((Math.random() * count) + 1)
        }, {
          'name': '150K - 200K',
          'size': Math.floor((Math.random() * count) + 1)
        }, {
          'name': '100K - 150K',
          'size': Math.floor((Math.random() * count) + 1)
        }, {
          'name': '60K - 100K',
          'size': Math.floor((Math.random() * count) + 1)
        }, {
          'name': '> 60K',
          'size': Math.floor((Math.random() * count) + 1)
        }]
      }, {
        name: 'Education',
        children: [{
          name: 'No Educaiton',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'High School',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Some School',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Bechelors',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Post Grad',
          size: Math.floor((Math.random() * count) + 1)
        }]
      }, {
        name: 'Transport',
        children: [{
          name: 'Drives Alone',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Carpooled',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Public Transit',
          size: Math.floor((Math.random() * count) + 1)
        }]
      }, {
        name: 'Marital Status',
        children: [{
          name: 'Single',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Married',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'Divorced',
          size: Math.floor((Math.random() * count) + 1)
        }]
      }, {
        name: 'Device Info',
        children: [{
          name: 'mobile',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'tablet',
          size: Math.floor((Math.random() * count) + 1)
        }, {
          name: 'desktop',
          size: Math.floor((Math.random() * count) + 1)
        }]
      }];
    };
  });
