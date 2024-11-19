// Script para abrir e fechar o modal
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('addModal');
    
    // Função para abrir o modal
    function openModal() {
        modal.style.display = "flex";
    }

    // Exemplo de como abrir o modal (pode ser chamado em um evento)
    openModal();
    
    // Função para fechar o modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
