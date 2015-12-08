'use strict';

angular.module('adomattic.dashboard')
  .factory('Asset', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'guages/assets/:id:list/:doc/',
      {
        id: '@id',
        doc: '@doc',
        list: '@list'
      }, {
        update: {
          method: 'PUT',
          isArray: false
        },
        patch: {
          method: 'PATCH',
          isArray: false
        },
        past: {
          method: 'GET',
          isArray: true,
          params: {
            list: 'past'
          }
        }
      }
    );
  });
