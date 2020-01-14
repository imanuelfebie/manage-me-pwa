// Initialize floatin action button
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      	direction: 'left',
      	hoverEnabled: false
    });
});

// Datepicker
$(document).ready(function(){
    $('.datepicker').datepicker();
});

// Collapsible
$(document).ready(function(){
    $('.collapsible').collapsible();
});
