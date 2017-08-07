(function (){

	var $mainNetworksFixed = $('.main_networks');
	var $networksListTitle = $('.networks_list__title');
	var $mainNetworksPostdetail = $('.main_networks_postdetail');
	var $getRandomImage = $('.get-random-image');

	$(window).on('scroll', scrolling);
	$getRandomImage.on('click', getImage);

	function getImage(e) {
		$getRandomImage.attr("disabled", true);
		$('.category__random-image').css("background-color", "A7A7A7");
		$.ajax({
			data: { categorySlug: categorySlug },
			url: '/get-random-image/',
			method: 'get',
			success: function (data) {
				$getRandomImage.attr("disabled", false);
				$('.category__random-image').css("background-color", "CD3232");
				var href = '/' + categorySlug + '/' + data.post_slug + '/' + data.image_slug + '/';
				$('#image-random-link').attr("href", href);
				$('#image-random-img').attr("src", data.image_url);
			}
		});
	}

	function scrolling(e) {
		var isPositionFixed = ($mainNetworksFixed.css('position') == 'fixed');
		if ($(this).scrollTop() > 200 && !isPositionFixed){ 
			$mainNetworksFixed.css({ 'display': 'block', 'position': 'fixed', 'top': '0px', width: '100%', 'z-index': 1}); 
			$networksListTitle.css({ 'display': 'none' });
		}
		if ($(this).scrollTop() < 200 && isPositionFixed) {
			$mainNetworksFixed.css({'position': 'static', 'top': '0px'}); 
			$networksListTitle.css({ 'display': 'block' });
			$mainNetworksPostdetail.css({ 'display': 'none' });
		}

	}

}());