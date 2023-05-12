const form = document.querySelector('form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
	event.preventDefault();

	const romFile = document.getElementById('rom').files[0];
	const modFile = document.getElementById('mod').files[0];

	if (!romFile || !modFile) {
		showError('Please select both a ROM file and a mod file.');
		return;
	}

	if (romFile.type !== 'application/octet-stream' || modFile.type !== 'application/octet-stream') {
		showError('Please select valid binary files.');
		return;
	}

	try {
		const formData = new FormData();
		formData.append('rom', romFile);
		formData.append('mod', modFile);

		const response = await fetch('/upload', {
			method: 'POST',
			body: formData
		});

		if (response.ok) {
			const blob = await response.blob();
			const url = URL.createObjectURL(blob);
			const link = document.createElement('a');
			link.href = url;
			link.download = 'smw_modded.smc';
			link.textContent = 'Download patched ROM file';
			resultDiv.appendChild(link);
		} else {
			showError(`Server error: ${response.status} ${response.statusText}`);
		}
	} catch (error) {
		showError(`Network error: ${error.message}`);
	}
});

function showError(message) {
	resultDiv.innerHTML = '';
	const errorDiv = document.createElement('div');
	errorDiv.id = 'error';
	errorDiv.textContent = message;
	resultDiv.appendChild(errorDiv);
}