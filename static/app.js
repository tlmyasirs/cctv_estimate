document.addEventListener('DOMContentLoaded', () => {
    const nvrSelect = document.getElementById('nvr');
    const hddSelect = document.getElementById('hdd');
    const camCheckboxes = document.querySelectorAll('.cam-checkbox');
    const slider = document.getElementById('storageSlider');
    const storageValue = document.getElementById('storageValue');
    const totalEl = document.getElementById('total');

    function updateTotal() {
        let total = 0;
        total += parseFloat(nvrSelect.value || 0);
        total += parseFloat(hddSelect.value || 0);
        camCheckboxes.forEach(cb => {
            if (cb.checked) {
                total += parseFloat(cb.value);
            }
        });
        total += parseInt(slider.value);
        totalEl.textContent = total.toFixed(2);
    }

    nvrSelect.addEventListener('change', updateTotal);
    hddSelect.addEventListener('change', updateTotal);
    camCheckboxes.forEach(cb => cb.addEventListener('change', updateTotal));
    slider.addEventListener('input', () => {
        storageValue.textContent = slider.value;
        updateTotal();
    });

    updateTotal();
});
