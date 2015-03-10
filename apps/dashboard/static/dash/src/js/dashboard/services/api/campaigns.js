'use strict';

angular.module('adomattic.dashboard')
  .factory('Campaign', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'campaigns/campaigns/:id:doc/:list/',
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
