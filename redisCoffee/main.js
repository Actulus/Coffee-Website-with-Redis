import './style.css'

fetch(`http://${import.meta.env.VITE_BACKEND_URL}:${import.meta.env.VITE_BACKEND_PORT}/getMenu`)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    const menu = document.getElementById('menu')
    let row = document.createElement('div')
    row.classList.add('row')
    data.forEach((item, index) => {
      // Create card element
      const card = document.createElement('div')
      card.classList.add('card')

      // Create image container
      const imgContainer = document.createElement('div')
      imgContainer.classList.add('image-container')

      // Create image element
      const img = document.createElement('img')
      img.src = item.img
      img.alt = item.name
      img.classList.add('coffee-image')

      // // Resize the image
      // img.style.width = '100%'
      // img.style.height = 'auto'

      imgContainer.appendChild(img)
      card.appendChild(imgContainer)

      // Create content container
      const content = document.createElement('div')
      content.classList.add('content')

      // Create name element
      const name = document.createElement('h2')
      name.textContent = item.name
      content.appendChild(name)

      // Create description element
      const description = document.createElement('p')
      description.textContent = item.description
      content.appendChild(description)

      card.appendChild(content)

      // Create price element
      const price = document.createElement('div')
      price.textContent = `$${item.price.toFixed(2)}`
      price.classList.add('price')
      card.appendChild(price)

      // Set background color
      card.style.backgroundColor = 'lightblue'

      // Append card to the current row
      row.appendChild(card)

      // Check if a new row needs to be created
      if ((index + 1) % 1 === 0) { // set grids
        menu.appendChild(row)
        row = document.createElement('div')
        row.classList.add('row')
      }
    })

    // Append the last row if it contains less than 3 cards
    if (row.children.length > 0) {
      menu.appendChild(row)
    }
  })
  .catch(err => console.log(err));
