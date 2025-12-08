document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Сброс предыдущих ошибок
    hideAllErrors();
    
    // Валидация полей
    let isValid = validateForm();
    
    // Если форма валидна, показываем успешное сообщение
    if (isValid) {
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('contactForm').reset();
        setTimeout(() => {
            document.getElementById('successMessage').style.display = 'none';
        }, 5000);
    }
});

function validateForm() {
    let isValid = true;
    
    // Проверка обязательных полей
    const firstName = document.getElementById('firstName');
    if (!firstName.value.trim()) {
        showError('firstNameError', 'Поле обязательно для заполнения');
        isValid = false;
    }
    
    const lastName = document.getElementById('lastName');
    if (!lastName.value.trim()) {
        showError('lastNameError', 'Поле обязательно для заполнения');
        isValid = false;
    }
    
    const email = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value.trim()) {
        showError('emailError', 'Поле обязательно для заполнения');
        isValid = false;
    } else if (!emailRegex.test(email.value)) {
        showError('emailError', 'Введите корректный email адрес');
        isValid = false;
    }
    
    const birthdate = document.getElementById('birthdate');
    if (!birthdate.value) {
        showError('birthdateError', 'Поле обязательно для заполнения');
        isValid = false;
    } else {
        // Дополнительная проверка даты рождения (возраст не менее 18 лет)
        const birthDate = new Date(birthdate.value);
        const today = new Date();
        const age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        
        if (age < 18) {
            showError('birthdateError', 'Регистрация разрешена с 18 лет');
            isValid = false;
        }
    }
    
    const agreement = document.getElementById('agreement');
    if (!agreement.checked) {
        showError('agreementError', 'Необходимо принять условия');
        isValid = false;
    }
    
    return isValid;
}

function showError(errorElementId, message) {
    const errorElement = document.getElementById(errorElementId);
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}

function hideAllErrors() {
    const errorElements = document.querySelectorAll('.error-message');
    errorElements.forEach(element => {
        element.style.display = 'none';
    });
    document.getElementById('successMessage').style.display = 'none';
}

// Валидация телефона в реальном времени
document.getElementById('phone').addEventListener('input', function(e) {
    const phone = e.target.value.replace(/\D/g, '');
    const formattedPhone = formatPhoneNumber(phone);
    e.target.value = formattedPhone;
});

function formatPhoneNumber(phone) {
    if (!phone) return '';
    
    if (phone.length === 0) return '';
    if (phone.length <= 3) return `+7 (${phone}`;
    if (phone.length <= 6) return `+7 (${phone.slice(0, 3)}) ${phone.slice(3)}`;
    if (phone.length <= 8) return `+7 (${phone.slice(0, 3)}) ${phone.slice(3, 6)}-${phone.slice(6)}`;
    return `+7 (${phone.slice(0, 3)}) ${phone.slice(3, 6)}-${phone.slice(6, 8)}-${phone.slice(8, 10)}`;
}

// Добавляем ручную валидацию для поля даты при изменении
document.getElementById('birthdate').addEventListener('change', function() {
    hideAllErrors();
    validateForm();
});