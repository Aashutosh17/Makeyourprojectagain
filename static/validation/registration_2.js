
const form = document.getElementById('form');
const username = document.getElementById('username')
const password = document.getElementById('password')
const password_c = document.getElementById('password_c')
const email = document.getElementById('email')

form.addEventListener('submit',(e) => {
    if(checkInputs()){
        alert('Validation Completed! Please click "OK" to proceed into login session.')
    }
    else{
        e.preventDefault();
    }
    // if(message.length == 1){
    //     alert('OK')
    //     console.log('successful!')
    // }
    // else{
    //     console.log('Unsuccessful!')
    //     e.preventDefault();
    // }
    // if(username.value === '' || username.value == null){
    //     alert('wrong!')
    // }

});

function checkInputs(){
    // get the values from the inputs.
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passValue = password.value.trim();
    const pass_cValue = password_c.value.trim();


    if(usernameValue === ''){
        // show error
        // add error class
        setErrorfor(username, 'Username cannot be empty!');

    }
    else{
        // success class
        setsuccessfor(username);
    }

    if(emailValue === ''){
        setErrorfor(email,'Email cannot be empty!')
    }
    else if(!isEmail(emailValue)){
        setErrorfor(email,'Email is not valid!')
        
    }
    else{
        setsuccessfor(email);        
    }

    if(passValue.length >= 6){
        if(passValue.length <= 20){
            if(passValue === pass_cValue){
                setsuccessfor(password);
                setsuccessfor(password_c);
                
            }
            else{
                setErrorfor(password,'Password did not match!')
                setErrorfor(password_c,'Password did not match!')
            }
        }
        else{
            setErrorfor(password,'Password must contain less than 20 characters')
        }
    }
    else{
            setErrorfor(password,'Password must contain more than 6 characters')
    }

    

    if(usernameValue !== '' && emailValue !== '' && passValue.length >= 6 && passValue.length <= 20 && passValue === pass_cValue ){
        console.log('ok!')
        return true;
    }
    else{
        return false;
    }
}

// For error
function setErrorfor(input, message){
    const formControl = input.parentElement; // formControl
    const small = formControl.querySelector('small');

    // add error message iside small
    small.innerText = message;

    // add error message
    formControl.className = 'form-control error';
    
}

// For valid.
function setsuccessfor(input){
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
}

// For valid Email.
function isEmail(email){
    return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email);
}



