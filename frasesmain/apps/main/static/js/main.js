(function (){
	var $images = $('.article__image');
	var $close = $('.close');
	var $arrowRight = $('.arrow_right');
	var $arrowLeft = $('.arrow_left');
	var $img = $('.modal__left_side__image');
	var $modal = $('.modal');
	var $downloadButton = $('.download_button__link');
	var $imageDescription = $('.image__description');
	var $mainNetworksPostdetail = $('.main_networks_postdetail');
	var $linkToImage = $('.link_to_image');
	var $facebookShare = $('#fb-share');

	var currentNumber;

	$images.on('click', clicked);
	$close.on('click', closeModal);
	$arrowRight.on('click', nextImage);
	$arrowLeft.on('click', previousImage);
	$downloadButton.on('click', downloadImagen);

	$(document).keyup(function(e) {
		if (e.keyCode == 27) { // escape key maps to keycode `27`
			closeModal();
		}
		if (e.keyCode == 37) {
			previousImage();
		}
		if (e.keyCode == 39) {
			nextImage();
		}
	});

	function downloadImagen(e) {
		ga('send', {
		  hitType: 'event',
		  eventCategory: 'Image',
		  eventAction: 'download',
		  eventLabel: 'Download Image'
		});	
	}

	function setDataToModal(url, title, imageSlug) {
		$img.attr('src', url);
		$linkToImage.text(title);
		$linkToImage.attr('href', imageSlug);
		$downloadButton.attr('href', url);
		$facebookShare.data('href', currentUrl + imageSlug);
	}

	function clicked(e) {
		var url = e.target.src;
		var title = e.target.title;
		currentNumber = Number(e.target.dataset.number);
		var imageSlug = e.target.dataset.slug;
		setDataToModal(url, title, imageSlug);
		$modal.css('display', 'block');
		$mainNetworksPostdetail.css({ 'display': 'none' });
		ga('send', {
		  hitType: 'event',
		  eventCategory: 'Image',
		  eventAction: 'click',
		  eventLabel: 'Open Image Modal'
		});
	}

	function closeModal(e) {
		$mainNetworksPostdetail.css({ 'display': 'block' });
		$('.modal').css('display', 'none');
	}

	function nextImage(e) {
		if (currentNumber !== numberOfImages) {
			var url = $('#image' + (currentNumber + 1)).attr('src');
			var title = $('#image' + (currentNumber + 1)).attr('title');
			var imageSlug = $('#image' + (currentNumber + 1)).data('slug');
			setDataToModal(url, title);
			currentNumber += 1;
		}
	}

	function previousImage(e) {
		if (currentNumber !== 1) {
			var url = $('#image' + (currentNumber - 1)).attr('src');
			var title = $('#image' + (currentNumber - 1)).attr('title');
			var imageSlug = $('#image' + (currentNumber - 1)).data('slug');
			setDataToModal(url, title, imageSlug);
			currentNumber -= 1;
		}
	}


}());