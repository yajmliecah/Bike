/* dropdown menu and dropdown for sidebar filter menu */

$(document).ready(function() {
    $( '.dropdown' ).hover(
        function(){
            $(this).children('.sub-menu').slideDown(100);
        },
        function(){
            $(this).children('.sub-menu').slideUp(100);
        }
    );
}); // end ready});