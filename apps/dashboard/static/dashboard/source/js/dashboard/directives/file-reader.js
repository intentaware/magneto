'use strict';

angular.module('adomattic.dashboard')
  .directive('readFile', ['$q', 'urls', function($q, urls) {
    return {
      restrict: 'E',
      scope: {
        label: '@',
        accept: '@',
        maxSize: '@',
        ngModel: '=',
      },
      templateUrl: urls.partials.directives + 'file-reader.html',
      replace: true,
      require: '^ngModel',
      link: function(scope, elm, atr, ngModelCtrl) {
        ngModelCtrl.$render = function() {};
        //scope.fileName = '';
        var $file = elm[0].querySelector('.overlay');
        console.log($file);

        // watch for a new file in input
        $file.onchange = function(e) {
          var el = e.target;
          console.log(el.value);

          if (!el.value) {
            return;
          }

          //scope.apply();
          var name = el.files[0].name;

          $q.all(Array.prototype.slice.call(el.files, 0).map(read))
            .then(function(vals) {
              scope.fileName = name;
              // ng-model contains the binary value, file the file name is the view value
              ngModelCtrl.$setViewValue(vals.length ? vals[0] : null);
            }, function() {
              scope.fileName = 'Unable to load file, please try again';
              //scope.$apply();
            });
        };

        // return the file contents in base64 format
        var read = function(f) {
          var d = $q.defer();
          var size = parseInt(scope.maxSize);
          console.log(size);
          console.log(f.size);

          if (parseInt(scope.maxSize) <= f.size) {
            d.reject();
          } else {

            var r = new FileReader();

            r.onload = function(ev) {
              d.resolve(ev.target.result);
            };

            r.onerror = function(ev) {
              d.reject(ev);
            };

            r.readAsDataURL(f);
          }

          return d.promise;
        };

      }
    };
  }]);
