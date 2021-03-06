$(document).ready(function() {
	$("#newsletterForm").submit(function(event){
		event.preventDefault();
		const userEmail = $('#userEmail').val();
		const userName = $('#userName').val();
		if (userEmail && userName) {
			var formData = new FormData();
			formData.append('email', userEmail);
			formData.append('name', userName);
			$.ajaxSetup({
				headers: {
					"X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
				}
			});
			$.ajax({
				url: '/newsletter/',
				type: 'POST',
				dataType: 'json',
				cache: false,
				processData: false,
				contentType: false,
				data: formData,
				error: function (res) {
					$('.result').append(res.msg);
				},
				success: function (res) {
					$('.result').append(res.msg);
					$('#userEmail').val(' ');
					$('#userName').val(' ');
				}
			})
		}
	});
});