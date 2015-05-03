'use strict';

angular.module('adomattic.dashboard')
  .factory('Circle', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'companies/circles/:id:doc/:list/',
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
    );
  });
