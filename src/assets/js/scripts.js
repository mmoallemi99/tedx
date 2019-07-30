$(function () {

	// DOM Cache
	let navbar = $('.main_nav ul li');
	let current_tab = $('#item-1');
	let tabs_count = navbar.length;
	let tab_width = navbar.css('width');
	tab_width = tab_width.replace(/[^-\d\.]/g, '');
	let nav_open = $('#toggle');
	let nav_close = $('#close_nav');
	let mobile_nav = $('.mobile_nav');
	let body = $('.flip-card');
	let inside_body = $('.flip-card-inner');
	$(window).on('resize', function () {
		tab_width = navbar.css('width');
		tab_width = tab_width.replace(/[^-\d\.]/g, '');
	});

	// Nav
	let pathname = window.location.pathname;
	for (let i = 0; i < tabs_count; i++) {
		let li_value = navbar.eq(i).text().trim();
		if (pathname.indexOf(li_value) !== -1) {
			let left = (40 + i * tab_width) + 'px';
			current_tab.css({'left': left, 'transition': 'none', 'display': 'block'});
		} else if (pathname === '/') {
			current_tab.css({'left': '40px', 'transition': 'none', 'display': 'block'});
		}
	}
	let current_tab_location = current_tab.css('left');
	for (let i = 0; i < tabs_count; i++) {
		navbar.eq(i).hover(function () {
			let left = (40 + i * tab_width) + 'px';
			current_tab.css({'left': left, 'transition': 'left 300ms'});
		});
		navbar.eq(i).mouseleave(function () {
			current_tab.css({'left': current_tab_location, 'transition': 'left 300ms'});
		});
	}
	function open_nav()
	{
			body.css('transform', 'rotateY(45deg)');
			inside_body.css({
				'transform': 'rotateY(45deg)',
				'left': '-25%',
			});
			mobile_nav.show();
			mobile_nav.animate({
				'width': '44%',
			}, 1);
	}
	function close_nav()
	{
		body.css('transform', 'rotateY(0deg)');
		inside_body.css({
			'transform': 'rotateY(0deg)',
			'left': '0',
		});
		mobile_nav.animate({
			'width': '0',
		}, 1);
		mobile_nav.hide();

	}
	nav_open.on('click', open_nav);
	nav_close.on('click', close_nav);
	
	$('#id_professions').attr('placeholder', 'Please Describe Yourself...');
	// nav_toggle.on('click', function () {
	//     $('.flip-card').css('transform','rotateY(45deg)');
	//     $('.flip-card-inner').css({
	//         'transform': 'rotateY(45deg)',
	//         'left': '-25%',
	//     });
	//     $('.mobile_nav').css({
	//         'display': 'block',
	//         'width': '44%',
	//     });
	// });


	// Nav

	// //Modal Box
	// $(".box-top").on("click", function () {
	//     $(this).parent().siblings(".sponsor-box-bg").show();
	//     $(this).parent().siblings(".sponsor-box-bg").css("opacity", "0.95");
	// });
	// $(".sponsor-box .close").on("click", function () {
	//     $(this).parents(".sponsor-box-bg").fadeOut(250, function () {
	//         $(this).parents(".sponsor-box-bg").hide();
	//     });
	// });
	// $(".sponsor-box-bg").click(function (event) {
	//     if (event.target.className === "sponsor-box-bg") {
	//         $(this).hide();
	//         $(this).css("opacity", "0");
	//     }
	// });
	// //Modal Box
});
