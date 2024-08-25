const loader = document.querySelector('.loader');

// select inputs
const submitBtn = document.querySelector('.submit-btn');
const name = document.querySelector('#name') || null;
const username = document.querySelector('#username');
const password = document.querySelector('#password');
const number = document.querySelector('#number') || null;
const tac = document.querySelector('#terms-and-cond') || null;
const notification = document.querySelector('#notification') || null;

submitBtn.addEventListener('click', () => {
  if(name != null){ // sign up page
    if(name.value.length < 3) {
      showAlert('name must be 3 letters long');
    } else if (!username.value.length) {
      showAlert('enter your username');
    } else if (password.value.length < 8) {
      showAlert('password should be 8 letters long');
    } else if (!number.value.length) {
      showAlert('enter your phone number');
    } else if (!Number(number.value) || number.value.length < 10) {
      showAlert('invalid number, please enter a valid one');
    } else if (!tac.checked) {
      showAlert('you must agree to our terms and conditions');
    } else {
      //submit form
      loader.style.display = 'block';
      sendData('/signup', {
        name: name.value,
        username: username.value,
        password: password.value,
        number: number.value,
        tac: tac.checked,
        notification: notification.checked,
        seller: false
      })
    }
  } else {
    // login page
    if (!username.value.length || !password.value.length){
      showAlert('fill all the inputs');
    } else {
      loader.style.display = 'block';
      sendData('/login', {
        username: username.value,
        password: password.value,
      })
    }
  }
})


// send data function
const sendData = (path, data) => {
  fetch (path, {
    method: 'post',
    headers: new Headers({'Content-Type': 'application/json'}),
    body: JSON.stringify(data)
  }).then((res) => res.json())
  .then(response => {
    console.log(response);
  });
};

//alert function
const showAlert = (msg) => {
  let alertBox = document.querySelector('.alert-box');
  let alertMsg = document.querySelector('.alert-msg');
  alertMsg.innerHTML = msg;
  alertBox.classList.add('show');
  setTimeout(() => {
    alertBox.classList.remove('show');
  }, 3000);
}