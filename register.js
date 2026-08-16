/* =========================================
   InternCircle – register.js
   ========================================= */

'use strict';

// ── Form validation & submission ──
const form        = document.getElementById('registrationForm');
const submitBtn   = document.getElementById('submitBtn');
const btnText     = submitBtn.querySelector('.btn-text');
const btnLoader   = submitBtn.querySelector('.btn-loader');
const successModal = document.getElementById('successModal');
const closeModal  = document.getElementById('closeModal');

const validations = {
  firstName : { el: null, err: null, validate: v => v.trim().length >= 2 ? '' : 'First name must be at least 2 characters.' },
  lastName  : { el: null, err: null, validate: v => v.trim().length >= 2 ? '' : 'Last name must be at least 2 characters.' },
  email     : { el: null, err: null, validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Please enter a valid email address.' },
  phone     : { el: null, err: null, validate: v => /^\d{10}$/.test(v) ? '' : 'Enter a valid 10-digit mobile number.' },
  college   : { el: null, err: null, validate: v => v.trim().length >= 3 ? '' : 'Please enter your college name.' },
  course    : { el: null, err: null, validate: v => v !== '' ? '' : 'Please select your course.' },
  year      : { el: null, err: null, validate: v => v !== '' ? '' : 'Please select your year of study.' },
  domain    : { el: null, err: null, validate: v => v !== '' ? '' : 'Please choose an internship domain.' },
  state     : { el: null, err: null, validate: v => v !== '' ? '' : 'Please select your state.' },
};

// Bind elements
Object.keys(validations).forEach(key => {
  validations[key].el  = document.getElementById(key);
  validations[key].err = document.getElementById(`${key}Error`);
});

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

// Phone – digits only
document.getElementById('phone').addEventListener('input', function () {
  this.value = this.value.replace(/\D/g, '').slice(0, 10);
});

form.addEventListener('submit', function (e) {
  e.preventDefault();

  // Validate all fields
  let isValid = true;
  Object.keys(validations).forEach(key => {
    if (!validateField(key)) isValid = false;
  });



  if (!isValid) {
    // Scroll to first invalid field
    const firstInvalid = form.querySelector('.invalid');
    if (firstInvalid) firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
    return;
  }

  // Simulate submission
  btnText.style.display = 'none';
  btnLoader.style.display = 'block';
  submitBtn.disabled = true;

  setTimeout(() => {
    btnText.style.display = 'block';
    btnLoader.style.display = 'none';
    submitBtn.disabled = false;
    form.reset();
    Object.keys(validations).forEach(key => {
      validations[key].el.classList.remove('valid', 'invalid');
      validations[key].err.textContent = '';
    });

    showModal();
  }, 1800);
});

function showModal() {
  successModal.classList.add('active');
  document.body.style.overflow = 'hidden';
}
function hideModal() {
  successModal.classList.remove('active');
  document.body.style.overflow = '';
}

closeModal.addEventListener('click', hideModal);
successModal.addEventListener('click', e => {
  if (e.target === successModal) hideModal();
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') hideModal();
});

// Auto-select domain from query parameter
window.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const domainParam = urlParams.get('domain');
  if (domainParam) {
    const domainSelect = document.getElementById('domain');
    if (domainSelect) {
      // Normalize parameter and match against options
      const normalizedParam = domainParam.toLowerCase().replace(/[^a-z0-9]/g, '');
      for (let i = 0; i < domainSelect.options.length; i++) {
        const optionText = domainSelect.options[i].text.toLowerCase().replace(/[^a-z0-9]/g, '');
        const optionValue = domainSelect.options[i].value.toLowerCase().replace(/[^a-z0-9]/g, '');
        if (optionText === normalizedParam || optionValue === normalizedParam) {
          domainSelect.selectedIndex = i;
          validateField('domain');
          break;
        }
      }
    }
  }
});

console.log('%c📝 InternCircle Registration Page Loaded', 'color:#1a56e8; font-weight:bold;');
