// login.js - Har safar yangi matematik masala yaratish

// 1. Matematik masala yaratish funksiyasi
function createMathProblem() {
    // Amallar ro'yxati (faqat + va -)
    var operations = ['+', '-'];
    
    // Tasodifiy amal tanlash
    var operation = operations[Math.floor(Math.random() * operations.length)];
    
    // O'zgaruvchilar
    var num1, num2, correctAnswer;
    
    // Qo'shish amali uchun
    if (operation === '+') {
        // Birinchi son: 1 dan 20 gacha
        num1 = Math.floor(Math.random() * 20) + 1;
        // Ikkinchi son: 1 dan 20 gacha
        num2 = Math.floor(Math.random() * 20) + 1;
        // To'g'ri javob
        correctAnswer = num1 + num2;
    }
    // Ayirish amali uchun
    else {
        // Birinchi son: 10 dan 30 gacha
        num1 = Math.floor(Math.random() * 20) + 10;
        // Ikkinchi son: 1 dan 10 gacha
        num2 = Math.floor(Math.random() * 10) + 1;
        
        // Manfiy javob chiqmasligi uchun
        if (num2 > num1) {
            var temp = num1;
            num1 = num2;
            num2 = temp;
        }
        
        // To'g'ri javob
        correctAnswer = num1 - num2;
    }
    
    // Masalani ekranga chiqarish
    document.getElementById('mathProblem').innerHTML = 
        '<strong>' + num1 + ' ' + operation + ' ' + num2 + ' = ?</strong>';
    
    // To'g'ri javobni saqlash (maxfiy, foydalanuvchiga ko'rinmaydi)
    document.getElementById('mathAnswer').dataset.correct = correctAnswer;
    
    // Console'da ko'rish uchun
    console.log('Yangi masala: ' + num1 + ' ' + operation + ' ' + num2 + ' = ' + correctAnswer);
}

// 2. Sahifa yuklanganda yangi masala yaratish
window.onload = function() {
    // Birinchi masalani yaratish
    createMathProblem();
    
    // Forma yuborilganda tekshirish
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        // Sahifa yangilanmasligi uchun
        event.preventDefault();
        
        // Foydalanuvchi javobini olish
        var userAnswer = document.getElementById('mathAnswer').value;
        var correctAnswer = document.getElementById('mathAnswer').dataset.correct;
        
        // Javoblarni raqamga o'tkazish
        userAnswer = parseInt(userAnswer);
        correctAnswer = parseInt(correctAnswer);
        
        // Javobni tekshirish
        if (userAnswer === correctAnswer) {
            // To'g'ri javob
            alert('✅ To\'g\'ri javob! Tizimga kiring.');
            // index.html sahifasiga o'tish
            window.location.href = 'index.html';
        } else {
            // Noto'g'ri javob
            alert('❌ Noto\'g\'ri javob! Yangi masala yeching.');
            // Yangi masala yaratish
            createMathProblem();
            // Javob maydonini tozalash
            document.getElementById('mathAnswer').value = '';
            // Kursorni javob maydoniga qaytarish
            document.getElementById('mathAnswer').focus();
        }
    });
    
    // Har 20 soniyada yangi masala (agar foydalanuvchi uzoq kutib qolsa)
    setInterval(function() {
        if (document.getElementById('mathAnswer').value === '') {
            createMathProblem();
        }
    }, 20000);
};

// 3. Qo'shimcha: Sahifa har yangilanganda yangi masala
window.onbeforeunload = function() {
    createMathProblem();
};