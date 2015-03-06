'use strict';

angular.module('adomattic.dashboard')
  .factory('Ad', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'ads/:id:doc/:list/',
      {
        id: '@id',
        doc: '@doc',
        list: '@list'
      }, {
        update: {
          method: 'PUT',
          isArray: false
        }
      }
    )
  });
