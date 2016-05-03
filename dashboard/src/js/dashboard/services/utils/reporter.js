'use strict';

angular.module('adomattic.dashboard')
  .service('ReporterOld', function() {
    var self = this;

    self.setUserAgentInfo = function(parser, ua, obj) {
      var info = parser.setUA(ua).getResult();

      (obj.devices.os[info.os.name]) ? obj.devices.os[info.os.name]++: obj.devices.os[info.os.name] = 1;

      (obj.devices.browser[info.browser.name]) ? obj.devices.browser[info.browser.name]++: obj.devices.browser[info.browser.name] = 1;

      if (info.device.type) {
        (obj.devices.device[info.device.type]) ? obj.devices.device[info.device.type]++: obj.devices.device[info.device.type] = 1;
      } else {
        (obj.devices.device['computer']) ? obj.devices.device['computer']++: obj.devices.device['computer'] = 1;
      }
    };

    self.setMarkerInfo = function(nav, parser, country) {
      var info = {
        device: {
          type: undefined
        },
        browser: {
          name: undefined
        },
        cpu: {},
        os: {
          name: undefined
        }
      };

      if (nav) {
        info = parser.setUA(nav.userAgent).getResult();

        if (!info.device.type) {
          info.device = {
            type: 'computer'
          };
        }
      }

      if (info.device.type === 'computer') {
        info.color = '#0053a0';
      } else if (info.device.type === 'mobile') {
        info.color = '#a00053';
      } else if (info.device.type === 'tablet') {
        info.color = '#00a04d';
      } else {
        info.color = '#a04d00';
      }

      var profile = ['White Collar', 'Blue Collar'];

      var white_education = ['PHD', 'Masters', 'Bachelors'];
      var blue_education = ['Bachelors', 'High School'];

      var mStatus = ['Single', 'Married', 'Married with Kids'];

      info.tooltip = '<p><strong>Device: <\/strong>' + info.device.type + '<\/p>';
      info.tooltip += '<p><strong>OS: <\/strong>' + info.os.name;
      info.tooltip += '<br><strong>Browser: <\/strong>' + info.browser.name + '<\/p>';

      if (country === 'United States' || country === 'Canada') {
        var p = _.sample(profile);
        var e;
        if (p === profile[0]) {
          e = _.sample(white_education);
        } else {
          e = _.sample(blue_education);
        }
        info.tooltip += '<br><p><strong>Income: <\/strong>' + p;
        info.tooltip += '<br><strong>Education: <\/strong>' + e;
        info.tooltip += '<br><strong>Household Info: <\/strong>' + _.sample(mStatus) + '<\/p>';
      }
      //info.tooltip += '<p>' + info.os.type + '<\/p>';
      //info.tooltip += '<p>' + info.

      return info;
    };
  });
