function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function handlerOrder(formData) {
    axios.post(
        '/cart/create-order/',
        formData,
        {headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }}
    )
}

function handlerCartAddProduct(id) {
    axios.post(
        '/cart/add-product/',
        {id: id},
        {headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }}
    )
}

document.addEventListener('click' , ({target: {id , tagName, className}}) => {
    if(tagName === 'BUTTON' && className === 'product__item-add-button') {
        handlerCartAddProduct(id)
    }
})

document.querySelector('.order__item-form').addEventListener('submit', (e) => {
    const formData = Object.fromEntries(new FormData(e.target).entries())
    handlerOrder(formData)
    e.preventDefault()
  });
