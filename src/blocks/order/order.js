let patterns = {
    notEmpty: /.+/,
    phone: /^\d{7,15}$/,
    email: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/i
}

const form = document.querySelector('.order__item-form')
let inputs = document.querySelectorAll('.order__item-input')
let errorArea = document.querySelector('.order__bottom-error')
form.addEventListener('submit', (e) => {

    let hasError = false

    for (let i = 0; i < inputs.length; i++) {
        let inp = inputs[i]
        let val = inp.value.trim()
        let name = inp.dataset.valid
        let pattern = patterns[name]
        if (!pattern.test(val)) {
            inputs[i].classList.add('err')
            hasError = true
        }
        if (hasError) {
            e.preventDefault()
            errorArea.innerHTML = 'Заполните все поля'
        }
    }
})