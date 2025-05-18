async function enviarMensagem() {
    const entrada = document.getElementById("entrada").value.trim();
    if (!entrada) return;

    const respostaBox = document.getElementById("dialogo");
    respostaBox.innerText = "Consultando o Oráculo...";

    try {
        const resposta = await fetch("/interagir", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mensagem: entrada })
        });
        const dados = await resposta.json();
        respostaBox.innerText = dados.resposta || "O Oráculo não respondeu.";

        if (dados.encerrar) {
            document.getElementById("entrada").disabled = true;
        }
    } catch (error) {
        respostaBox.innerText = "Erro ao consultar o Oráculo.";
        console.error(error);
    }

    document.getElementById("entrada").value = "";
}
