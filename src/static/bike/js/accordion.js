
jQuery(document).ready(function() {
    function close_sidebar_section() {
		jQuery('.sidebar .sidebar-section-title').removeClass('active');
		jQuery('.sidebar .sidebar-section-list').slideUp(300).removeClass('open');
	}

	jQuery('.sidebar-section-title').click(function(e) {
		var currentAttrValue = jQuery(this).attr('href');

		if(jQuery(e.target).is('.active')) {
			close_sidebar_section();
		}else {
			close_sidebar_section();

	    	jQuery(this).addClass('active');
			jQuery('.sidebar ' + currentAttrValue).slideDown(200).addClass('open');
		}

		e.preventDefault();
	});
});