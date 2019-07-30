$(function () {

	// config
	let animationSpeed = 1000;
	let pause = 5000;
	let current_slide = 1;

	// DOM Cache
	let $slider = $('#slider');
	let $slideContainer = $slider.find('.slides');
	let $slides = $slideContainer.find('.slide');

	//Slider Interval for Play & Pause
	let interval;
	let slider_interval_status = true;

	//Play Slider Function
	function startSlider()
	{
		interval = setInterval(function ()
		{
			$slideContainer.animate(
				{'margin-left': '-=100%'}, animationSpeed, function ()
				{
					current_slide++;
					if (current_slide === $slides.length)
					{
						current_slide = 1;
						$slideContainer.css('margin-left', 0);
					}
					}
			);
		}, pause);
		slider_interval_status = true;
	}

	// //Pause Slider Function
	// function pauseSlider()
	// {
	// 	slider_interval_status = false;
	// 	clearInterval(interval);
	// }
	//
	// // 	Icon Play/Pause


	// Toggle Slider Play Status
	// $slider.on('click', function () {
	// 	if (!slider_interval_status)
	// 	{
	// 		$slider.find('#mid-box #slider-status').css({//'display': 'block',
	// 																	'background': 'background: url("files/pause-icon.png") no-repeat center',
	// 																	'transform': 'scale(2, 2)',
	// 																	'opacity': '0',
	// 																	});
	// 		startSlider();
	// 	}
	// 	else
	// 	{
	// 		$slider.find('#mid-box #slider-status').css({//'display': 'block',
	// 																	'background': 'background: url("files/play-icon.png") no-repeat center',
	// 																	'transform': 'scale(2, 2)',
	// 																	'opacity': '0',
	// 																	});
	// 		pauseSlider();
	// 	}
	// });
	//
	startSlider();

	function previousSlide()
	{
		let current_margin;
		if (current_slide === 1)
		{
			current_slide = $slides.length;
			current_margin = current_slide * (-100) + 100;
			$slideContainer.animate(
				{'margin-left': current_margin + '%', }, 0, 0
			);
			console.log(current_margin)
		}
		current_margin = current_slide * (-100) + 200;
		console.log(current_margin);
		current_slide--;
		$slideContainer.animate(
			{'margin-left': current_margin + '%'}, animationSpeed, 0
		);
	}

	function nextSlide()
	{
		let current_margin;
		current_margin = current_slide * (-100);
		current_slide++;
		$slideContainer.animate(
			{'margin-left': current_margin + '%'}, animationSpeed, 0
		);
		if (current_slide === $slides.length)
		{
			current_slide = 1;
			$slideContainer.animate(
				{'margin-left': 0, }, 0, 0
			);
		}
	}

	$('#previous').on('click', previousSlide);
	$('#next').on('click', nextSlide);


});