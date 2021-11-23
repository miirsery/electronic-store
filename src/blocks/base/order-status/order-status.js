const orderBtn = document.querySelector('#order__btn')
const statusMenu = document.querySelector('.status')

document.addEventListener('click', (e) => {
    // if (e.target !== orderBtn && e.target !== statusMenu && e.target !== document.querySelector('.status-block') && e.target !== document.querySelector('.status__number')) {
    //         statusMenu.style.opacity = 0
    //     statusMenu.style.visibility = 'hidden'
    // }
    if (e.target == orderBtn) {
        statusMenu.style.opacity = (statusMenu.style.opacity == 1) ? 0 : 1
        statusMenu.style.visibility = (statusMenu.style.visibility == 'visible') ? 'hidden' : 'visible'
    }
})