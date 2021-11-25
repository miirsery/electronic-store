const marker = document.querySelector('.header__menu-marker')
const headerList = document.querySelectorAll('.header__menu-item')

function moveIndicator(e) {
    marker.style.left = e.offsetLeft + 'px'
    marker.style.width = e.offsetWidth + 'px'
}

function activeLink() {
    headerList.forEach((item) =>
        item.classList.remove('active'));
    this.classList.add('active');
    marker.style.opacity = 1
}
function removeActive() {
    marker.style.opacity = 0
}
headerList.forEach(item => item.addEventListener('mouseover', activeLink))
headerList.forEach(item => item.addEventListener('mouseout', removeActive))

headerList.forEach(link => {
    link.addEventListener('mousemove', (e) => {
        moveIndicator(e.target)
    })
})

const profileBtn = document.querySelector('.header__actions-profile')
profileBtn.addEventListener('click', menuToggle)
function menuToggle(){
    const toggleMenu = document.querySelector('.profile__menu')
    toggleMenu.classList.toggle('active')
}