'use strict';

angular.module('adomattic.dashboard')
  .service('Reporter', function() {
    var self = this;

    self.setUserAgentInfo = function(parser, ua, obj) {
      var info = parser.setUA(ua).getResult();

      (obj.devices.os[info.os.name]) ? obj.devices.os[info.os.name]++: obj.devices.os[info.os.name] = 1;

      (obj.devices.browser[info.browser.name]) ? obj.devices.browser[info.browser.name]++: obj.devices.browser[info.browser.name] = 1;

      if (info.device.type) {
        (obj.devices.device[info.device.type]) ? obj.devices.device[info.device.type]++: obj.devices.device[info.device.type] = 1;
      } else {
        (obj.devices.device['system-x86']) ? obj.devices.device['system-x86']++: obj.devices.device['system-x86'] = 1;
      }
    };
  });
