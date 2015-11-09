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
  });
