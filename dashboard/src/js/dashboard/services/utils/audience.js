'use strict';

angular.module('adomattic.dashboard')
  .service('AudienceManager', function() {
    var self = this;

    self.getAges = function(min) {
      min = min || null;
      var range = min ? _.range(min, 99) : _.range(13, 99);

      return range;
    };

    self.getJobs = function() {
      return ['White Collar', 'Blue Collar', 'All'];
    };

    self.getEducation = function() {
      return ['High School', 'Bachelors', 'Post Graduate', 'PHD', 'All'];
    };

    self.getCommuteChoices = function() {
      return ['Walks', 'Rides a Bus', 'Car Pool', 'Drives Alone', 'All'];
    };

    self.getRelationshipStatus = function() {
      return ['Married', 'Single', 'Divorced', 'All'];
    };
  });
