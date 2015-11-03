'use strict';

angular.module('adomattic.dashboard')
  .factory('Circle', ['$resource', 'urls', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'metas/circles/:id:list/:doc/',
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
  }]);
