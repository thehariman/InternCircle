/* =========================================
   InternCircle – login.js
   ========================================= */

'use strict';

const form      = document.getElementById('loginForm');
const submitBtn = document.getElementById('submitBtn');
const btnText   = submitBtn.querySelector('.btn-text');
const btnLoader = submitBtn.querySelector('.btn-loader');

const validations = {
  email: {
    el: document.getElementById('email'),
    err: document.getElementById('emailError'),
    validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Please enter a valid email address.'
  },
  password: {
    el: document.getElementById('password'),
    err: document.getElementById('passwordError'),
    validate: v => v.length >= 6 ? '' : 'Password must be at least 6 characters.'
  }
};

function validateField(key) {
  const cfg = validations[key];
  const msg = cfg.validate(cfg.el.value);
  cfg.err.textContent = msg;
  cfg.el.classList.toggle('invalid', msg !== '');
  cfg.el.classList.toggle('valid',   msg === '');
  return msg === '';
}

// Live validation on blur
Object.keys(validations).forEach(key => {
  validations[key].el.addEventListener('blur', () => validateField(key));
  validations[key].el.addEventListener('input', () => {
    if (validations[key].el.classList.contains('invalid')) validateField(key);
  });
});

form.addEventListener('submit', function (e) {
  e.preventDefault();

  let isValid = true;
  Object.keys(validations).forEach(key => {
    if (!validateField(key)) isValid = false;
  });

  if (!isValid) return;

  // Mock sign-in loader
  btnText.style.display = 'none';
  btnLoader.style.display = 'block';
  submitBtn.disabled = true;

  setTimeout(() => {
    alert('Logged in successfully! Redirecting you to home page...');
    window.location.href = 'index.html';
  }, 1500);
});

console.log('%c🔑 InternCircle Student Login Loaded', 'color:#06b6d4; font-weight:bold;');
