const ordersItemEstimate = document.querySelector('.orders__item-estimate')
document.querySelector('.orders__item-raitingbtn').addEventListener('click', (e) => {
    console.log(e.target);
    ordersItemEstimate.classList.toggle('orders__item-estimate--active')
})
