// Side bar initialization
document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidebar);
  });

// Model
document.addEventListener('DOMContentLoaded', function() {
  var model = document.querySelectorAll('.modal');
  M.Modal.init(model);
})