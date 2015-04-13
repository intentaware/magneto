'use strict';

angular.module('adomattic.dashboard')
  .controller('SettingsFormCtrl', function($rootScope) {
    var self = this;
    self.company = $rootScope.globals.company
  });
