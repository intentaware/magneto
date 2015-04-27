'use strict';

angular.module('adomattic.dashboard')
  .controller('SettingsFormCtrl', function($rootScope, $location, Company) {
    var self = this;
    self.company = $rootScope.globals.company;

    self.updateSettings = function () {
      console.log('i am here');
      Company.update(self.company).$promise.then(function () {
        $location.path('/');
      });
    };
  });
