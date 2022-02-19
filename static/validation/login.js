

const email = document.getElementById('email');
const password = document.getElementById('password');
const form = document.getElementById('formm');
const invalid = document.getElementById('invalid');
const show = document.getElementById('show');
const hide = document.getElementById('hide');


form.addEventListener('submit',(e) => {

    if(email.value === '' || email.value == null){
        invalid.style.visibility = 'visible';
        

        e.preventDefault();
        return;
    }

    if(password.value.length <= 6){
        console.log('password must contain more than 6 characters');
        alert('password must contain more than 6 characters');
        e.preventDefault();
    }
    else{
        alert('Login Successful!')
    }
});

function toggleShow(){
    show.style.visibility = 'hidden';
    hide.style.visibility = 'visible';
    password.type = 'password';
    
}
function toggleHide(){
    hide.style.visibility = 'hidden';
    show.style.visibility = 'visible';
    password.type = 'text';
    
}

