

document.querySelector('.reviews-form').addEventListener('submit', (e) => {
    const formData = Object.fromEntries(new FormData(e.target).entries())
    handlerOrder(formData)
    e.preventDefault()
  });