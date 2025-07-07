document.getElementById('downloadBtn').addEventListener('click', function() {
  const card = document.getElementById('gameCard');
  html2canvas(card, {
    scale: 1,
    width: 1120,
    height: 1680,
    useCORS: true
  }).then(canvas => {
    // If the canvas is not the right size, resize it manually
    if (canvas.width !== 1120 || canvas.height !== 1680) {
      const resizedCanvas = document.createElement('canvas');
      resizedCanvas.width = 1120;
      resizedCanvas.height = 1680;
      const ctx = resizedCanvas.getContext('2d');
      ctx.drawImage(canvas, 0, 0, 1120, 1680);
      canvas = resizedCanvas;
    }
    const link = document.createElement('a');
    link.download = 'game-card.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  });
});

document.getElementById('downloadPdfBtn').addEventListener('click', function() {
  const card = document.getElementById('gameCard');
  html2canvas(card, {
    scale: 1,
    width: 1120,
    height: 1680,
    useCORS: true
  }).then(canvas => {
    const imgData = canvas.toDataURL('image/png');
    // jsPDF uses points (1 pt = 1/72 inch). At 96dpi, 1 px = 0.75 pt
    const pdfWidth = 1120 * 0.75;
    const pdfHeight = 1680 * 0.75;
    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'pt',
      format: [pdfWidth, pdfHeight]
    });
    pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
    pdf.save('game-card.pdf');
  });
});

document.getElementById('loadCardBtn').addEventListener('click', function() {
  fetch('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
    .then(response => response.json())
    .then(data => {
      // Use the first member as the card example
      const member = data.members[0];
      document.getElementById('cardName').textContent = member.name;
      // Example: 3 blue mana icons
      const manaCost = document.getElementById('manaCost');
      manaCost.innerHTML = '';
      for (let i = 0; i < 3; i++) {
        const img = document.createElement('img');
        img.src = 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Mana_Blue.png';
        img.alt = 'Blue Mana';
        img.className = 'mana-icon';
        manaCost.appendChild(img);
      }
      document.getElementById('artworkImg').src = 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80';
      document.getElementById('cardType').textContent = 'Superhero';
      document.getElementById('setIconImg').src = 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Star_icon-72a7cf.svg';
      document.getElementById('rulesBox').innerHTML = member.powers.map(p => `<div>${p}</div>`).join('');
      document.getElementById('illustrator').textContent = 'Illus. ' + member.secretIdentity;
      document.getElementById('copyright').textContent = `© ${data.formed} ${data.squadName}`;
    });
}); 