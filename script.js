    // JS：点击标题，文字颜色随机变化
    
    const title = document.getElementById('title');
    title.addEventListener('click', function () {
      const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
      title.style.color = randomColor;

    });