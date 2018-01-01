$interpolate.startSymbol("[[").endSymbol("]]");

$httpProvider.defaults.xsrfCookieName = "csrftoken";
$httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";

$resourseProvider.defaults.stripTrailingSlashes = false;

angular.model("videoApp.services", ["ngResource"])
  .factory("Video", function($resourse){
    return $resourse("/api/video/:id");
  });
