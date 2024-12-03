function mostrarExemplo(sistema) {
    let exemplo;
    if (sistema === 'hiragana') {
        exemplo = `
            <h3>Exemplo de Hiragana</h3>
            <p>Exemplo de letras: あ、い、う、え、お</p>
            <p>Palavra: こんにちは (Konnichiwa) - Olá/Boa Tarde</p>
        `;
    } else if (sistema === 'katakana') {
        exemplo = `
            <h3>Exemplo de Katakana</h3>
            <p>Exemplo de letras: ア、イ、ウ、エ、オ</p>
            <p>Palavra: コンピュータ (Konpyu-ta) - Computador</p>
        `;
    } else if (sistema === 'kanji') {
        exemplo = `
            <h3>Exemplo de Kanji</h3>
            <p>Exemplo de caracteres: 日、月、火、水</p>
            <p>Palavra: 日本 (Nihon) - Japão</p>
        `;
    }

    // Mostra a caixa com o exemplo
    document.getElementById("exemplo-box").innerHTML = exemplo;
    document.getElementById("exemplo-box").style.display = "block";
}

function esconderExemplo(sistema) {
    // Esconde a caixa quando o mouse sai da área
    document.getElementById("exemplo-box").style.display = "none";
}
