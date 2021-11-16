document.addEventListener('click' , ({target: {id , tagName, className}}) => {
    if(tagName === 'BUTTON' && className === 'product__item-add-button') {
        console.log(id)
    }
})