const sortSelect = document.getElementById('select-sort');
// const list = document.getElementById('list');

sortSelect.addEventListener('change', function (list) {
    const selectedValue = this.value;
    const items = Array.from(list.querySelectorAll('li'));

    switch (selectedValue) {
        // Xếp tên A - Z
        case 'incName':
            items.sort((a, b) => a.innerText.localeCompare(b.innerText));
            break;

        // Xếp tên Z - A
        case 'desName':
            items.sort((a, b) => b.innerText.localeCompare(a.innerText));
            break;

        // Xếp giá tăng dần
        case 'descending':
            items.sort((a, b) => b.innerText.localeCompare(a.innerText));
            break;

        // Xếp giá giảm dần
        case 'descending':
            items.sort((a, b) => b.innerText.localeCompare(a.innerText));
            break;

        // Xếp ngày xuất bản giảm dần
        case 'descending':
            items.sort((a, b) => b.innerText.localeCompare(a.innerText));
            break;

        // Xếp ngày xuất bản tăng dần
        case 'descending':
            items.sort((a, b) => b.innerText.localeCompare(a.innerText));
            break;

        // Mặc định
        default:
            // Do nothing
            break;
    }

    list.innerHTML = '';
    items.forEach(item => list.appendChild(item));
});