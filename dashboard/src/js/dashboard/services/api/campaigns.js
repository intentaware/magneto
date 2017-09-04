'use strict';

angular.module('adomattic.dashboard')
  .factory('Campaign', function ($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'campaigns/campaigns/:id:list/:doc/',
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
        },
        impressions: {
          method: 'GET',
          isArray: true,
          params: {
            doc: 'impressions'
          }
        }
      }
    );
  });
