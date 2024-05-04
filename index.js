function handleNavIconClick(item) {
    $(`#${item}`)[0].scrollIntoView();
}

function handleContactIconClick(item) {
    window.open(
        item === "gmail"
            ? "mailto:er.gupta.arpit@gmail.com"
            : item === "linkedin"
                ? "https://www.linkedin.com/in/er-arpit-gupta"
                : "https://github.com/er-arpitgupta"
    );
}

function handleFilterClick(item) {
    $('.filters label').removeClass('active')
    $(`.filters label[for="${item}"]`).addClass('active')
}

function handleImageClick(image) {
    $('.popup img').attr('src', `images/high_images/${image}.jpg`);
    $('.popup').css('display', 'flex');
}

function handlePopupClose() {
    $('.popup').css('display', 'none');
}