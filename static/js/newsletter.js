const scriptURL = 'https://script.google.com/macros/s/AKfycbx-t8xfrKPMBA_yDJT2kPvfPqlbCmiPBuMIg2UIMX0cMmGZg8e3fc4EUeD3ZQlTT4IwHQ/exec'
			const form = document.forms['submit-to-google-sheet']
		
			form.addEventListener('submit', e => {
			  e.preventDefault()
			  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
				.then(response => console.log('Success!', response))
				.catch(error => console.error('Error!', error.message))
			})