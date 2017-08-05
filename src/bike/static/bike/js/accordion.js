
$(function() {
    function close_sidebar_section() {
		$('.sidebar .sidebar-section-title').removeClass('active');
		$('.sidebar .sidebar-section-list').slideUp(300).removeClass('open');
	}

	$('.sidebar-section-title').click(function(e) {
		var currentAttrValue = $(this).attr('href');

		if($(e.target).is('.active')) {
			close_sidebar_section();
		}else {
			close_sidebar_section();

	    	$(this).addClass('active');
			$('.sidebar ' + currentAttrValue).slideDown(200).addClass('open');
		}

		e.preventDefault();
	});
});

$(function() {
    $( '.dropdown' ).hover(
        function(){
            $(this).children('.sub-menu').stop(true, false, true).slideDown(300);
        },
        function(){
            $(this).children('.sub-menu').stop(true, false, true).slideUp(300);
        }
    );
    });

$(function() {
    $('#panel').slideDown(1000);

});

$(function() {


});